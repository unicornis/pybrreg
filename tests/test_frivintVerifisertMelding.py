# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import unittest
import base64
import hashlib

import pyxb.utils.domutils as pyxb_util

from pybrreg.xml import frivintVerifisertMelding as fVM
from pybrreg.xml.generated import frivintVerifisertMelding

brreg_change_report = """<?xml version="1.0" encoding="UTF-8"?><integrasjonERFV xmlns="http://schema.brreg.no/intef/integrasjonERFV" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://schema.brreg.no/intef/integrasjonERFV integrasjonERFV.xsd">
    <header MeldingsDato="2015-10-13">
        <SLsysId>1001</SLsysId>
        <SLsysMeldingsId>a</SLsysMeldingsId>
        <sakstype>
            <hovedsakstype>N</hovedsakstype>
            <undersakstype>NY</undersakstype>
        </sakstype>
        <organisasjonsform>
            <orgform>FLI</orgform>
        </organisasjonsform>
        <status>
            <ERstatus>J</ERstatus>
            <FVstatus>J</FVstatus>
        </status>
    </header>
    <melding>
        <navn infoType="NAVN" register="ER">
            <navn1>Nærøy Jakt og Fisk</navn1>
        </navn>
        <stiftelsesdato infoType="STID" register="ER">1920-09-09</stiftelsesdato>
        <forretningsAdresse infoType="FADR" register="ER">
            <adresse1>Testgata 5</adresse1>
            <postnr>7970</postnr>
            <poststed>Kolvereid</poststed>
            <kommunenummer>1751</kommunenummer>
            <kommune>Nærøy</kommune>
            <landkode>NO</landkode>
            <land>Norge</land>
        </forretningsAdresse>
        <hjemmeside infoType="IADR" register="ER">
            <url>www.eksempel.no</url>
        </hjemmeside>
        <epost infoType="EPOS" register="ER">
            <epostAdresse>post@eksempel.no</epostAdresse>
        </epost>
        <mobil infoType="MTLF" register="ER">
            <nummer>99999999</nummer>
        </mobil>
        <formaal infoType="FORM" register="ER">
            <formaalTekst>Idrettslag</formaalTekst>
        </formaal>
        <kontaktperson infoType="KONT" register="ER">
            <rolle rolletype="KONT">
                <person>
                    <fodselsnr>17033900562</fodselsnr>
                    <slektsnavn>Grimstad</slektsnavn>
                </person>
            </rolle>
        </kontaktperson>
        <styre infoType="STYR" register="ER">
            <rolle rolle="LEDE">
                <person>
                    <fodselsnr>17033900562</fodselsnr>
                    <slektsnavn>Grimstad</slektsnavn>
                </person>
            </rolle>
            <rolle rolle="MEDL">
                <person>
                    <fodselsnr>17035600213</fodselsnr>
                    <slektsnavn>Augestad</slektsnavn>
                </person>
            </rolle>
        </styre>
        <signatur infoType="SIGN" register="ER">
            <signaturTekst>To styremedlemmer i fellesskap.</signaturTekst>
            <rolle rolletype="SIFE">
                <person>
                    <fodselsnr>17035600213</fodselsnr>
                    <slektsnavn>Augestad</slektsnavn>
                </person>
            </rolle>
            <rolle rolletype="SIFE">
                <person>
                    <fodselsnr>17033900562</fodselsnr>
                    <slektsnavn>Grimstad</slektsnavn>
                </person>
            </rolle>
        </signatur>
        <maalform infoType="MÅL" register="ER">
            <maalformKode>B</maalformKode>
        </maalform>
        <ansatte infoType="ARBG" register="ER">
            <harAnsatte>N</harAnsatte>
        </ansatte>
        <grasrotandel infotype="GRDT" register="FV">
            <skalDelta>J</skalDelta>
        </grasrotandel>
        <kategori infoType="KATG" register="FV">
            <kode>1200</kode>
            <rangering>1</rangering>
        </kategori>
        <kontonummer infoType="KTO" register="FV">
            <nummer>44670546397</nummer>
        </kontonummer>
        <meldepliktVedtekter infoType="MPVT" register="FV">
            <skalRegistreres>N</skalRegistreres>
        </meldepliktVedtekter>
        <aarsregnskapLeveres infoType="FVRR" register="FV">
            <skalLevere>J</skalLevere>
        </aarsregnskapLeveres>
        <regnskapsperiode infoType="FVRP" register="FV">
            <datoMaaned>3112</datoMaaned>
        </regnskapsperiode>
        <vedlegg>
            <vedleggsType>VEDT</vedleggsType>
        </vedlegg>
        <vedlegg>
            <vedleggsType>STIF</vedleggsType>
        </vedlegg>
        <vedlegg>
            <vedleggsType>PAAR</vedleggsType>
        </vedlegg>
        <vedlegg>
            <vedleggsType>SGDK</vedleggsType>
        </vedlegg>
        <signerer>17033900562</signerer>
    </melding>
</integrasjonERFV>"""  # NOQA

