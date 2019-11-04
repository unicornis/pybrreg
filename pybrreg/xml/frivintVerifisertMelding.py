# -*- coding: utf-8 -*-

import hashlib
import base64
from xml.etree import ElementTree

import pyxb.utils.domutils as pyxb_util

from generated import frivintVerifisertMelding as fVM


SOH_ALGORITHM = "SHA-256"
RECORD_SEAL_ALGORITHM = "SHA-512"


def create_signed_object_hash(brreg_change_report):
    """
    Create a signed object hash. Algorithm is set from specification, although this could be
    changed at a later time.

    Example:
    ::
    <SignedObjectHash algorithm="SHA-256">SV1FPI3Ln...Dbb2ZFaenVeEqI1VWuA=</SignedObjectHash>

    :param brreg_change_report: A complete XML of a change report, approved in precontrol (string)
    :return: SignedObjectHash - Compiled XML element
    """

    if not isinstance(brreg_change_report, basestring):
        raise TypeError("Brreg change report must be a string")

    if isinstance(brreg_change_report, unicode):
        brreg_change_report = brreg_change_report.encode("utf-8")

    try:
        ElementTree.fromstring(brreg_change_report)
    except ElementTree.ParseError as error:
        raise ValueError("The provided XML is not valid: {err}".format(err=error.message))

    hashed = hashlib.sha256(base64.b64encode(brreg_change_report))

    encoded = base64.b64encode(hashed.digest())

    signed_object_hash = fVM.SignedObjectHash(encoded, algorithm=SOH_ALGORITHM)

    return signed_object_hash


def create_record_seal(authentication, signed_object_hash, secret):
    """
    Produce a record seal XML for this SDO.

    Example:
    ::
        <RecordSeal algorithm="SHA-512">
            yPY+0QKeixOouaqylKvgyd6lA5rb3DdKHeXCWAPHKAN2BK5KYCs9nX0+1ldzckrkAumLweDeA5141F2zIWMgPw==
        </RecordSeal>

    :param authentication: Signed SAML assertion in XML (string)
    :param signed_object_hash: SignedObjectHash
    :param secret: Pre-shared secret, this must be requested from Brønnøysundregisteret (string)
    :return: RecordSeal - Compiled XML element
    """

    if not isinstance(authentication, basestring):
        raise TypeError("Authentication must be a string")
    if not isinstance(signed_object_hash, fVM.SignedObjectHash):
        raise TypeError("Expected: {exp}, got {actual}".format(exp=fVM.SignedObjectHash,
                                                               actual=type(signed_object_hash)))
    if not isinstance(secret, basestring):
        raise TypeError("Secret must be a string")

    try:
        ElementTree.fromstring(authentication)
    except ElementTree.ParseError as error:
        raise ValueError("The provided XML is not valid: {err}".format(err=error.message))

    hashed = hashlib.sha512()
    hashed.update(signed_object_hash.value())
    hashed.update(base64.b64encode(authentication))
    hashed.update(secret)

    encoded = base64.b64encode(hashed.digest())

    record_seal = fVM.RecordSeal(encoded, algorithm=RECORD_SEAL_ALGORITHM)

    return record_seal


def create_signed_object(brreg_change_report):
    """
    Create a base64-encoded value of a change report. This is the value to be used in
    SDO.SignedObject


    :param brreg_change_report: A complete XML of a change report, approved in precontrol (string)
    :return: base64-encoded string of brreg_change_report
    """

    if not isinstance(brreg_change_report, basestring):
        raise TypeError("Brreg change report must be a string")

    if isinstance(brreg_change_report, unicode):
        brreg_change_report = brreg_change_report.encode("utf-8")

    try:
        ElementTree.fromstring(brreg_change_report)
    except ElementTree.ParseError as error:
        raise ValueError("The provided XML is not valid: {err}".format(err=error.message))

    encoded = base64.b64encode(brreg_change_report)

    return encoded


