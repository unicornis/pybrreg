# -*- coding: utf-8 -*-
import pytest
import unittest

from pybrreg.utils.converters import convert_signature_procuration, format_person, extract_settings


# CASE 1
person1 = {
    'input': {
        u'@beskrivelse': 'Lever', 
        u'@statuskode': 'L', 
        u'fodselsdato': '1974-08-19', 
        u'fornavn': 'Martine', 
        u'slektsnavn': 'Andersen', 
        u'adresse1': 'Mosseveien 128', 
        u'postnr': '1580', 
        u'poststed': 'RYGGE', 
        u'land': {
            u'@landkode4': 'NOR', 
            '#text': 'Norge'
            }, 
        u'fratraadt': 'N'},
    'expected': {
        'name': "Martine Andersen",
        'birth_date': '1974-08-19'
    }
}

# CASE 2
signature1 = {
    u'@beskrivelse': 'Signatur', 
    u'@registreringsDato': '2014-02-26', 
    u'@samendringstype': 'SIGN', 
    u'headerTekst': 'Styret i fellesskap.'
}
signature1_expected_result = {
    'text': ['Styret i fellesskap.'], 'custom_text': []
}

# CASE 3
signature2 = {
    u'@beskrivelse': 'Signatur', 
    u'@registreringsDato': '2011-03-02', 
    u'@samendringstype': 'SIGN', 
    u'headerTekst': 'Styret i fellesskap. Styrets leder alene.'
}
signature2_expected_result = {
    'text': ['Styret i fellesskap.', 'Styrets leder alene.'], 'custom_text': []
}

# CASE 4
proc0_2roles = {
    u'@beskrivelse': 'Prokura', 
    u'@registreringsDato': '2012-07-30', 
    u'@samendringstype': 'PROK', 
    u'rolle': {
        u'@beskrivelse': 'Prokura hver for seg', 
        u'@rolletype': 'POHV', 
        u'person': [{
            u'@beskrivelse': 'Lever', 
            u'@statuskode': 'L', 
            u'fodselsdato': '1991-02-05', 
            u'fornavn': 'Olav Magne', 
            u'slektsnavn': 'Batt', 
            u'adresse1': 'Bogstadveien 3', 
            u'postnr': '0355', 
            u'poststed': 'OSLO', 
            u'land': {
                u'@landkode4': 'NOR', 
                '#text': 'Norge'}, 
            u'fratraadt': 'N'
            },{
            u'@beskrivelse': 'Lever', 
            u'@statuskode': 'L', 
            u'fodselsdato': '1929-11-20', 
            u'fornavn': 'Ørjan', 
            u'slektsnavn': 'Thorbjørnsen', 
            u'adresse1': 'Hegermanns Gate 10', 
            u'postnr': '0478', 
            u'poststed': 'OSLO', 
            u'land': {
                u'@landkode4': 'NOR', 
                '#text': 'Norge'}, 
            u'fratraadt': 'N'
        }]
    }
}
proc0_2roles_expected_result = {
    'roles': [{
            'roletype': 'POHV',
            'description': 'Prokura hver for seg',
            'person': [
                {'name':'Olav Magne Batt', 'birth_date':'1991-02-05'},
                {'name':'Ørjan Thorbjørnsen', 'birth_date':'1929-11-20'}
            ],
        }]
}

# CASE 5 
proc2_1custom = {
        u'@beskrivelse': 'Prokura', 
        u'@registreringsDato': '2012-12-01', 
        u'@samendringstype': 'PROK', 
        u'headerTekst': 'Styrets leder alene. To styremedlemmer i fellesskap.', 
        u'trailerTekst': 'Kan delegeres enkeltpersoner ved styrevedtak'
    }
proc2_1custom_expected = {
    'text': ['Styrets leder alene.', 'To styremedlemmer i fellesskap.'],
    'custom_text': ['Kan delegeres enkeltpersoner ved styrevedtak']
}

# CASE 6 // Punctuation
sign_custom1 = {
        u'@beskrivelse': 'Signatur', 
        u'@registreringsDato': '2010-01-21', 
        u'@samendringstype': 'SIGN', 
        u'trailerTekst': 'Leder og kasserer hver for seg.'
    }
