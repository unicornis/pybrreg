# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
import pyxb
import pyxb.utils.domutils
from xml.sax.saxutils import escape

from . import integrasjonPYXB

# The prefix is used to avoid name space conflicts
NAMESPACEPREFIX = "aNameSpacePrefixThatWillBeRemoved"

EXPIREABLE_FIELDCODES = {
    "postAdresse": "PADR",
    "forretningsAdresse": "FADR",
    "hjemmeside": "IADR",
    "epost": "EPOS",
    "telefon": "TFON",
    "telefaks": "TFAX",
    "mobil": "MTLF",
    "kontaktperson": "KONT",
    "dagligLeder": "DAGL",
    "forretningsforer": "FFØR",
    "styre": "STYR",
    "signatur": "SIGN",
    "prokura": "PROK",
    "kontonummer": "KTO",  }

def make_xml(_dict):
    # Build object from dict using PYXB
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(integrasjonPYXB.Namespace, NAMESPACEPREFIX)
    pyxb_object = integrasjonPYXB.integrasjonERFV()
    pyxb_object.header = make_header(_dict['header'])
    pyxb_object.melding = make_melding(_dict)

    # Generate xml and remove default namespace to make BRREGs
    # XML-parsers happy.
    xml = pyxb_object.toxml(element_name='integrasjonERFV')
    return strip_default_namespace(xml)


def cdata_helper(string):
    return "<![CDATA[%s]]>" % string


def make_header(_dict):
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(integrasjonPYXB.Namespace, NAMESPACEPREFIX)
    h = integrasjonPYXB.header()
    try:
        h.MeldingsDato = datetime.now().date()
        h.SLsysId = _dict['SLsysId']
        h.SLsysMeldingsId = _dict['SLsysMeldingsId']

        dict_sakstype = _dict['sakstype']
        if dict_sakstype['undersakstype'] == 'NY' and dict_sakstype['hovedsakstype'] == 'E':
            undersakstype = 'NYFV'
        else:
            undersakstype = dict_sakstype['undersakstype']
        h.sakstype = integrasjonPYXB.sakstype(
            hovedsakstype=dict_sakstype['hovedsakstype'],
            undersakstype=undersakstype)

        h.organisasjonsform = integrasjonPYXB.organisasjonsform(
                        orgform='FLI')

        if 'organisasjonsnummer' in _dict and _dict['organisasjonsnummer']:
            h.organisasjonsnummer = _dict['organisasjonsnummer']

        dict_status = _dict['status']
        h.status = integrasjonPYXB.CTD_ANON_(
            ERstatus=dict_status['ERstatus'],
            FVstatus=dict_status['FVstatus'])
    except Exception:
        raise
    return h


