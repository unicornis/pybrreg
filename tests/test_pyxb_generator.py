# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
from datetime import datetime
from pybrreg.brreg_report_changes.pyxb_tools.converters import (strip_default_namespace, 
  make_header, make_melding, integrasjonPYXB, make_xml)

TODAY = datetime.now().date()
AA_DICT = {
  # Header:
  'header': {  'SLsysId': '1001',
    'SLsysMeldingsId': 'a',
    'sakstype': {
        'hovedsakstype': 'N',
        'undersakstype': 'NY'
    },
    'organisasjonsform': 'FLI',
    'status': {
        'ERstatus': 'J',
        'FVstatus': 'J'
    },
  },
  # Elektronisk varslingsadresse
  'elektroniskVarslingsadresse': {
    'epostadresse': 'naroyfisk@eksempel.no',
    'mobil': {
      'prefiks': '47',
      'mobilnummer': '44994499',
    }
  },
  # Melding:
  'er': {
    'navn':{
          'navn1': 'Nærøy Jakt og Fisk',
          },
    'stiftelsesdato': '1920-09-09',
    'forretningsAdresse': { 
      'infoType': 'FADR',
      'register': 'ER',
      'adresse1': 'Testgata 5',
      'adresse2': 'Testgata X',
      'adresse3': 'Testgata Y',
      'postnr': '7970',
      'poststed': 'Kolvereid',
      'kommunenummer': '1751',
      'kommune': 'Nærøy',
      'landkode': 'NO',
      'land': 'Norge'
    },
    'hjemmeside':'www.eksempel.no',
    'epost': 'post@eksempel.no',
    'telefon': '77 77 77 77',
    'mobil': '99999999',
    'telefaks': '55555555',

    'formaal': 'Idrettslag',
      
    
    "dagligLeder": {
      "person": {
        "fodselsnr": "18048100232",
        "slektsnavn": "Jakobsen",
        "dsfverifisert": True,
        "navn": "Maja Jakobsen",
      }
    },     
    'kontaktperson':{
      'rolle': "KONT",      
        'person':{
          'fodselsnr':'17033900562',
          'slektsnavn':'Grimstad',
        }    
    },
  
    'styre':  {
      'infoType': "STYR",
      'register': "ER",
        
      'rolle':[
            {'rolle': "LEDE",
              'person':{
                'fodselsnr': '17033900562',
                'slektsnavn': 'Grimstad',
                'navn': 'Navn Grimstad'
              }
            },
            {'rolle': "MEDL",
              'person': {
                'fodselsnr': '17035600213',
                'slektsnavn':'Augestad'
                }
            }
          ]
    },
    'signatur': {
      'infoType': "SIGN" ,
      'register': "ER",
      'signaturTekst': ['To styremedlemmer i fellesskap.', 'Daglig leder alene.'],

    },
    'prokura': {
      'infoType': "PROK" ,
      'register': "ER",
      'prokuraTekst': ['To styremedlemmer i fellesskap.', 'Daglig leder alene.'],
    },
  
  'maalform': 'B',

  'ansatte': 'N',
  },

  'fv': {
    'grasrotandel': 'J',
  
    'kategori':[{
          'infoType': "KATG",
          'register': "FV",
          'kode':'1200',
          'rangering':'1'}],
  
    'kontonummer': '44670546397',
  
    'meldepliktVedtekter':'N',
  
    'aarsregnskapLeveres': 'J',
  
    'regnskapsperiode': '3112',
  },

  "opplysningUtgaar": {
    "postAdresse": False,
    "forretningsAdresse": True,
    "hjemmeside": True,
    "epost": True,
    "telefon": False,
    "telefaks": False,
    "mobil": False,
    "kontaktperson": False,
    "dagligLeder": False,
    "forretningsforer": False,
    "styre": False,
    "signatur": False,
    "prokura": False,
    "kontonummer": False,
  },
  'vedlegg':['VEDT',
          'STIF',
          'PAAR',
          'SGDK',
    ],
  'signerer':['17033900562'],

}
IDENTICAL_ADDRESSES = {
  # Header:
  'header': {  'SLsysId': '1001',
    'SLsysMeldingsId': 'a',
    'sakstype': {
        'hovedsakstype': 'N',
        'undersakstype': 'NY'
    },
    'organisasjonsform': 'FLI',
    'status': {
        'ERstatus': 'J',
        'FVstatus': 'J'
    },
  },
  # Elektronisk varslingsadresse
  'elektroniskVarslingsadresse': {
    'epostadresse': 'naroyfisk@eksempel.no',
    'mobil': {
      'prefiks': '47',
      'mobilnummer': '44994499',
    }
  },
  # Melding:
  'er': {
    'navn':{
          'navn1': 'Nærøy Jakt og Fisk',
          },
    'stiftelsesdato': '1920-09-09',
    'postAdresse': { 
      'infoType': 'PADR',
      'register': 'ER',
      'adresse1': 'Testgata 5',
      'adresse2': 'Testgata X',
      'adresse3': 'Testgata Y',
      'postnr': '7970',
      'poststed': 'Kolvereid',
      'kommunenummer': '1751',
      'kommune': 'Nærøy',
      'landkode': 'NO',
      'land': 'Norge'
    },
    'forretningsAdresse': { 
      'infoType': 'FADR',
      'register': 'ER',
      'adresse1': 'Testgata 5',
      'adresse2': 'Testgata X',
      'adresse3': 'Testgata Y',
      'postnr': '7970',
      'poststed': 'Kolvereid',
      'kommunenummer': '1751',
      'kommune': 'Nærøy',
      'landkode': 'NO',
      'land': 'Norge'
    },
    'hjemmeside':'www.eksempel.no',
    'epost': 'post@eksempel.no',
    'telefon': '77 77 77 77',
    'mobil': '99999999',
    'telefaks': '55555555',

    'formaal': 'Idrettslag',
     
    'kontaktperson':{
      'rolle': "KONT",      
        'person':{
          'fodselsnr':'17033900562',
          'slektsnavn':'Grimstad',
        }    
    },

  
    'styre':  {
      'infoType': "STYR",
      'register': "ER",
        
      'rolle':[
            {'rolle': "LEDE",
              'person':{
                'fodselsnr': '17033900562',
                'slektsnavn': 'Grimstad',
                'navn': 'Navn Grimstad'
              }
            },
            {'rolle': "MEDL",
              'person': {
                'fodselsnr': '17035600213',
                'slektsnavn':'Augestad'
                }
            }
          ]
    },
    'signatur': {
      'infoType': "SIGN" ,
      'register': "ER",
      'signaturTekst': ['To styremedlemmer i fellesskap.', 'Daglig leder alene.'],

    },
    'prokura': {
      'infoType': "PROK" ,
      'register': "ER",
      'prokuraTekst': ['To styremedlemmer i fellesskap.', 'Daglig leder alene.'],
    },
  
  'maalform': 'B',

  'ansatte': 'N',
  },

  'fv': {
    'grasrotandel': 'J',
  
    'kategori':[{
          'infoType': "KATG",
          'register': "FV",
          'kode':'1200',
          'rangering':'1'}],
  
    'kontonummer': '44670546397',
  
    'meldepliktVedtekter':'N',
  
    'aarsregnskapLeveres': 'J',
  
    'regnskapsperiode': '3112',
  },

  "opplysningUtgaar": {
    "postAdresse": False,
    "forretningsAdresse": True,
    "hjemmeside": True,
    "epost": True,
    "telefon": False,
    "telefaks": False,
    "mobil": False,
    "kontaktperson": False,
    "dagligLeder": False,
    "forretningsforer": False,
    "styre": False,
    "signatur": False,
    "prokura": False,
    "kontonummer": False,
  },
  'vedlegg':['VEDT',
          'STIF',
          'PAAR',
          'SGDK',
    ],
  'signerer':['17033900562'],

}