authentication = """<saml:Assertion ID="s2542af21668a8983a66bf6d63d1b178c1c1f7ccea" IssueInstant="2015-11-04T19:54:40Z" Version="2.0" xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">
    <saml:Issuer>idporten-ver2.difi.no-v2</saml:Issuer>
    <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
        <ds:SignedInfo>
            <ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
            <ds:SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"/>
            <ds:Reference URI="#s2542af21668a8983a66bf6d63d1b178c1c1f7ccea">
                <ds:Transforms>
                    <ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/>
                    <ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
                </ds:Transforms>
                <ds:DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/>
                <ds:DigestValue>sIkhA00zfS1FrLstbyi4Wtp5c5g=</ds:DigestValue>
            </ds:Reference>
        </ds:SignedInfo>
        <ds:SignatureValue>mHmT8YAW5JaD7Nygk0faiKpbZ7qBo8JJNg7KJ2A0XBfsUYpe71uLEGjkewzEwI+WYg5IzkD+Rm71 SmvmJQsqEyQlCjXCxvNiQZZDv11vzIShE9Ulna72I63TAUVit1uQPzJ5EG1TQy6LOAvdctTNFzea YPm5oI69y/oAuX3ANGFFGu+2YeqcH3jRDGaza1l+fE3AN4OOPmReTVtpaHuzoz6Ak4MCdWSFujOk CsNO67nX5ppuuHj0aL+XdfEz1Yrxjsw+HhTkO+LWorEOD14HegnSs8x2YTvloh+wotknmeblcPbo GzfTeNmpuG2z5IU9LFToqy+Lnrzq2C1SafFUkw==
</ds:SignatureValue>
        <ds:KeyInfo>
            <ds:X509Data>
                <ds:X509Certificate>MIIE9zCCA9+gAwIBAgIKMbZ4wGiF3IUUOzANBgkqhkiG9w0BAQUFADBLMQswCQYDVQQGEwJOTzEd MBsGA1UECgwUQnV5cGFzcyBBUy05ODMxNjMzMjcxHTAbBgNVBAMMFEJ1eXBhc3MgQ2xhc3MgMyBD QSAzMB4XDTEzMDMwNzE0MDAzOFoXDTE2MDMwNzE0MDAzNVowgYsxCzAJBgNVBAYTAk5PMSwwKgYD VQQKDCNESVJFS1RPUkFURVQgRk9SIEZPUlZBTFROSU5HIE9HIElLVDEMMAoGA1UECwwDVkVSMSww KgYDVQQDDCNESVJFS1RPUkFURVQgRk9SIEZPUlZBTFROSU5HIE9HIElLVDESMBAGA1UEBRMJOTkx ODI1ODI3MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtRTwCP3aPXB61np2eF+ebEZT Tz8ebMzSfpin8bbga65jubLOSN28JQHysCBZryghJkUHhs+xL8wP85DEpCT7DoIe+9Hyx84Ei2eH kpO5B4HaY8c1s6X2iABvEUC7TsHxvsf71ORuP77/CtR4U29BH4X0OUGu3yKJOUWSYfiHyIpwPkcd Ns1jSkrvy6HJeCY0ICmdqTv/PzhHXS2pnGOt7aMkMQuHxmlgFO/wUeRmP4Rff3AUOPrPwk7OMhCe B219l7TNcd9Tb5xKySeVWDuHYzfjCM+5V86ZBNaGe6eFHfiFUMmGkmxtzcUqIsmSCH1fwIVBTpfn E6MS4WMo6TfsKQIDAQABo4IBmjCCAZYwCQYDVR0TBAIwADAfBgNVHSMEGDAWgBTMw/gHt5xtek71 pysdBfmzRxyR0TAdBgNVHQ4EFgQUR3iI9AQJNcfdr1Pp2c25VNGVAkUwDgYDVR0PAQH/BAQDAgSw MBUGA1UdIAQOMAwwCgYIYIRCARoBAwIwgaUGA1UdHwSBnTCBmjAvoC2gK4YpaHR0cDovL2NybC5i dXlwYXNzLm5vL2NybC9CUENsYXNzM0NBMy5jcmwwZ6BloGOGYWxkYXA6Ly9sZGFwLmJ1eXBhc3Mu bm8vZGM9QnV5cGFzcyxkYz1OTyxDTj1CdXlwYXNzJTIwQ2xhc3MlMjAzJTIwQ0ElMjAzP2NlcnRp ZmljYXRlUmV2b2NhdGlvbkxpc3QwegYIKwYBBQUHAQEEbjBsMDMGCCsGAQUFBzABhidodHRwOi8v b2NzcC5idXlwYXNzLm5vL29jc3AvQlBDbGFzczNDQTMwNQYIKwYBBQUHMAKGKWh0dHA6Ly9jcnQu YnV5cGFzcy5uby9jcnQvQlBDbGFzczNDQTMuY2VyMA0GCSqGSIb3DQEBBQUAA4IBAQDZpzajceMe 9vwzY01BIafvcLX70WHxNUz2q5beYxW1+RDchr6wvznTChhpmuPuWp3Kuq9nD7kkZgIaiqUcjH1F uv2Jo0wEC8OtJAlUfIcyGh/o3s/u761Qq84viEV50cyXaUX9ryzdDgkxujgx1nFY0rnGWiHoM1jD SglTLfCOrd/ofF+Mr9gLVFl+AlZ3waIbhidlEC0fw05OTXPJ9sc3LJ+1QwV3DsZwjciL+ZIqS2Cg 4NXvNe1C8KpGUGoPN4gBWleB8WjyY1uTyz8ssE9+8ETMWnxCrxY6/rfm01iK0ZSFtqYl9Wdg1xyd kaTOrtGwi422Y0KOzixrsau1eMRh
</ds:X509Certificate>
            </ds:X509Data>
        </ds:KeyInfo>
    </ds:Signature>
    <saml:Subject>
        <saml:NameID Format="urn:oasis:names:tc:SAML:2.0:nameid-format:transient" NameQualifier="idporten-ver2.difi.no-v2" SPNameQualifier="difi.brreg.testsp.dev">VA3qSZnjmV4CdjkAgY9yo/b1x5nn</saml:NameID>
        <saml:SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
            <saml:SubjectConfirmationData InResponseTo="_8d4fb45737b6a3db02afef20a4ee8b3e" NotOnOrAfter="2015-11-04T20:04:40Z" Recipient="http://localhost/testsp/assertionconsumer"/>
        </saml:SubjectConfirmation>
    </saml:Subject>
    <saml:Conditions NotBefore="2015-11-04T19:44:40Z" NotOnOrAfter="2015-11-04T20:04:40Z">
        <saml:AudienceRestriction>
            <saml:Audience>difi.brreg.testsp.dev</saml:Audience>
        </saml:AudienceRestriction>
    </saml:Conditions>
    <saml:AuthnStatement AuthnInstant="2015-11-04T19:39:50Z" SessionIndex="s27f9ba43e7e43e87633a381aaf6e8a8e516a88901">
        <saml:AuthnContext>
            <saml:AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport
</saml:AuthnContextClassRef>
        </saml:AuthnContext>
    </saml:AuthnStatement>
    <saml:AttributeStatement>
        <saml:Attribute Name="uid">
            <saml:AttributeValue xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">15037100398</saml:AttributeValue>
        </saml:Attribute>
        <saml:Attribute Name="Culture">
            <saml:AttributeValue xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">nb</saml:AttributeValue>
        </saml:Attribute>
        <saml:Attribute Name="AuthMethod">
            <saml:AttributeValue xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">Minid-PIN</saml:AttributeValue>
        </saml:Attribute>
        <saml:Attribute Name="SecurityLevel">
            <saml:AttributeValue xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">3</saml:AttributeValue>
        </saml:Attribute>
    </saml:AttributeStatement>
</saml:Assertion>"""  # NOQA

