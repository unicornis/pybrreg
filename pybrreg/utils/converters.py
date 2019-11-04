# -*- coding: utf-8 -*-
import json

def convert_signature_procuration(data):
    if data:
        settings = {}
        if 'signatur' in data:
            signatur = data['signatur']
            signData = signatur['samendring']
            assert signData["@samendringstype"] == "SIGN"
            signatureSettings = extract_settings(signData)
            settings['signature'] = signatureSettings
        if 'prokura' in data:
            proc = data['prokura']
            procData = proc['samendring']
            assert procData["@samendringstype"] == "PROK"
            procSettings = extract_settings(procData)
            settings['procuration'] = procSettings
        return settings
    return data


def format_person(person):
    return {'name': "%s %s" % (person['fornavn'], person['slektsnavn']),
            'birth_date': person['fodselsdato']}


def extract_settings(data):
    """
    'prokura' and 'signatur' has the same structure from BRREG.

    Text based rules can be found in 'headerTekst' and 'trailerTekst'.
    They can be a mixture of standard texts and custom texts.
    Rules may also be applied to certain specific people, and these
    are fount in 'rolle'
    """
    settings = {}

    standardTexts = ['Styret i fellesskap.',
        'Styrets medlemmer hver for seg.',
        'To styremedlemmer i fellesskap.',
        'Styrets leder alene.',
        'Styrets leder og nestleder hver for seg.',
        'Styrets leder og ett styremedlem i fellesskap.',
        'Daglig leder alene.',
        'Daglig leder og styrets leder i fellesskap.']

    def makeArrayOfTexts(text):
        x = '.'
        array = [s.strip() for s in text.split(x) if s != ""]
        if len(array) > 1:
            txt = [s+x for s in array if s != ""]
        else:
            txt = [text]
        return txt

    texts = []
    if 'headerTekst' in data and data['headerTekst']:
        h_texts = makeArrayOfTexts(data['headerTekst'])
        for t in h_texts:
            texts.append(t)

    if 'trailerTekst' in data and data['trailerTekst']:
        t_texts = makeArrayOfTexts(data['trailerTekst'])
        for t in t_texts:
            texts.append(t)

    if len(texts) > 0:
        settings['text'] = []
        settings['custom_text'] = []

        for txt in texts:
            if txt in standardTexts:
                settings['text'].append(txt)
            else:
                settings['custom_text'].append(txt)

    if 'rolle' in data and data['rolle']:
        roles_ = data['rolle']
        roles = []
        roles_list = []
        if isinstance(roles_, list):
            roles = roles_
        else:
            roles.append(roles_)
        for r in roles:
            role = {}
            role['roletype'] = r['@rolletype']
            role['description'] = r['@beskrivelse']
            role['person'] = []
            if isinstance(r['person'], list):
                for p in r['person']:
                    role['person'].append(format_person(p))
            else:
                role['person'].append(format_person(r['person']))
            roles_list.append(role)
        settings['roles'] = roles_list
    return settings