ELADR_EMAIL_DICT = {
  # Header:
  'header': {  'SLsysId': '1001',
    'SLsysMeldingsId': 'a',
    'sakstype': {
        'hovedsakstype': 'N',
        'undersakstype': 'NY'
    },'organisasjonsform': 'FLI',
    'status': {
        'ERstatus': 'J',
        'FVstatus': 'J'},
  },
  # Elektronisk varslingsadresse
  'elektroniskVarslingsadresse': {
    'epostadresse': 'naroyfisk@eksempel.no',
  },
  # Melding:
  'er': {},
  'fv': {},
  'signerer':['17033900562'],
}
ELADR_MOBILE_DICT = {
  # Header:
  'header': {  'SLsysId': '1001',
    'SLsysMeldingsId': 'a',
    'sakstype': {
        'hovedsakstype': 'N',
        'undersakstype': 'NY'
    },'organisasjonsform': 'FLI',
    'status': {
        'ERstatus': 'J',
        'FVstatus': 'J'},
  },
  # Elektronisk varslingsadresse
  'elektroniskVarslingsadresse': {
    'mobil': {
      'prefiks': '47',
      'mobilnummer': '44994499',
    }
  },
  # Melding:
  'er': {},
  'fv': {},
  'signerer':['17033900562'],
}
ELADR_WRONG_TYPE_DICT = {
  # Header:
  'header': {  'SLsysId': '1001',
    'SLsysMeldingsId': 'a',
    'sakstype': {
        'hovedsakstype': 'E',
        'undersakstype': 'EN'
    },'organisasjonsform': 'FLI',
    'status': {
        'ERstatus': 'J',
        'FVstatus': 'J'},
  },
  # Elektronisk varslingsadresse
  'elektroniskVarslingsadresse': {
    'epostadresse': 'naroyfisk@eksempel.no',
    'mobil': {
      'prefiks': '47',
      'mobilnummer': '44994499',
    }
  },
  # Melding:
  'er': {},
  'fv': {},
  'signerer':['17033900562'],
}


INCOMPLETE_DICT = {
  'er': {  
    'maalform':'B',

    'ansatte': 'N',
  },
  'fv': {
    'grasrotandel':'J',
  
    'kategori':[{
          'infoType': "KATG",
          'register': "FV",
          'kode':'1200',
          'rangering':'1'}],
  
    'kontonummer': '44670546397'
    }
}