malformed_xml = """<integrasjonERFV xmlns="http://schema.brreg.no/intef/integrasjonERFV" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://schema.brreg.no/intef/integrasjonERFV integrasjonERFV.xsd">
    <header MeldingsDato="2015-10-13">
        <SLsysId>1001</SLsysId>
        <SLsysMeldingsId>a</SLsysMeldingsId>
        <sakstype>
            <hovedsakstype>N</hovedsakstype>
            <undersakstype>NY</undersakstype>
        </sakstype>
        <organisasjonsform>
            <orgform>FLI</orgform>
        </organisasjonsform>
        <status>
            <ERstatus>J</ERstatus>
            <FVstatus>J</FVstatus>
        </status>
    <melding>
        <navn infoType="NAVN" register="ER">
            <navn1>Nærøy Jakt og Fisk</navn1>
        </navn>
        <stiftelsesdato infoType="STID" register="ER">1920-09-09</stiftelsesdato>
        <forretningsAdresse infoType="FADR" register="ER">
            <adresse1>Testgata 5</adresse1>
            <postnr>7970</postnr>
            <poststed>Kolvereid</poststed>
            <kommunenummer>1751</kommunenummer>
            <kommune>Nærøy</kommune>
            <landkode>NO</landkode>
            <land>Norge</land>
        </forretningsAdresse>
        <hjemmeside infoType="IADR" register="ER">
            <url>www.eksempel.no</url>
        </hjemmeside>
        <epost infoType="EPOS" register="ER">
            <epostAdresse>post@eksempel.no</epostAdresse>
        </epost>
        <mobil infoType="MTLF" register="ER">
            <nummer>99999999</nummer>
        </mobil>
        <formaal infoType="FORM" register="ER">
            <formaalTekst>Idrettslag</formaalTekst>
        </formaal>
        <kontaktperson infoType="KONT" register="ER">
            <rolle rolletype="KONT">
                <person>
                    <fodselsnr>17033900562</fodselsnr>
                    <slektsnavn>Grimstad</slektsnavn>
                </person>
            </rolle>
        </kontaktperson>
        <styre infoType="STYR" register="ER">
            <rolle rolle="LEDE">
                <person>
                    <fodselsnr>17033900562</fodselsnr>
                    <slektsnavn>Grimstad</slektsnavn>
                </person>
            </rolle>
            <rolle rolle="MEDL">
                <person>
                    <fodselsnr>17035600213</fodselsnr>
                    <slektsnavn>Augestad</slektsnavn>
                </person>
            </rolle>
        </styre>
        <signatur infoType="SIGN" register="ER">
            <signaturTekst>To styremedlemmer i fellesskap.</signaturTekst>
            <rolle rolletype="SIFE">
                <person>
                    <fodselsnr>17035600213</fodselsnr>
                    <slektsnavn>Augestad</slektsnavn>
                </person>
            </rolle>
            <rolle rolletype="SIFE">
                <person>
                    <fodselsnr>17033900562</fodselsnr>
                    <slektsnavn>Grimstad</slektsnavn>
                </person>
            </rolle>
        </signatur>
        <maalform infoType="MÅL" register="ER">
            <maalformKode>B</maalformKode>
        </maalform>
        <ansatte infoType="ARBG" register="ER">
            <harAnsatte>N</harAnsatte>
        </ansatte>
        <grasrotandel infotype="GRDT" register="FV">
            <skalDelta>J</skalDelta>
        </grasrotandel>
        <kategori infoType="KATG" register="FV">
            <kode>1200</kode>
            <rangering>1</rangering>
        </kategori>
        <kontonummer infoType="KTO" register="FV">
            <nummer>44670546397</nummer>
        </kontonummer>
        <meldepliktVedtekter infoType="MPVT" register="FV">
            <skalRegistreres>N</skalRegistreres>
        </meldepliktVedtekter>
        <aarsregnskapLeveres infoType="FVRR" register="FV">
            <skalLevere>J</skalLevere>
        </aarsregnskapLeveres>
        <regnskapsperiode infoType="FVRP" register="FV">
            <datoMaaned>3112</datoMaaned>
        </regnskapsperiode>
        <vedlegg>
            <vedleggsType>VEDT</vedleggsType>
        </vedlegg>
        <vedlegg>
            <vedleggsType>STIF</vedleggsType>
        </vedlegg>
        <vedlegg>
            <vedleggsType>PAAR</vedleggsType>
        </vedlegg>
        <vedlegg>
            <vedleggsType>SGDK</vedleggsType>
        </vedlegg>
        <signerer>17033900562</signerer>
    </melding>
</integrasjonERFV>"""  # NOQA


