# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import xmltodict

from ..exceptions import BrregServiceError
from ..utils import brreg_fields


def parse_response(response):
    """
    Parse a response from Brreg, given from Suds.
    Args:
        response: Suds response object

    Returns:
        header: Content header describing metadata for this request
        content: Main content with the response

    Raises:
        BrregServiceError: If there was an error in processing the request, or if the server
            responded with an error (i.e. 500).
    """
    http_code, response = response
    if http_code == 200:

        parsed_response = xmltodict.parse(response)
        header = parsed_response["grunndata"]["responseHeader"]
        content = parsed_response["grunndata"].get("melding")

        if header["hovedStatus"] == "-1":
            main_code, sub_code, message = _parse_error_data(header)
            error_context = {
                "main_status_code": main_code,
                "sub_status_code": sub_code,
                "http_code": http_code
            }
            raise BrregServiceError(message, **error_context)
        else:
            return header, content
    else:
        raise BrregServiceError(unicode(response), http_code=http_code)


def _parse_error_data(header):
    main_status_code = header["hovedStatus"]

    sub_status = header["underStatus"]["underStatusMelding"]

    sub_status_code = sub_status["@kode"]
    message = sub_status["#text"]

    return main_status_code, sub_status_code, message


def _traverse(data, path):
    """
    Recursively get the value specified by `path` from `data`.
    Return None if the path does not lead to a value.

    >>> nested_dict = {'root': {'nested_key': 'nested_value'}}
    >>> _traverse(nested_dict, ['root', 'nested_key'])
    'nested_value'
    >>> _traverse(nested_dict, ['root', 'nonexistent_key'])
    >>> _traverse(nested_dict, ['nonexistent_root', 'nonexistent_key'])
    """
    def get_next_dict_value():
        return data.get(path[0])

    def get_next_list_value():
        return data[0]


    if not data:
        return None

    # Determine dataType and traverse accordingly
    if isinstance(data, dict):
        if len(path) == 1:
            return get_next_dict_value()
        return _traverse(get_next_dict_value(), path[1:])
    elif isinstance(data, list):
        if len(data) == 1:
            return get_next_list_value()
        return _traverse(get_next_list_value(), path[1:])
    return None


def _transform_field(brreg_data, field):
    value = _traverse(brreg_data, field.path)
    return field.transform(value) if value else None


def transform(brreg_data, service_fields):
    """
    Return a tree structure similar to `service_fields`, where the bottom nodes
    are transformed values from `brreg_data`.
    """
    return {
        key: transform(brreg_data, value) if isinstance(value, dict)
        else _transform_field(brreg_data, value)
        for key, value in service_fields.iteritems()
    }


def coded_description(code, description):
    return {
        'code': code,
        'description': description,
    }


def error(message):
    return {'error': coded_description(
        code=message['@kode'],
        description=message['#text'])
    }


def get_data(brreg_xml):
    brreg_dict = xmltodict.parse(brreg_xml, dict_constructor=dict)
    try:
        return brreg_dict['grunndata']['melding']
    except KeyError:
        raise ValueError(error(brreg_dict['grunndata']['responseHeader']['underStatus']['underStatusMelding']))


def transform_brreg_data(brreg_xml, service):
    fields = {
        'hentBasisdataFdato': {
            'name': brreg_fields.OrganisationName(['navn']),
            'organisation_number': brreg_fields.Text(['organisasjonsnummer']),
            'founding_date': brreg_fields.Text(['stiftelsesdato']),
            'business_address': brreg_fields.Address(['forretningsAdresse']),
            'postal_address': brreg_fields.Address(['postAdresse']),
            'contact_person': brreg_fields.Person(['kontaktperson', 'samendring', 'rolle', 'person']),
            'organisation_type': brreg_fields.OrganisationType(['organisasjonsform']),
            'description': brreg_fields.Text(['formaal', 'virksomhetArtBransje']),
            'bylaw_purpose': brreg_fields.Text(['formaal', 'vedtektsfestetFormaal']),
            'language': brreg_fields.Language(['maalform']),
        },
        'hentRollerFdato': {
            'board': {
                'chair': brreg_fields.PersonOrPersons(['styre', 'samendring', 'rolle'],
                                                      where=('@rolletype', 'LEDE')),
                'deputy_chair': brreg_fields.PersonOrPersons(['styre', 'samendring', 'rolle'],
                                                             where=('@rolletype', 'NEST')),
                'member': brreg_fields.PersonOrPersons(['styre', 'samendring', 'rolle'],
                                                       where=('@rolletype', 'MEDL')),
            },
            'accountant': brreg_fields.EntityOrEntities(['regnskapsfoerer', 'samendring', 'rolle']),
            'auditor': brreg_fields.EntityOrEntities(['revisor', 'samendring', 'rolle']),
        },
        'hentFrivillighet': {
            'registration_date': brreg_fields.RegistrationDate(['frivillighet', 'registrertFrivillighet']),
            'account_number': brreg_fields.Text(['frivillighet', 'kontonummer']),
            'categories': brreg_fields.RankedCategories(['frivillighet', 'kategorier', 'kategori']),
            'reports_bylaws': brreg_fields.Text(['frivillighet', 'vedtekter']),
            'last_registered_bylaws': brreg_fields.RegistrationDate(['frivillighet', 'sisteRegistrerteVedtekter']),
            'reports_accounts': brreg_fields.Text(['frivillighet', 'aarsregnskap']),
            'account_period': brreg_fields.Text(['frivillighet', 'regnskapsperiode']),
            'grassroot_share': brreg_fields.Text(['frivillighet', 'grasrotandel']),
        },
        'hentKontaktdata': {
            'phone_number': brreg_fields.Text(['telefonnummer']),
            'fax_number': brreg_fields.Text(['telefaksnummer']),
            'mobile_number': brreg_fields.Text(['mobiltelefonnummer']),
            'email': brreg_fields.Text(['epostadresse']),
            'website': brreg_fields.Text(['hjemmesideadresse']),
        }
    }
    try:
        brreg_data = get_data(brreg_xml)
    except ValueError as error:
        return error.message
    return transform(brreg_data, fields[service])