def make_melding(_dict):
    m = integrasjonPYXB.melding()
    er_dict = _dict['er']
    fv_dict = _dict['fv']

    sakstype = None
    if 'header' in _dict:
        sakstype = _dict['header']['sakstype']

        #  'elektroniskVarslingsadresse' is only included in new registrations, and not
        #  added to Enhetsregisteret or Frivillighetsregisteret.
        if sakstype['hovedsakstype'] == 'N' and sakstype['undersakstype'] == 'NY':
            if 'elektroniskVarslingsadresse' in _dict:
                el_dict = _dict['elektroniskVarslingsadresse']
                m.elektroniskVarslingsadresse = make_electronic_address(el_dict)
            else:
                raise ValueError('Electronic alert address(e-mail or mobile) is required for registering new organisations.')

    if 'navn' in er_dict:
        _navn = er_dict['navn']
        navn = integrasjonPYXB.navn(
            infoType="NAVN",
            register="ER"
            )
        if 'navn1' in _navn:
            navn.navn1 = escape(_navn['navn1'])
        if 'navn2' in _navn:
            navn.navn2 = escape(_navn['navn2'])
        if 'navn3' in _navn:
            navn.navn3 = escape(_navn['navn3'])
        if 'navn4' in _navn:
            navn.navn4 = escape(_navn['navn4'])
        if 'navn5' in _navn:
            navn.navn5 = escape(_navn['navn5'])
        m.navn = navn

    if 'stiftelsesdato'in er_dict:
        m.stiftelsesdato = integrasjonPYXB.stiftelsesdato(
                er_dict['stiftelsesdato'],
                infoType="STID",
                register="ER"
            )

    # If the addresses are identical, only FADR should be included,
    # and PADR should be removed if allready stored in brreg
    addresses_equal = False
    p_adr_in_brreg = False
    if 'padr_registrert' in _dict:
        p_adr_in_brreg = _dict['padr_registrert']
    if 'forretningsAdresse' in er_dict and 'postAdresse' in er_dict:
        b_adr = er_dict['forretningsAdresse']
        p_adr = er_dict['postAdresse']
        addresses_equal = compare_addresses(b_adr, p_adr)
    # Remove PADR if identical addresses, and some address registered in BRREG
    if addresses_equal and p_adr_in_brreg:
        m.opplysningUtgaar.append(EXPIREABLE_FIELDCODES['postAdresse'])

    if 'forretningsAdresse' in er_dict:
        b_adr = er_dict['forretningsAdresse']
        if b_adr['land'] == 'Norway':
            land = 'Norge'
        else:
            land = b_adr['land']
        adr = integrasjonPYXB.forretningsAdresse(
            infoType = "FADR",
            register = "ER",
            postnr = b_adr['postnr'],
            poststed = b_adr['poststed'],
            kommunenummer = b_adr['kommunenummer'],
            kommune = b_adr['kommune'],
            landkode = b_adr['landkode'],
            land = land,
            )
        if 'adresse1' in b_adr and b_adr['adresse1']:
            adr.adresse1 = b_adr['adresse1']
        if 'adresse2' in b_adr and b_adr['adresse2']:
            adr.adresse2 = b_adr['adresse2']
        if 'adresse3' in b_adr and b_adr['adresse3']:
            adr.adresse3 = b_adr['adresse3']
        m.forretningsAdresse = adr

    if 'postAdresse' in er_dict and not addresses_equal:
        p_adr = er_dict['postAdresse']
        if p_adr['land'] == 'Norway':
            land = 'Norge'
        else:
            land = p_adr['land']
        adr = integrasjonPYXB.postAdresse(
            infoType = "PADR",
            register = "ER",
            postnr = p_adr['postnr'],
            poststed = p_adr['poststed'],
            kommunenummer = p_adr['kommunenummer'],
            kommune = p_adr['kommune'],
            landkode = p_adr['landkode'],
            land = land,
            )
        if 'adresse1' in p_adr and p_adr['adresse1']:
            adr.adresse1 = p_adr['adresse1']
        if 'adresse2' in p_adr and p_adr['adresse2']:
            adr.adresse2 = p_adr['adresse2']
        if 'adresse3' in p_adr and p_adr['adresse3']:
            adr.adresse3 = p_adr['adresse3']
        m.postAdresse = adr


    if 'hjemmeside' in er_dict:
        u = er_dict['hjemmeside']
        url = u.replace('http://', '')
        url = url.replace('https://', '')
        m.hjemmeside = integrasjonPYXB.hjemmeside(
            url=url,
            infoType="IADR",
            register="ER"
            )

    if 'epost' in er_dict:
        m.epost = integrasjonPYXB.epost(
            infoType="EPOS",
            register="ER",
            epostAdresse=er_dict['epost']
            )

    if 'mobil' in er_dict:
        m.mobil = integrasjonPYXB.mobil(
            infoType="MTLF",
            register="ER",
            nummer=er_dict['mobil']
            )

    if 'telefon' in er_dict:
        m.telefon = integrasjonPYXB.telefon(
            infoType="TFON",
            register="ER",
            nummer=er_dict['telefon']
            )


    if 'telefaks' in er_dict:
        m.telefaks = integrasjonPYXB.telefaks(
            infoType="TFAX",
            register="ER",
            nummer=er_dict['telefaks']
            )

    if 'formaal' in er_dict:
        m.formaal = integrasjonPYXB.formaal(
            infoType="FORM",
            register="ER",
            formaalTekst=er_dict['formaal']
            )

    if 'kontaktperson' in er_dict:
        m.kontaktperson = make_kontaktperson(er_dict['kontaktperson'])

    if 'dagligLeder' in er_dict:
        m.dagligLeder = make_dagligLeder(er_dict['dagligLeder'])

    if 'forretningsforer' in er_dict:
        m.forretningsforer = make_forretningsforer(er_dict['forretningsforer'])

    if 'styre' in er_dict:
        m.styre = make_styre(er_dict['styre'])

    if 'signatur' in er_dict:
        m.signatur = make_signatur(er_dict['signatur'])

    if 'prokura' in er_dict:
        m.prokura = make_prokura(er_dict['prokura'])

    if 'maalform' in er_dict:
        m.maalform = integrasjonPYXB.maalform(
            infoType="MÅL",
            register="ER",
            maalformKode=er_dict['maalform']
            )

    if 'ansatte' in er_dict:
        m.ansatte = integrasjonPYXB.ansatte(
            infoType="ARBG",
            register="ER",
            harAnsatte=er_dict['ansatte'])

    if 'nedleggelsesdato'in er_dict:
        m.nedleggelsesdato = integrasjonPYXB.nedleggelsesdato(
                er_dict['nedleggelsesdato'],
                infoType="NDAT",
                register="ER"
            )

    if 'grasrotandel' in fv_dict:
        m.grasrotandel = integrasjonPYXB.grasrotandel(
            infotype="GRDT",
            register="FV",
            skalDelta=fv_dict['grasrotandel']
            )

    if 'kategori' in fv_dict:
        for kat in fv_dict['kategori']:
            k = integrasjonPYXB.kategori(
                    infoType="KATG",
                    register="FV",
                    kode=kat['kode'],
                    rangering=kat['rangering'])
            m.kategori.append(k)

    if 'kontonummer' in fv_dict:
        m.kontonummer = integrasjonPYXB.kontonummer(
            infoType="KTO",
            register="FV",
            nummer=fv_dict['kontonummer']
            )

    if 'meldepliktVedtekter' in fv_dict:
        m.meldepliktVedtekter = integrasjonPYXB.meldepliktVedtekter(
            infoType="MPVT",
            register="FV",
            skalRegistreres=fv_dict['meldepliktVedtekter']
        )

    if 'endringAvVedtekter' in fv_dict and fv_dict['endringAvVedtekter'] == 'J':
        # Only add value if value === 'J'
        # Brreg only allowes 'J' on this particular field, not 'N'
        # This is a fix to make it possible to simplify the GUIfor the user 
        # by making it possible to offer both alternatives
        m.endringAvVedtekter = integrasjonPYXB.endringAvVedtekter(
            infoType="EVDT",
            register="FV",
            endringMeldt=fv_dict['endringAvVedtekter']
            )

    if 'aarsregnskapLeveres' in fv_dict:
        m.aarsregnskapLeveres = integrasjonPYXB.aarsregnskapLeveres(
            infoType="FVRR",
            register="FV",
            skalLevere=fv_dict['aarsregnskapLeveres']
            )

    if 'regnskapsperiode' in fv_dict:
        m.regnskapsperiode = integrasjonPYXB.regnskapsperiode(
            infoType="FVRP",
            register="FV",
            datoMaaned=fv_dict['regnskapsperiode']
            )

    if 'opplysningUtgaar' in _dict:
        expire = []
        for k in _dict['opplysningUtgaar']:
            field_exp_status = _dict['opplysningUtgaar'][k]
            if field_exp_status:
                m.opplysningUtgaar.append(EXPIREABLE_FIELDCODES[k])

    if 'vedlegg' in _dict:
        for vedl in _dict['vedlegg']:
            v = integrasjonPYXB.vedlegg(vedleggsType=vedl)
            m.vedlegg.append(v)

    # The person(s) signing the report
    if 'signerer' in _dict:
        for sign in _dict['signerer']:
            m.signerer.append(sign)
    return m