SECRET = "Secret"


class SignedObjectTests(unittest.TestCase):

    def setUp(self):
        self.expected = base64.b64encode(brreg_change_report.encode("utf-8"))

    @staticmethod
    def test_invalid_input():

        with pytest.raises(TypeError):
            fVM.create_signed_object(None)

        with pytest.raises(ValueError):
            fVM.create_signed_object(malformed_xml)

    def test_valid_result(self):

        result = fVM.create_signed_object(brreg_change_report)

        self.assertEqual(self.expected, result)


class SignedObjectHashTests(unittest.TestCase):

    def setUp(self):
        hashed = hashlib.sha256(base64.b64encode(brreg_change_report.encode("utf-8")))

        encoded = base64.b64encode(hashed.digest())

        signed_object_hash = frivintVerifisertMelding.SignedObjectHash(encoded, algorithm="SHA-256")

        self.expected = signed_object_hash.toxml(element_name="SignedObjectHash")

    @staticmethod
    def test_invalid_input():

        with pytest.raises(TypeError):
            fVM.create_signed_object_hash(None)

        with pytest.raises(ValueError):
            fVM.create_signed_object_hash(malformed_xml)

    def test_valid_result(self):

        signed_object_hash = fVM.create_signed_object_hash(brreg_change_report)

        result = signed_object_hash.toxml(element_name="SignedObjectHash")

        self.assertEqual(self.expected, result)


