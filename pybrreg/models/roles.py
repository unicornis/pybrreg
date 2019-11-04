# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from copy import deepcopy

from .xsd import hentRoller


class RoleData(object):

    def __init__(self, xml):
        elem = hentRoller.CreateFromDocument(xml)
        self.header = Header(elem.responseHeader)
        self.message = Message(elem.melding) if elem.melding else None

    def json(self):
        if self.message:
            return self.message.json()
        else:
            return self.get_error()

    def get_error(self):
        return {
            'error': {
                'code': self.header.sub_status[0].status_code,
                'description': self.header.sub_status[0].status,
            }
        }


class Header(object):

    def __init__(self, elem):
        self.organisation_number = elem.orgnr
        self.processing_date = elem.prossessDato
        self.service = elem.tjeneste
        self.primary_status = elem.hovedStatus
        self.sub_status = [Status(sub_element) for sub_element in elem.underStatus.underStatusMelding]


class Status(object):
    def __init__(self, elem):
        self.status_code = unicode(elem.kode)
        self.status = elem.value()


class Message(object):

    def __init__(self, elem):
        self.organisation_number = OrganisationNumber(elem.organisasjonsnummer)
        self.contact_person = Grouping(elem.kontaktperson) if elem.kontaktperson else None
        self.board = Board(elem.styre) if elem.styre else None
        self.auditor = Grouping(elem.revisor) if elem.revisor else None
        self.accountant = Grouping(elem.regnskapsfoerer) if elem.regnskapsfoerer else None
        self.participants = Grouping(elem.deltakere) if elem.deltakere else None
        self.complements = Grouping(elem.komplementar) if elem.komplementar else None
        self.co_owners = Grouping(elem.sameiere) if elem.komplementar else None
        self.owning_municipality = Grouping(elem.eierkommune) if elem.eierkommune else None

    def json(self):
        return {
            'contact_person': self.contact_person.json(with_type=True) if self.contact_person else None,
            'board': self.board.json() if self.board else None,
            'auditor': self.auditor.json() if self.auditor else None,
            'accountant': self.accountant.json() if self.accountant else None,
            'participants': self.participants.json() if self.participants else None,
            'complements': self.complements.json() if self.complements else None,
            'co_owners': self.co_owners.json() if self.co_owners else None,
            'owning_municipality': self.owning_municipality.json() if self.owning_municipality else None
        }


class Grouping(object):

    def __init__(self, base_elem):
        elem = base_elem.samendring[0]
        self.description = elem.beskrivelse
        self.registration_date = elem.registreringsDato
        self.type = elem.samendringstype
        self.roles = [Role(role) for role in elem.rolle]
        self.trailer_text = getattr(elem, 'trailerTekst', None)
        self.header_text = getattr(elem, 'headerTekst', None)
        self.gender_representation = getattr(elem, 'kjonnsrepresentasjon', None)

    def json(self, with_type=False):
        return [role.json(with_type) for role in self.roles]


class Board(Grouping):

    def json(self):
        ret = {}
        chair = None
        deputy_chair = None
        member = None
        for role in self.roles:
            rtype, data = role.json(with_type=True)
            if rtype == 'chair':
                chair = data
            if rtype == 'deputy_chair':
                deputy_chair = data
            if rtype == 'member':
                member = data

        ret['chair'] = chair if chair else None
        ret['deputy_chair'] = deputy_chair if deputy_chair else None
        ret['member'] = member if member else None
        return ret


class Role(object):

    role_types = {
        'LEDE': 'chair',
        'NEST': 'deputy_chair',
        'MEDL': 'member',
        'REVI': 'auditor',
        'REGN': 'accountant',
        'DAGL': 'gm_gs',
        'KONT': 'contact_person',
        'FFØR': 'business_manager',
    }

    def __init__(self, elem):
        self.description = elem.beskrivelse
        self.role_type = elem.rolletype
        if getattr(elem, 'person', None):
            self.entities = [Person(person) for person in elem.person]
        if getattr(elem, 'enhet', None):
            self.entities = [Entity(entity) for entity in elem.enhet]

    def json(self, with_type=False):
        data = [entity.json() for entity in self.entities]
        if with_type:
            try:
                return self.role_types[self.role_type], data
            except Exception as e:
                return 'unknown', data
        else:
            return data


