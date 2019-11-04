# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import xmltodict

from pybrreg.utils.logging import getLogger


log = getLogger(__name__)


def perform_precontrol(client, xml):
    log.info('Preparing to request Brreg:validereInput (Precontrol)')
    log.debug('Input XML to validate: {}'.format(xml))
    log.debug('Dispatching request to service.')
    brreg_response = client.validate_input(xml)
    log.debug('Parsing response from service.')

    parsed = xmltodict.parse(brreg_response, dict_constructor=dict)
    if not parsed.get('prekontrollResponse'):
        raise ValueError('Precontrol could not be performed. Server response:\n{}'.format(xml))
    response = parsed['prekontrollResponse']
    if not isinstance(response, dict):
        return {'error': 'Invalid message formatting'}
    if response['kontroll'] == 'OK':
        return {'status': 'OK'}
    if response['kontroll'] == 'SPERRE':
        string_or_list = response['sperrer']['sperre']
        return {
            'status': 'Rejected',
            'errors': [client.error(sperre) for sperre in
                       response['sperrer']['sperre']] if isinstance(string_or_list, list)
            else [client.error(string_or_list)]
        }
    if response['kontroll'] == 'INVALID_XML':
        return {'status': 'Rejected', 'fail': 'Invalid XML. Please contact support.'}
    if response['kontroll'] == 'SYSTEMFEIL':
        return {'status': 'Rejected', 'fail': 'Unable to contact external service. Please try again later.'}
    raise ValueError('Unexpected response from precontrol service:\n {}'.format(brreg_response))