class RecordSealTests(unittest.TestCase):

    def setUp(self):
        self.secret = "Secret"

        self.signed_object_hash = fVM.create_signed_object_hash(brreg_change_report)

        hashed = hashlib.sha512()
        hashed.update(self.signed_object_hash.value())
        hashed.update(base64.b64encode(authentication))
        hashed.update(self.secret)

        encoded = base64.b64encode(hashed.digest())

        record_seal = frivintVerifisertMelding.RecordSeal(encoded, algorithm="SHA-512")

        self.expected = record_seal.toxml(element_name="RecordSeal")

    def test_invalid_input(self):

        with pytest.raises(TypeError):
            fVM.create_record_seal(None, self.signed_object_hash, self.secret)

        with pytest.raises(TypeError):
            fVM.create_record_seal(authentication, "Somestring", self.secret)

        with pytest.raises(TypeError):
            fVM.create_record_seal(authentication, self.signed_object_hash, None)

        with pytest.raises(ValueError):
            fVM.create_record_seal(malformed_xml, self.signed_object_hash, self.secret)

    def test_valid_result(self):

        record_seal = fVM.create_record_seal(authentication, self.signed_object_hash, self.secret)

        result = record_seal.toxml(element_name="RecordSeal")

        self.assertEqual(self.expected, result)


class SignatureRecordTests(unittest.TestCase):

    def setUp(self):
        self.secret = "Secret"
        encoded_auth = base64.b64encode(authentication)
        signed_object_hash = fVM.create_signed_object_hash(brreg_change_report)

        signature = frivintVerifisertMelding.SignatureRecord()
        signature.SignedObjectHash = signed_object_hash
        signature.Authentication = encoded_auth
        signature.RecordSeal = fVM.create_record_seal(authentication, signed_object_hash,
                                                      self.secret)

        self.expected = signature.toxml(element_name="SignatureRecord")

    def test_invalid_input(self):

        with pytest.raises(TypeError):
            fVM.create_signature_record(None, authentication, self.secret)

        with pytest.raises(TypeError):
            fVM.create_signature_record(brreg_change_report, None, self.secret)

        with pytest.raises(TypeError):
            fVM.create_signature_record(brreg_change_report, authentication, None)

        with pytest.raises(ValueError):
            fVM.create_signature_record(malformed_xml, authentication, self.secret)

        with pytest.raises(ValueError):
            fVM.create_signature_record(brreg_change_report, malformed_xml, self.secret)

        with pytest.raises(TypeError):
            fVM.create_signature_record_list(brreg_change_report, authentication, self.secret)

        with pytest.raises(TypeError):
            fVM.create_signature_record_list(brreg_change_report, None, self.secret)

    def test_valid_result(self):

        signature_record = fVM.create_signature_record(brreg_change_report, authentication,
                                                       self.secret)

        result = signature_record.toxml(element_name="SignatureRecord")

        self.assertEqual(self.expected, result)

    def test_multiple_signatures(self):

        auth_list = [authentication, authentication]

        signature_records = fVM.create_signature_record_list(brreg_change_report, auth_list,
                                                             self.secret)

        for signature in signature_records:
            result = signature.toxml(element_name="SignatureRecord")

            self.assertEqual(self.expected, result)