def compare_addresses(b_adr, p_adr):
    if b_adr['postnr'] != p_adr['postnr']:
        return False
    if b_adr['poststed'] != p_adr['poststed']:
        return False
    if b_adr['kommunenummer'] != p_adr['kommunenummer']:
        return False
    if b_adr['kommune'] != p_adr['kommune']:
        return False
    if b_adr['landkode'] != p_adr['landkode']:
        return False

    if 'adresse1' in b_adr and 'adresse1' in p_adr:
        if b_adr['adresse1'] != p_adr['adresse1']:
            return False
    elif 'adresse1' in b_adr or 'adresse1' in p_adr:
        return False

    if 'adresse2' in b_adr and 'adresse2' in p_adr:
        if b_adr['adresse2'] != p_adr['adresse2']:
            return False
    elif 'adresse2' in b_adr or 'adresse2' in p_adr:
        return False

    if 'adresse3' in b_adr and 'adresse3' in p_adr:
        if b_adr['adresse3'] != p_adr['adresse3']:
            return False
    elif 'adresse3' in b_adr or 'adresse3' in p_adr:
        return False

    return True


def make_signatur(s_dict):
    s = integrasjonPYXB.signatur(
        infoType="SIGN",
        register="ER")
    if 'signaturTekst' in s_dict:
        for sTxt in s_dict['signaturTekst']:
            s.signaturTekst.append(sTxt)
    if 'rolle' in s_dict:
        for r in s_dict['rolle']:
            rolle = make_rolle(r['rolle'], r['person'], integrasjonPYXB.CTD_ANON_41)
            s.rolle.append(rolle)
    return s