wrong_content_onechar_fields = {
  # Melding:
  'er': {
    'ansatte': 'X',
    'maalform': 'Y',
  },
  'fv': {
    'grasrotandel': 'X',
    'meldepliktVedtekter':'X',
    'aarsregnskapLeveres': 'X',
    'endringAvVedtekter': 'X',
  },
}
wrong_numeric_content_onechar_fields = {
  # Melding:
  'er': {
    'ansatte': '0',
    'maalform': '0',
  },
  'fv': {
    'grasrotandel': '1',
    'meldepliktVedtekter':'1',
    'aarsregnskapLeveres': '0',
    'endringAvVedtekter': '2',
  },
}
wrong_whitespace_content_onechar_fields = {
  # Melding:
  'er': {
    'ansatte': ' J',
    'maalform': 'B ',
  },
  'fv': {
    'grasrotandel': 'N ',
    'meldepliktVedtekter':' J ',
    'aarsregnskapLeveres': 'J',
    'endringAvVedtekter': 'N',
  },
}
wrong_ammount_onechar_fields = {
  # Melding:
  'er': {
    'ansatte': 'JN',
    'ansatte': 'NJ',
    'maalform': 'BN',
  },
  'fv': {
    'grasrotandel': 'JN',
    'meldepliktVedtekter':'JN',
    'aarsregnskapLeveres': 'JN',
    'endringAvVedtekter': 'JN',
  },
}
correct_changebylaws_field = {
  'er': {},
  'fv': {
    'endringAvVedtekter': 'J',
  },
}
wrong_changebylaws_field = {
  'er': {},
  'fv': {
    'grasrotandel': 'N',
    'meldepliktVedtekter':'N',
    'aarsregnskapLeveres': 'N',
    'endringAvVedtekter': 'N',  # wrong val
  },
  'signerer':['17033900562'], 
}

CORRECT_BYLAWS_DICT = {
  # Melding:
  'er': {},
  'fv': {
    'endringAvVedtekter': 'J',
  },
  'signerer':['17033900562'],
}

SIGN_PROK_ROLES = {
  "header": {  "SLsysId": "1001",
    "SLsysMeldingsId": "a",
    "sakstype": {
        "hovedsakstype": "E",
        "undersakstype": "EN"
    },"organisasjonsform": "FLI",
    "status": {
        "ERstatus": "J",
        "FVstatus": "N"},
  },
  "fv": {},
  "er": {
    "signatur": {
      "signaturTekst": ["To styremedlemmer i fellesskap.", "Daglig leder alene."],
       "rolle": [
            {
              "rolle": "SIGN",
              "person": {
                  "fodselsnr": "20044100127",
                  "slektsnavn": "Heldal",
                  "dsfverifisert": True,
                  "navn": "Bjørnar Heldal"
                },
              "rollenavn": "Signatur",
            },{
              "rolle": "SIHV",
              "person": {
                  "fodselsnr": "17033900562",
                  "slektsnavn": "Grimstad",
                  "dsfverifisert": True,
                  "navn": "Nils Grimstad"
              },
              "rollenavn": "Signatur hver for seg",
            },{
              "rolle": "SIFE",
              "person": {
                  "fodselsnr": "17035600213",
                  "slektsnavn": "Augestad",
                  "dsfverifisert": True,
                  "navn": "Nils Augestad"
              },
              "rollenavn": "Signatur i fellesskap",
            }
        ]
    },
    "prokura" :{
      "prokuraTekst": ["To styremedlemmer i fellesskap.", "Daglig leder alene."],
      "rolle": [{
                "rolle": "PROK",
                "person": {
                    "fodselsnr": "20044100127",
                    "slektsnavn": "Heldal",
                    "dsfverifisert": True,
                    "navn": "Bjørnar Heldal"
                },
                "rollenavn": "Prokura",
            },{
                "rolle": "POHV",
                "person": {
                    "fodselsnr": "17033900562",
                    "slektsnavn": "Grimstad",
                    "dsfverifisert": True,
                    "navn": "Nils Grimstad"
                },
                "rollenavn": "Prokura hver for seg",
            },{
                "rolle": "POFE",
                "person": {
                    "fodselsnr": "17035600213",
                    "slektsnavn": "Augestad",
                    "dsfverifisert": True,
                    "navn": "Nils Augestad"
                },
                "rollenavn": "Prokura i fellesskap",
            }
        ]
    }
  }
}