def create_signature_record(brreg_change_report, authentication, secret):
    """
    Produce a signature record for an SDO. There will be one or more of these.

    Example:
    ::
        <SignatureRecord>
            <SignedObjectHash algorithm="SHA-256">SV1FPI3Lneva....bb2ZFaenVeEqI1VWuA=</SignedObjectHash>
            <Authentication>
                PD94bWwgdmVyc2lvbj0iMS....c3NlcnRpb24+
            </Authentication>
            <RecordSeal algorithm="SHA-512">
                rQ76lgrbrklfAaQXhGG2mNrjFk...EfYUIMtL4/2VZUGtmhw==
            </RecordSeal>
        </SignatureRecord>

    :param brreg_change_report: A complete XML of a change report, approved in precontrol (string)
    :param authentication: Signed SAML assertion in XML (string)
    :param secret: Pre-shared secret, this must be requested from Brønnøysundregisteret (string)
    :return: SignatureRecord
    """

    if not isinstance(brreg_change_report, basestring):
        raise TypeError("Brreg change report must be a string")
    if not isinstance(authentication, basestring):
        raise TypeError("Authentication must be a string")
    if not isinstance(secret, basestring):
        raise TypeError("Secret must be a string")

    if isinstance(brreg_change_report, unicode):
        brreg_change_report = brreg_change_report.encode("utf-8")

    try:
        ElementTree.fromstring(brreg_change_report)
    except ElementTree.ParseError as error:
        raise ValueError("The provided XML is not valid: {err}".format(err=error.message))
    try:
        ElementTree.fromstring(authentication)
    except ElementTree.ParseError as error:
        raise ValueError("The provided XML is not valid: {err}".format(err=error.message))

    signed_object_hash = create_signed_object_hash(brreg_change_report)

    signature = fVM.SignatureRecord()
    signature.SignedObjectHash = signed_object_hash
    signature.Authentication = base64.b64encode(authentication)
    signature.RecordSeal = create_record_seal(authentication, signed_object_hash, secret)

    return signature


def create_signature_record_list(brreg_change_report, authentications, secret):
    """
    Create a list of SignatureRecord objects. This makes it easier to work with SDOs that contain
    several signatures.

    :param brreg_change_report: A complete XML of a change report, approved in precontrol (string)
    :param authentications: list containing signed SAML assertions (string)
    :param secret: Pre-shared secret, this must be requested from Brønnøysundregisteret (string)
    :return: list containing 0 or more SignatureRecord
    """

    if not isinstance(authentications, list):
        raise TypeError("Authentications must be a list")

    signature_records = list()

    for authentication in authentications:
        signature_record = create_signature_record(brreg_change_report, authentication, secret)

        signature_records.append(signature_record)

    return signature_records


def create_sdo(brreg_change_report, authentications, secret):
    """
    Produce a complete SDO.

    Example (with two signatures):
    ::
        <SDO xmlns="http://schema.brreg.no/postmottak/BR-SDO">
            <SignedObject>
                PD94bWw....vbkVSRlY+
            </SignedObject>
            <Signatures>
                <SignatureRecord>
                    <SignedObjectHash algorithm="SHA-256">SV1F...bb2ZFaenVeEqI1VWuA=</SignedObjectHash>
                    <Authentication>
                        PD94bWwgdmVyc2lvbj0iMS4wIiBlbmN.....2VydGlvbj4=
                    </Authentication>
                    <RecordSeal algorithm="SHA-512">
                        yPY+0QKeixOouaqylKvgyd6lA5r.....zckrkAumLweDeA5141F2zIWMgPw==
                    </RecordSeal>
                </SignatureRecord>
                <SignatureRecord>
                    <SignedObjectHash algorithm="SHA-256">SV1FPI3Lneva9....qI1VWuA=</SignedObjectHash>
                    <Authentication>
                        PD94bWwgdmVyc2lvbj0iMS4wIiBlbmN.....pBc3NlcnRpb24+
                    </Authentication>
                    <RecordSeal algorithm="SHA-512">
                        rQ76lgrbrklfAaQXhGG2mNrjFk2aifCfY3lwmdr....HT903g9bEfYUIMtL4/2VZUGtmhw==
                    </RecordSeal>
                </SignatureRecord>
            </Signatures>
        </SDO>

    :param brreg_change_report: A complete XML of a change report, approved in precontrol (string)
    :param authentications: list containing signed SAML assertions (string)
    :param secret: Pre-shared secret, this must be requested from Brønnøysundregisteret (string)
    :return: Complete XML schema of SDO, as a string
    """

    namespace_prefix = "MagicalNSPrefix"

    document = fVM.SDO()
    pyxb_util.BindingDOMSupport.DeclareNamespace(fVM.Namespace, namespace_prefix)

    signed_object = create_signed_object(brreg_change_report)

    document.SignedObject = signed_object
    document.Signatures = fVM.Signatures()

    signatures = create_signature_record_list(brreg_change_report, authentications, secret)

    for signature in signatures:
        document.Signatures.append(signature)

    xml = document.toxml(element_name="SDO")

    opening = "{namespace}:".format(namespace=namespace_prefix)
    closing = ":{namespace}".format(namespace=namespace_prefix)

    xml = xml.replace(opening, "")
    xml = xml.replace(closing, "")

    return xml