sign_custom1_expected ={
    'custom_text': ['Leder og kasserer hver for seg.'],
    'text': []
}

# CASE 7 // No pnuctuation
sign_custom1_nopunc = {
        u'@beskrivelse': 'Signatur', 
        u'@registreringsDato': '2010-01-21', 
        u'@samendringstype': 'SIGN', 
        u'trailerTekst': 'Leder og kasserer hver for seg'
    }
sign_custom1_nopunc_expected ={
    'custom_text': ['Leder og kasserer hver for seg'],
    'text': []
}


# CASE 8
complete_set = {u'@tjeneste': 'hentProkuraSignatur', 
u'organisasjonsnummer': {
    u'@registreringsDato': '2009-05-20', 
    '#text': '893429662'
    }, 
    u'prokura': {
        u'samendring': {
            u'@beskrivelse': 'Prokura', 
            u'@registreringsDato': '2016-03-17', 
            u'@samendringstype': 'PROK', 
            u'rolle': {
                u'@beskrivelse': 'Prokura', 
                u'@rolletype': 'PROK', 
                u'person': {
                    u'@beskrivelse': 'Lever', 
                    u'@statuskode': 'L', 
                    u'fodselsdato': '1996-07-30', 
                    u'fornavn': 'Sigrid Johanne', 
                    u'slektsnavn': 'Gol', 
                    u'adresse1': 'Frydenbergvegen 1 B', 
                    u'postnr': '7050', 
                    u'poststed': 'TRONDHEIM', 
                    u'land': {
                        u'@landkode4': 'NOR', 
                        '#text': 'Norge'}, 
                    u'fratraadt': 'N'}
                }
        }
    }, 
    u'signatur': {
        u'samendring': {
            u'@beskrivelse': 'Signatur', 
            u'@registreringsDato': '2009-05-20', 
            u'@samendringstype': 'SIGN', 
            u'headerTekst': 'To styremedlemmer i fellesskap.'
        }        
    }
}
complete_set_expected = {
    'procuration':{
        'roles': [{
                    'roletype': 'PROK',
                    'description': 'Prokura',
                    'person': [
                        {'name':'Sigrid Johanne Gol', 'birth_date':'1996-07-30'}
                    ],
                }]
    },
    'signature': {
        'text': ['To styremedlemmer i fellesskap.'], 'custom_text': []
    }
}


class ConverterTests(unittest.TestCase):

    def setUp(self):
        self.person1 = person1

    # CASE 1
    def test_person1_formatted(self):
        self.assertEqual(format_person(self.person1['input']), self.person1['expected'])

    def test_person1_not_formatted(self):
        self.assertNotEqual(self.person1['input'], self.person1['expected'])


    # CASE 2
    def test_extract_basic_signature_settings(self):
        # 1 signaturesetting, no roles
        self.assertEqual(signature1_expected_result, extract_settings(signature1))

    # CASE 3
    def test_extract_double_signature_settings(self):
        # 2 signaturesetting, no roles
        self.assertEqual(signature2_expected_result, extract_settings(signature2))

    # CASE 4
    def test_extract_zero_procura_2roles_settings(self):
        self.assertEqual(proc0_2roles_expected_result, extract_settings(proc0_2roles))

    # CASE 5
    def test_proc_with_2standard_1custom_text_no_punctuation(self):
        self.assertEqual(proc2_1custom_expected, extract_settings(proc2_1custom))        

    # CASE 6
    def test_sign_custom1_with_punctuation(self):
        self.assertEqual(sign_custom1_expected, extract_settings(sign_custom1))

    # CASE 7
    def test_sign_custom1_no_punctuation(self):
        self.assertEqual(sign_custom1_nopunc_expected, extract_settings(sign_custom1_nopunc))

    # CASE 8
    def test_complete_case(self):
        result = convert_signature_procuration(complete_set)
        self.assertEqual(complete_set_expected['signature'], result['signature'])
        self.assertEqual(complete_set_expected['procuration'], result['procuration'])