full_nny_message = {'elektroniskVarslingsadresse': {'epostadresse': 'test@test.no'},
 'er': {'ansatte': 'N',
  'formaal': 'Et fint form\xe5l',
  'forretningsAdresse': {'adresse1': 'Harald Galemanns Plass 95',
   'adresse2': '',
   'adresse3': '',
   'kommune': 'Gj\xf8vik',
   'kommunenummer': '0502',
   'land': 'Norway',
   'landkode': 'no',
   'postnr': '2832',
   'poststed': 'Biri'},
  'maalform': 'B',
  'navn': {'navn1': 'Foreningen for utspekulerte',
   'navn2': 'ludospillere',
   'navnCounter': {'parts': 2, 'totalLength': 39}},
  'prokura': {'prokuraTekst': [u'Styrets leder og nestleder hver for seg.',
    'To styremedlemmer i fellesskap.'],
   'rolle': [{'person': {'dsfverifisert': True,
      'fodselsnr': '19096000173',
      'navn': 'Olav Batt',
      'slektsnavn': 'Batt'},
     'rolle': 'POFE',
     'rollenavn': ''},
    {'person': {'dsfverifisert': True,
      'fodselsnr': '19087400428',
      'navn': 'Martine Andersen',
      'slektsnavn': 'Andersen'},
     'rolle': 'POFE',
     'rollenavn': ''},
    {'person': {'dsfverifisert': True,
      'fodselsnr': '20112900196',
      'navn': '\xd8rjan Thorbj\xf8rnsen',
      'slektsnavn': 'Thorbj\xf8rnsen'},
     'rolle': 'POHV',
     'rollenavn': ''}]},
  'signatur': {'rolle': [{'person': {'dsfverifisert': True,
      'fodselsnr': '19096000173',
      'navn': 'Olav Batt',
      'slektsnavn': 'Batt'},
     'rolle': 'SIFE',
     'rollenavn': ''},
    {'person': {'dsfverifisert': True,
      'fodselsnr': '19087400428',
      'navn': 'Martine Andersen',
      'slektsnavn': 'Andersen'},
     'rolle': 'SIFE',
     'rollenavn': ''},
    {'person': {'dsfverifisert': True,
      'fodselsnr': '20044100127',
      'navn': 'Bj\xf8rnar Heldal',
      'slektsnavn': 'Heldal'},
     'rolle': 'SIFE',
     'rollenavn': ''},
    {'person': {'dsfverifisert': True,
      'fodselsnr': '17080921861',
      'navn': 'Jens \xd8deg\xe5rd',
      'slektsnavn': '\xd8deg\xe5rd'},
     'rolle': 'SIHV',
     'rollenavn': ''}],
   'signaturTekst': [u'Styrets leder alene.',
    'Styrets leder og nestleder hver for seg.',
    'Styrets leder og ett styremedlem i fellesskap.']},
  'stiftelsesdato': '2019-02-01',
  'styre': {'rolle': [{'person': {'dsfverifisert': True,
      'fodselsnr': '20112900196',
      'navn': '\xd8rjan Thorbj\xf8rnsen',
      'slektsnavn': 'Thorbj\xf8rnsen'},
     'rolle': 'LEDE',
     'rollenavn': 'Styreleder'},
    {'person': {'dsfverifisert': True,
      'fodselsnr': '19096000173',
      'navn': 'Olav Batt',
      'slektsnavn': 'Batt'},
     'rolle': 'NEST',
     'rollenavn': 'Nestleder'},
    {'person': {'dsfverifisert': True,
      'fodselsnr': '20044100127',
      'navn': 'Bj\xf8rnar Heldal',
      'slektsnavn': 'Heldal'},
     'rolle': 'MEDL',
     'rollenavn': 'Medlem'},
    {'person': {'dsfverifisert': True,
      'fodselsnr': '17080921861',
      'navn': 'Jens \xd8deg\xe5rd',
      'slektsnavn': '\xd8deg\xe5rd'},
     'rolle': 'MEDL',
     'rollenavn': 'Medlem'},
    {'person': {'dsfverifisert': True,
      'fodselsnr': '19087400428',
      'navn': 'Martine Andersen',
      'slektsnavn': 'Andersen'},
     'rolle': 'MEDL',
     'rollenavn': 'Medlem'},
    {'person': {'dsfverifisert': True,
      'fodselsnr': '18092532034',
      'navn': 'Ole \xd8deg\xe5rd',
      'slektsnavn': '\xd8deg\xe5rd'},
     'rolle': 'MEDL',
     'rollenavn': 'Medlem'},
    {'person': {'dsfverifisert': True,
      'fodselsnr': '11038329679',
      'navn': 'Sara B\xe5rdsen',
      'slektsnavn': 'B\xe5rdsen'},
     'rolle': 'MEDL',
     'rollenavn': 'Medlem'}]}},
 'fv': {'aarsregnskapLeveres': 'N',
  'grasrotandel': 'N',
  'kategori': [{'kode': '2300', 'rangering': '1'},
   {'kode': '1100', 'rangering': '2'}],
  'meldepliktVedtekter': 'N'},
 'header': {'SLsysId': '1002',
  'SLsysMeldingsId': 'Unicornis:HS2:36:54:1',
  'organisasjonsform': '',
  'sakstype': {'hovedsakstype': 'N', 'undersakstype': 'NY'},
  'status': {'ERstatus': 'J', 'FVstatus': 'J'}},
 'opplysningUtgaar': {'dagligLeder': False,
  'epost': False,
  'forretningsAdresse': False,
  'forretningsforer': False,
  'hjemmeside': False,
  'kontaktperson': False,
  'kontonummer': False,
  'mobil': False,
  'postAdresse': False,
  'prokura': False,
  'signatur': False,
  'styre': False,
  'telefaks': False,
  'telefon': False},
 'padr_registrert': False,
 'signerer': [u'20112900196'],
 'vedlegg': [u'PAAR', 'STIF', 'VEDT', 'SGDK']}


XB_EXPECTED_DATE_TAG = """<stiftelsesdato infoType="STID" register="ER">1920-09-09</stiftelsesdato>"""

XA_EXPECTED_ADDRESS_TAG = """<forretningsAdresse infoType="FADR" register="ER"><adresse1>Testgata 5</adresse1><adresse2>Testgata X</adresse2><adresse3>Testgata Y</adresse3><postnr>7970</postnr><poststed>Kolvereid</poststed><kommunenummer>1751</kommunenummer><kommune>Nærøy</kommune><landkode>NO</landkode><land>Norge</land></forretningsAdresse>"""
XB_EXPECTED_ADDRESS_TAG = """<forretningsAdresse infoType="FADR" register="ER"><adresse1>Testgata 5</adresse1><adresse2>Testgata X</adresse2><adresse3>Testgata Y</adresse3><postnr>7994</postnr><poststed>Kolvereid</poststed><kommunenummer>1755</kommunenummer><kommune>Leka</kommune><landkode>NO</landkode><land>Norge</land></forretningsAdresse>"""

XA_EXPECTED_NAME_TAG = """<navn infoType="NAVN" register="ER"><navn1>Nærøy Jakt og Fisk</navn1></navn>"""
XB_EXPECTED_NAME_TAG = """<navn infoType="NAVN" register="ER"><navn1>Naroy Jakt og Fisk</navn1></navn>"""