def make_prokura(p_dict):
    pr = integrasjonPYXB.prokura(
        infoType="PROK",
        register="ER")
    if 'prokuraTekst' in p_dict:
        for pTxt in p_dict['prokuraTekst']:
            pr.prokuraTekst.append(pTxt)
    if 'rolle' in p_dict:
        for r in p_dict['rolle']:
            rolle = make_rolle(r['rolle'], r['person'], integrasjonPYXB.CTD_ANON_37)
            pr.rolle.append(rolle)
    return pr


def make_styre(s_dict):
    s = integrasjonPYXB.styre(
        infoType="STYR",
        register="ER")
    for r in s_dict['rolle']:
        rolle = make_styrerolle(r['rolle'], r['person'], integrasjonPYXB.CTD_ANON_20)
        s.rolle.append(rolle)
    return s


def make_styrerolle(rolle_, person_, pyxb_def):
    rolle = pyxb_def(rolle=rolle_)
    person = make_person(person_['fodselsnr'], person_['slektsnavn'])
    rolle.append(person)
    return rolle


def make_rolle(rolle_, person_, pyxb_def):
    rolle = pyxb_def(rolletype=rolle_)
    person = make_person(person_['fodselsnr'], person_['slektsnavn'])
    rolle.append(person)
    return rolle


def make_person(fodselsnr, slektsnavn):
    return integrasjonPYXB.person(
        fodselsnr=fodselsnr,
        slektsnavn=slektsnavn)


def make_kontaktperson(k_dict):
    # To avoid SimplePluralValueError:
    rolletype = 'KONT'
    person = k_dict['person']

    kp = integrasjonPYXB.kontaktperson(
        infoType="KONT",
        register="ER")
    rolle = make_rolle(rolletype, person, integrasjonPYXB.CTD_ANON_4)
    kp.rolle.append(rolle)
    return kp


def make_dagligLeder(dgl_dict):
    rolletype = 'DAGL'
    person = dgl_dict['person']

    dgl = integrasjonPYXB.dagligLeder(
        infoType="DAGL",
        register="ER")

    rolle = make_rolle(rolletype, person, integrasjonPYXB.CTD_ANON_5)
    dgl.rolle.append(rolle)
    return dgl

def make_forretningsforer(ffor_dict):
    rolletype = 'FFØR'
    ffor = integrasjonPYXB.forretningsforer(
        infoType="FFØR",
        register="ER")
    if 'person' in ffor_dict:
        person = ffor_dict['person']
        rolle = make_rolle(rolletype, person, integrasjonPYXB.CTD_ANON_6)
    elif 'enhet' in ffor_dict:
        enhet_ = ffor_dict['enhet']
        rolle = integrasjonPYXB.CTD_ANON_6(rolletype=rolletype)
        enhet = integrasjonPYXB.enhet(orgnr=enhet_['orgnr'])
        rolle.append(enhet)
    ffor.rolle.append(rolle)
    return ffor


def make_electronic_address(el_dict):
    """
    A minimum of one of the elements must be included (email or mobile number)
    """
    electronic_adr = integrasjonPYXB.elektroniskVarslingsadresse()
    if not 'mobil' in el_dict and not 'epostadresse' in el_dict:
        raise ValueError('Mobile or email is required for electronic alerts.')
    if 'epostadresse' in el_dict:
        electronic_adr.epostadresse = el_dict['epostadresse']
    if 'mobil' in el_dict:
        prefiks = el_dict['mobil']['prefiks']
        nr = el_dict['mobil']['mobilnummer']
        electronic_adr.mobil = integrasjonPYXB.CTD_ANON_18(prefiks=prefiks, mobilnummer=nr)
    return electronic_adr


def strip_default_namespace(xmlstring):
    """
    Example of pyxb-generated xml:
    .....
    <ns1:header MeldingsDato="2015-10-13"
        xmlns:ns1="http://schema.brreg.no/intef/integrasjonERFV">
        <ns1:SLsysId>1001</ns1:SLsysId>
        <ns1:SLsysMeldingsId>a</ns1:SLsysMeldingsId>
        ......

    </ns1:header>

    Remove 'ns1'
    """
    r1 = '%s:' %NAMESPACEPREFIX
    r2 = ':%s' %NAMESPACEPREFIX
    stripped = xmlstring.replace(r1, '')
    stripped = stripped.replace(r2, '')
    return stripped