class BaseEntity(object):

    _resigned = None

    def __init__(self, elem):
        self.description = elem.beskrivelse
        self.status_code = elem.statuskode
        self.address1 = getattr(elem, 'adresse1', None)
        self.address2 = getattr(elem, 'adresse2', None)
        self.address3 = getattr(elem, 'adresse3', None)
        self.zip_code = getattr(elem, 'postnr', None)
        self.location = getattr(elem, 'poststed', None)
        self.country = Country(getattr(elem, 'land', None)) if hasattr(elem, 'land') else None
        self.responsibility = getattr(elem, 'ansvarsdel', None)
        self.resigned = getattr(elem, 'fratraadt', None)
        self.resigned_text = getattr(elem, 'fratraadtTekst', None)
        self.accountant_category = getattr(elem, 'revisorKategori', None)
        self.accountant_r_code = getattr(elem, 'revisorRkode', None)
        self.re_text = getattr(elem, 'reTekst', None)
        self.role_free_text = getattr(elem, 'rolleFriTekst', None)

    def json(self, remove_none=False):
        ret = {
            'description': self.description,
            'status_code': self.status_code,
            'address1': self.address1,
            'address2': self.address2,
            'address3': self.address3,
            'zip_code': self.zip_code,
            'location': self.location,
            'country_code': self.country.country_code,
            'country': self.country.country,
            'resigned': self.resigned,
            'responsibility': self.responsibility,
            'resigned_text': self.resigned_text,
            'accountant_category': self.accountant_category,
            'accountant_r_code': self.accountant_r_code,
            're_text': self.re_text,
            'role_free_text': self.role_free_text
        }
        return self.clean_json(ret) if remove_none else ret

    @staticmethod
    def clean_json(data):
        copied = deepcopy(data)
        for key, value in copied.iteritems():
            if value is None:
                data.pop(key)

        return data

    @property
    def resigned(self):
        return self._resigned

    @resigned.setter
    def resigned(self, value):
        self._resigned = True if value == 'J' else False


class Country(object):

    def __init__(self, elem):
        self.country_code = elem.landkode4
        self.country = elem.value()


class Person(BaseEntity):

    def __init__(self, base_elem):
        elem = base_elem
        super(Person, self).__init__(elem)
        self.guardian_text = getattr(elem, 'vergeTekst', None)
        self.birth = elem.fodselsdato
        self.first_name = elem.fornavn
        self.middle_name = getattr(elem, 'mellomnavn', None)
        self.last_name = elem.slektsnavn

    def json(self, remove_none=False):
        ret = super(Person, self).json()
        ret['name'] = self.name
        ret['birth_date'] = self.birth
        ret['guardian_text'] = self.guardian_text

        return self.clean_json(ret)

    @property
    def name(self):
        parts = [self.first_name, self.middle_name if self.middle_name else '', self.last_name]
        return ' '.join(parts)


class Entity(BaseEntity):

    def __init__(self, base_elem):
        elem = base_elem
        super(Entity, self).__init__(elem)
        self.organisation_number = elem.orgnr
        self.name1 = elem.navn1
        self.name2 = getattr(elem, 'navn2', None)
        self.name3 = getattr(elem, 'navn3', None)
        self.name4 = getattr(elem, 'navn4', None)
        self.name5 = getattr(elem, 'navn5', None)

    def json(self, remove_none=False):
        ret = super(Entity, self).json()
        ret['name'] = self.name1
        ret['name2'] = self.name2
        ret['name3'] = self.name3
        ret['name4'] = self.name4
        ret['name5'] = self.name5
        ret['organisation_number'] = self.organisation_number

        return self.clean_json(ret)


class OrganisationNumber(object):

    def __init__(self, elem):
        self.registration_date = elem.registreringsDato
        self.value = elem.value