XB_EXPECTED_WEB_TAG = """<hjemmeside infoType="IADR" register="ER"><url>www.eksempel.no</url></hjemmeside>"""
XB_EXPECTED_MOB_TAG = """<mobil infoType="MTLF" register="ER"><nummer>99999999</nummer></mobil>"""
XB_EXPECTED_EMAIL_TAG = """<epost infoType="EPOS" register="ER"><epostAdresse>post@eksempel.no</epostAdresse></epost>"""

XB_EXPECTED_FORMAAL_TAG = """<formaal infoType="FORM" register="ER"><formaalTekst>Idrettslag</formaalTekst></formaal>"""
XB_EXPECTED_KONTAKTPERSON_TAG = """<kontaktperson infoType="KONT" register="ER"><rolle rolletype="KONT"><person><fodselsnr>17033900562</fodselsnr><slektsnavn>Grimstad</slektsnavn></person></rolle></kontaktperson>"""

BB_EXPECTED_HEADER_CONTENT = """<SLsysId>1001</SLsysId><SLsysMeldingsId>a</SLsysMeldingsId><sakstype><hovedsakstype>N</hovedsakstype><undersakstype>NY</undersakstype></sakstype><organisasjonsform><orgform>FLI</orgform></organisasjonsform><status><ERstatus>J</ERstatus><FVstatus>J</FVstatus></status>"""
BB_EXPECTED_HEADER_TAG_CONTENT = 'header MeldingsDato="%(today)s"' % {'today': TODAY}

BB_EXPECTED_DATE_TAG = """<stiftelsesdato infoType="STID" register="ER">1920-09-09</stiftelsesdato>"""

AA_EXPECTED_ADDRESS_TAG = """<forretningsAdresse infoType="FADR" register="ER" xmlns="http://schema.brreg.no/intef/integrasjonERFV"><adresse1>Testgata 5</adresse1><adresse2>Testgata X</adresse2><adresse3>Testgata Y</adresse3><postnr>7970</postnr><poststed>Kolvereid</poststed><kommunenummer>1751</kommunenummer><kommune>Nærøy</kommune><landkode>NO</landkode><land>Norge</land></forretningsAdresse>"""
BB_EXPECTED_ADDRESS_TAG = """<forretningsAdresse infoType="FADR" register="ER" xmlns="http://schema.brreg.no/intef/integrasjonERFV"><adresse1>Testgata 5</adresse1><adresse2>Testgata X</adresse2><adresse3>Testgata Y</adresse3><postnr>7994</postnr><poststed>Kolvereid</poststed><kommunenummer>1755</kommunenummer><kommune>Leka</kommune><landkode>NO</landkode><land>Norge</land></forretningsAdresse>"""
AA_EXPECTED_IDENTICAL_ADDRESS_TAG = """<forretningsAdresse infoType="FADR" register="ER"><adresse1>Testgata 5</adresse1><adresse2>Testgata X</adresse2><adresse3>Testgata Y</adresse3><postnr>7970</postnr><poststed>Kolvereid</poststed><kommunenummer>1751</kommunenummer><kommune>Nærøy</kommune><landkode>NO</landkode><land>Norge</land></forretningsAdresse>"""

AA_EXPECTED_NAME_TAG = """<navn infoType="NAVN" register="ER" xmlns="http://schema.brreg.no/intef/integrasjonERFV"><navn1>Nærøy Jakt og Fisk</navn1></navn>"""
BB_EXPECTED_NAME_TAG = """<navn infoType="NAVN" register="ER" xmlns="http://schema.brreg.no/intef/integrasjonERFV"><navn1>Naroy Jakt og Fisk</navn1></navn>"""

BB_EXPECTED_WEB_TAG = """<hjemmeside infoType="IADR" register="ER" xmlns="http://schema.brreg.no/intef/integrasjonERFV"><url>www.eksempel.no</url></hjemmeside>"""
BB_EXPECTED_MOB_TAG = """<mobil infoType="MTLF" register="ER" xmlns="http://schema.brreg.no/intef/integrasjonERFV"><nummer>99999999</nummer></mobil>"""
BB_EXPECTED_EMAIL_TAG = """<epost infoType="EPOS" register="ER" xmlns="http://schema.brreg.no/intef/integrasjonERFV"><epostAdresse>post@eksempel.no</epostAdresse></epost>"""

BB_EXPECTED_FORMAAL_TAG = """<formaal infoType="FORM" register="ER"><formaalTekst>Idrettslag</formaalTekst></formaal>"""
BB_EXPECTED_KONTAKTPERSON_TAG = """<kontaktperson infoType="KONT" register="ER" xmlns="http://schema.brreg.no/intef/integrasjonERFV"><rolle rolletype="KONT"><person><fodselsnr>17033900562</fodselsnr><slektsnavn>Grimstad</slektsnavn></person></rolle></kontaktperson>"""

BB_EXPECTED_STYRE_TAG = """<styre infoType="STYR" register="ER" xmlns="http://schema.brreg.no/intef/integrasjonERFV"><rolle rolle="LEDE"><person><fodselsnr>17033900562</fodselsnr><slektsnavn>Grimstad</slektsnavn></person></rolle><rolle rolle="MEDL"><person><fodselsnr>17035600213</fodselsnr><slektsnavn>Augestad</slektsnavn></person></rolle></styre>"""
BB_EXPECTED_SIGNATUR_TAG = """<signatur infoType="SIGN" register="ER" xmlns="http://schema.brreg.no/intef/integrasjonERFV"><signaturTekst>To styremedlemmer i fellesskap.</signaturTekst><signaturTekst>Daglig leder alene.</signaturTekst></signatur>"""
BB_EXPECTED_PROKURA_TAG = """<prokura infoType="PROK" register="ER" xmlns="http://schema.brreg.no/intef/integrasjonERFV"><prokuraTekst>To styremedlemmer i fellesskap.</prokuraTekst><prokuraTekst>Daglig leder alene.</prokuraTekst></prokura>"""

AA_EXPECTED_OPPLYSNINGUTGAAT_TAG1 = """<opplysningUtgaar>FADR</opplysningUtgaar>"""
AA_EXPECTED_OPPLYSNINGUTGAAT_TAG2 = """<opplysningUtgaar>IADR</opplysningUtgaar>"""
AA_EXPECTED_OPPLYSNINGUTGAAT_TAG3 = """<opplysningUtgaar>EPOS</opplysningUtgaar>"""

AA_EXPECTED_FULL_EL_ADR_TAG = """<elektroniskVarslingsadresse><epostadresse>naroyfisk@eksempel.no</epostadresse><mobil><prefiks>47</prefiks><mobilnummer>44994499</mobilnummer></mobil></elektroniskVarslingsadresse>"""
AA_EXPECTED_MOBILE_EL_ADR_TAG = """<elektroniskVarslingsadresse><mobil><prefiks>47</prefiks><mobilnummer>44994499</mobilnummer></mobil></elektroniskVarslingsadresse>"""
AA_EXPECTED_EMAIL_EL_ADR_TAG = """<elektroniskVarslingsadresse><epostadresse>naroyfisk@eksempel.no</epostadresse></elektroniskVarslingsadresse>"""

SIGN_W_ROLES_EXP = """<signatur infoType="SIGN" register="ER" xmlns="http://schema.brreg.no/intef/integrasjonERFV"><signaturTekst>To styremedlemmer i fellesskap.</signaturTekst><signaturTekst>Daglig leder alene.</signaturTekst><rolle rolletype="SIGN"><person><fodselsnr>20044100127</fodselsnr><slektsnavn>Heldal</slektsnavn></person></rolle><rolle rolletype="SIHV"><person><fodselsnr>17033900562</fodselsnr><slektsnavn>Grimstad</slektsnavn></person></rolle><rolle rolletype="SIFE"><person><fodselsnr>17035600213</fodselsnr><slektsnavn>Augestad</slektsnavn></person></rolle></signatur>"""
PROK_W_ROLES_EXP = """<prokura infoType="PROK" register="ER" xmlns="http://schema.brreg.no/intef/integrasjonERFV"><prokuraTekst>To styremedlemmer i fellesskap.</prokuraTekst><prokuraTekst>Daglig leder alene.</prokuraTekst><rolle rolletype="PROK"><person><fodselsnr>20044100127</fodselsnr><slektsnavn>Heldal</slektsnavn></person></rolle><rolle rolletype="POHV"><person><fodselsnr>17033900562</fodselsnr><slektsnavn>Grimstad</slektsnavn></person></rolle><rolle rolletype="POFE"><person><fodselsnr>17035600213</fodselsnr><slektsnavn>Augestad</slektsnavn></person></rolle></prokura>"""


@pytest.mark.parametrize("_dict, expected_content", [
    (AA_DICT, BB_EXPECTED_HEADER_CONTENT),
    (AA_DICT, BB_EXPECTED_HEADER_TAG_CONTENT),
    ])
def test_make_header(_dict, expected_content):
  header = make_header(_dict['header'])
  xmlheader = header.toxml(element_name='header')
  stripped = strip_default_namespace(xmlheader)
  assert expected_content in stripped


@pytest.mark.parametrize("_dict, expected_content", [
    (AA_DICT, AA_EXPECTED_NAME_TAG),
    ])
def test_make_name_tag(_dict, expected_content):
  melding = make_melding(_dict)
  generatedxml = melding.navn.toxml(element_name='navn')
  stripped = strip_default_namespace(generatedxml)
  assert expected_content in stripped


@pytest.mark.parametrize("_dict, expected_content", [
    (AA_DICT, BB_EXPECTED_DATE_TAG),
    ])
def test_make_date_tag(_dict, expected_content):
  melding = make_melding(_dict)
  generatedxml = melding.stiftelsesdato.toxml(element_name='stiftelsesdato')
  stripped = strip_default_namespace(generatedxml)
  assert expected_content in stripped


@pytest.mark.parametrize("_dict, expected_content", [
    (AA_DICT, AA_EXPECTED_ADDRESS_TAG),
    ])
def test_make_address_tag(_dict, expected_content):
  melding = make_melding(_dict)
  generatedxml = melding.forretningsAdresse.toxml(element_name='forretningsAdresse')

  stripped = strip_default_namespace(generatedxml)
  assert expected_content in stripped


@pytest.mark.parametrize("_dict, expected_content", [
    (AA_DICT, BB_EXPECTED_WEB_TAG),
    ])
def test_make_website_tag(_dict, expected_content):
  melding = make_melding(_dict)
  generatedxml = melding.hjemmeside.toxml(element_name='hjemmeside')

  stripped = strip_default_namespace(generatedxml)
  assert expected_content in stripped


@pytest.mark.parametrize("_dict, expected_content", [
    (AA_DICT, BB_EXPECTED_EMAIL_TAG),
    ])
def test_make_email_tag(_dict, expected_content):
  melding = make_melding(_dict)
  generatedxml = melding.epost.toxml(element_name='epost')

  stripped = strip_default_namespace(generatedxml)
  assert expected_content in stripped


@pytest.mark.parametrize("_dict, expected_content", [
    (AA_DICT, BB_EXPECTED_MOB_TAG),
    ])
def test_make_mobile_tag(_dict, expected_content):
  melding = make_melding(_dict)
  generatedxml = melding.mobil.toxml(element_name='mobil')

  stripped = strip_default_namespace(generatedxml)
  assert expected_content in stripped


@pytest.mark.parametrize("_dict, expected_content", [
    (AA_DICT, BB_EXPECTED_KONTAKTPERSON_TAG),
    ])
def test_make_kontaktpers_tag(_dict, expected_content):
  melding = make_melding(_dict)
  generatedxml = melding.kontaktperson.toxml(element_name='kontaktperson')

  stripped = strip_default_namespace(generatedxml)
  assert expected_content in stripped


@pytest.mark.parametrize("_dict, expected_content", [
    (AA_DICT, BB_EXPECTED_STYRE_TAG),
    ])
def test_make_styre_tag(_dict, expected_content):
  melding = make_melding(_dict)
  generatedxml = melding.styre.toxml(element_name='styre')

  stripped = strip_default_namespace(generatedxml)
  assert expected_content in stripped


@pytest.mark.parametrize("_dict, expected_content", [
    (AA_DICT, AA_EXPECTED_OPPLYSNINGUTGAAT_TAG1),
    (AA_DICT, AA_EXPECTED_OPPLYSNINGUTGAAT_TAG2),
    (AA_DICT, AA_EXPECTED_OPPLYSNINGUTGAAT_TAG3),
    ])
def test_make_opplysningUtgaar_tag(_dict, expected_content):
  melding = make_melding(_dict)
  generatedxml = melding.toxml(element_name='melding')

  stripped = strip_default_namespace(generatedxml)
  assert expected_content in stripped


@pytest.mark.parametrize("_dict, expected_content", [
    (AA_DICT, AA_EXPECTED_FULL_EL_ADR_TAG),
    (ELADR_EMAIL_DICT, AA_EXPECTED_EMAIL_EL_ADR_TAG),
    (ELADR_MOBILE_DICT, AA_EXPECTED_MOBILE_EL_ADR_TAG),
    ])
def test_make_elektroniskAdresse_tag(_dict, expected_content):
  melding = make_melding(_dict)
  generatedxml = melding.toxml(element_name='melding')

  stripped = strip_default_namespace(generatedxml)
  assert expected_content in stripped


@pytest.mark.parametrize("_dict, expected_content", [
    (ELADR_WRONG_TYPE_DICT, AA_EXPECTED_FULL_EL_ADR_TAG),
    ])
def test_fail_make_elektroniskAdresse_tag(_dict, expected_content):
  melding = make_melding(_dict)
  generatedxml = melding.toxml(element_name='melding')

  stripped = strip_default_namespace(generatedxml)
  assert expected_content not in stripped


@pytest.mark.parametrize("_dict, expected_content", [
    (AA_DICT, BB_EXPECTED_SIGNATUR_TAG),
    (SIGN_PROK_ROLES, SIGN_W_ROLES_EXP)
    ])
def test_make_signatur_tag(_dict, expected_content):
  melding = make_melding(_dict)
  generatedxml = melding.signatur.toxml(element_name='signatur')
  stripped = strip_default_namespace(generatedxml)
  assert expected_content in stripped


@pytest.mark.parametrize("_dict, expected_content", [
    (AA_DICT, BB_EXPECTED_PROKURA_TAG),
    (SIGN_PROK_ROLES, PROK_W_ROLES_EXP)
    ])
def test_make_prokura_tag(_dict, expected_content):
  melding = make_melding(_dict)
  generatedxml = melding.prokura.toxml(element_name='prokura')
  stripped = strip_default_namespace(generatedxml)
  assert expected_content in stripped


@pytest.mark.parametrize("_dict, expected_content", [
    (IDENTICAL_ADDRESSES, AA_EXPECTED_IDENTICAL_ADDRESS_TAG),
    ])
def test_identical_addresses(_dict, expected_content):
  melding = make_melding(_dict)
  generatedxml = melding.toxml(element_name='melding')
  stripped = strip_default_namespace(generatedxml)
  assert expected_content in stripped
  assert 'PADR' not in stripped


def test_complete_message_generation():
  # Testing that XML can be successfully created from this dataset,
  # without throwing an error.
  melding = make_melding(full_nny_message)
  xml = melding.toxml(element_name='melding')


def test_xml_generation():
  # Testing that XML can be successfully created from this dataset,
  # without throwing an error.
  melding = make_melding(AA_DICT)
  complete_melding = ""

  generatedxml = melding.navn.toxml(element_name='navn')
  stripped = strip_default_namespace(generatedxml)
  complete_melding += stripped

  generatedxml = melding.stiftelsesdato.toxml(element_name='stiftelsesdato')
  stripped = strip_default_namespace(generatedxml)
  complete_melding += stripped

  generatedxml = melding.forretningsAdresse.toxml(element_name='forretningsAdresse')
  stripped = strip_default_namespace(generatedxml)
  complete_melding += stripped

  generatedxml = melding.hjemmeside.toxml(element_name='hjemmeside')
  stripped = strip_default_namespace(generatedxml)
  complete_melding += stripped

  generatedxml = melding.epost.toxml(element_name='epost')
  stripped = strip_default_namespace(generatedxml)
  complete_melding += stripped

  generatedxml = melding.telefon.toxml(element_name='telefon')
  stripped = strip_default_namespace(generatedxml)
  complete_melding += stripped

  generatedxml = melding.mobil.toxml(element_name='mobil')
  stripped = strip_default_namespace(generatedxml)
  complete_melding += stripped

  generatedxml = melding.telefaks.toxml(element_name='telefaks')
  stripped = strip_default_namespace(generatedxml)
  complete_melding += stripped

  generatedxml = melding.formaal.toxml(element_name='formaal')
  stripped = strip_default_namespace(generatedxml)
  complete_melding += stripped

  generatedxml = melding.kontaktperson.toxml(element_name='kontaktperson')
  stripped = strip_default_namespace(generatedxml)
  complete_melding += stripped

  generatedxml = melding.dagligLeder.toxml(element_name='dagligLeder')
  stripped = strip_default_namespace(generatedxml)
  complete_melding += stripped

  generatedxml = melding.styre.toxml(element_name='styre')
  stripped = strip_default_namespace(generatedxml)
  complete_melding += stripped

  generatedxml = melding.signatur.toxml(element_name='signatur')
  stripped = strip_default_namespace(generatedxml)
  complete_melding += stripped

  generatedxml = melding.maalform.toxml(element_name='maalform')
  stripped = strip_default_namespace(generatedxml)
  complete_melding += stripped

  generatedxml = melding.ansatte.toxml(element_name='ansatte')
  stripped = strip_default_namespace(generatedxml)
  complete_melding += stripped

  generatedxml = melding.grasrotandel.toxml(element_name='grasrotandel')
  stripped = strip_default_namespace(generatedxml)
  complete_melding += stripped

  c = 0
  for k in melding.kategori:
    k_xml = k.toxml(element_name='kategori')
    stripped = strip_default_namespace(k_xml)
    complete_melding += stripped
    c += 1

  generatedxml = melding.kontonummer.toxml(element_name='kontonummer')
  stripped = strip_default_namespace(generatedxml)
  complete_melding += stripped

  generatedxml = melding.meldepliktVedtekter.toxml(element_name='meldepliktVedtekter')
  stripped = strip_default_namespace(generatedxml)
  complete_melding += stripped

  generatedxml = melding.aarsregnskapLeveres.toxml(element_name='aarsregnskapLeveres')
  stripped = strip_default_namespace(generatedxml)
  complete_melding += stripped

  generatedxml = melding.regnskapsperiode.toxml(element_name='regnskapsperiode')
  stripped = strip_default_namespace(generatedxml)
  complete_melding += stripped

  c = 0
  for v in melding.vedlegg:
    v_xml = v.toxml(element_name='vedlegg')
    stripped = strip_default_namespace(v_xml)
    complete_melding += stripped
    c += 1

  c = 0
  for s in melding.signerer:
    s_xml = s.toxml(element_name='signerer')
    stripped = strip_default_namespace(s_xml)
    complete_melding += stripped
    c += 1


  xml = complete_melding.replace(' xmlns="http://schema.brreg.no/intef/integrasjonERFV"', '')
  xml = xml.replace('<?xml version="1.0" ?>', '')


def test_generate_melding_from_incomplete_dict():
  melding = make_melding(INCOMPLETE_DICT)


def test_generate_xml():
  xml = make_xml(AA_DICT)


# -----------------------------------
@pytest.mark.parametrize("_dict, expected_content", [
    (AA_DICT, XA_EXPECTED_ADDRESS_TAG),
    (AA_DICT, XA_EXPECTED_NAME_TAG),
    (AA_DICT, XB_EXPECTED_WEB_TAG),
    (AA_DICT, XB_EXPECTED_MOB_TAG),
    (AA_DICT, XB_EXPECTED_EMAIL_TAG),
    (AA_DICT, XB_EXPECTED_FORMAAL_TAG),
    (AA_DICT, XB_EXPECTED_KONTAKTPERSON_TAG),
    ])
def test_make_melding_tag(_dict, expected_content):
  melding = make_melding(_dict)
  generatedxml = melding.toxml(element_name='melding')

  stripped = strip_default_namespace(generatedxml)
  assert expected_content in stripped


def test_if_unable_to_add_wrong_val_in_onechar_field():
  crashed = False
  try:
    melding = make_melding(wrong_content_onechar_fields)
  except Exception, e:
    crashed = True
  assert crashed == True


def test_if_unable_to_add_wrong_val2_in_onechar_field():
  crashed = False
  try:
    melding = make_melding(wrong_numeric_content_onechar_fields)
  except Exception, e:
    crashed = True
  assert crashed == True


def test_if_unable_to_add_wrong_val3_in_onechar_field():
  crashed = False
  try:
    melding = make_melding(wrong_whitespace_content_onechar_fields)
  except Exception, e:
    crashed = True
  assert crashed == True


def test_if_unable_to_add_more_than_oneval_jn_field():
  crashed = False
  try:
    melding = make_melding(wrong_ammount_onechar_fields)
  except Exception, e:
    crashed = True
  assert crashed == True


def test_if_unable_to_set_N_in_changebylaws_field():
  melding = make_melding(wrong_changebylaws_field)
  xml = strip_default_namespace(melding.toxml(element_name='melding'))
  unwanted_N = "<endringMeldt>N</endringMeldt>"
  unwanted_J = "<endringMeldt>J</endringMeldt>"
  assert unwanted_N not in xml
  assert unwanted_J not in xml


def test_if_able_to_set_J_in_changebylaws_field():
  melding = make_melding(CORRECT_BYLAWS_DICT)
  xml = strip_default_namespace(melding.toxml(element_name='melding'))
  wanted = "<endringMeldt>J</endringMeldt>"
  unwanted_N = "<endringMeldt>N</endringMeldt>"
  assert wanted in xml
  assert unwanted_N not in xml


