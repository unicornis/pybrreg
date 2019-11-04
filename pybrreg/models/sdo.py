# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import base64
import hashlib

from pyxb.utils.domutils import BindingDOMSupport

from ..xml.generated import frivintVerifisertMelding


class BrregSDO(object):
    """
    brreg:frivintVerifisertMelding

    XSD: http://schema.brreg.no/postmottak/frivintVerifisertMelding.xsd

    Documentation: https://confluence.brreg.no/pages/viewpage.action?pageId=43127764

    :py:class:`pybrreg.models.application_receipt.BrregApplicationReceipt`
    """

    _signed_object_hash = None
    _signed_object = None

    def __init__(self, change_report=None, authentications=(), secret=None, ns_prefix='brreg'):
        """
        Construct a new SDO.

        :param change_report: The report that has been signed as XML. Must be a properly encoded byte string.
        :type change_report: str
        :param authentications: Signatures, SAML assertions from IDPorten, list of XML strings
        :type authentications: list or tuple
        :param secret: Pre-shared secret from Brreg
        :type secret: basestring
        :param ns_prefix: Namespace prefix for the XML elements. Defaults to 'brreg'
        :type ns_prefix: basestring
        """
        self.ns_prefix = ns_prefix
        self.change_report = change_report
        self.secret = secret
        self.signatures = [BrregSignature(self.signed_object_hash, auth, secret) for auth in authentications]

    @property
    def element(self):
        """
        Get the PyXB element for frivintVerifisertMelding

        :return: Completed element
        :rtype: :py:class:`pybrreg.xml.generated.frivintVerifisertMelding.SDO`
        """
        BindingDOMSupport.DeclareNamespace(frivintVerifisertMelding.Namespace, self.ns_prefix)
        elem = frivintVerifisertMelding.SDO()
        elem.SignedObject = self.signed_object
        elem.Signatures = frivintVerifisertMelding.Signatures()
        for signature in self.signatures:
            elem.Signatures.append(signature.element)

        return elem

    @property
    def signed_object_hash(self):
        """
        Calculation: base64(sha256(base64(change_report)))

        :return: The base64-encoded value of the hashed base64-encoded change report
        :rtype: basestring
        """
        hashed = hashlib.sha256(self.signed_object)
        return base64.b64encode(hashed.digest())

    @property
    def signed_object(self):
        """
        :return: The change report in Base64
        :rtype: basestring
        """
        return base64.b64encode(self.change_report)

    def to_xml(self, encoding='utf-8', strip_namespace=False, strip_header=False):
        """
        Get the SDO as a valid XML document.

        :param encoding: Character encoding for the document declaration. Default: 'utf-8'
        :type encoding: basestring
        :param strip_namespace: Enable removal of all namespace prefixes in document. Default: False
        :type strip_namespace: bool
        :param strip_header: Strip the XML header (encoding tag etc) from the document. Default: False
        :type strip_header: bool
        :return: The XML document of frivintVerifisertMelding
        :rtype: basestring
        """
        xml = self.element.toxml(encoding=encoding)
        if strip_namespace:
            xml = self._strip_namespace(xml)
        if strip_header:
            xml = self._strip_header(xml, encoding)
        return xml

    def _strip_namespace(self, xml):
        opening = '{ns}:'.format(ns=self.ns_prefix)
        closing = ':{ns}'.format(ns=self.ns_prefix)
        xml = xml.replace(opening, '')
        xml = xml.replace(closing, '')
        return xml

    @staticmethod
    def _strip_header(xml, encoding):
        xml_tag = '<?xml version="1.0" encoding="{}"?>'.format(encoding)
        xml = xml.replace(xml_tag, '')
        return xml


class BrregSignature(object):
    """
    brreg:frivintVerifisertMelding:SignatureRecord

    Each signature has one record, which contains a hashed SAML assertion, the Signed Object Hash and a
    Record Seal.
    """

    _algorithm = 'SHA-256'

    def __init__(self, signed_object_hash, authentication, secret):
        """
        Signature instance.

        :param signed_object_hash: Calculated SOH, from :py:data: pybrreg.models.sdo.SDO.signed_object_hash
        :type signed_object_hash: basestring
        :param authentication: The SAML assertion for this signature in XML
        :type authentication: basestring
        :param secret: Pre-shared secret from Brreg
        :type secret: basestring
        """
        self.signed_object_hash = signed_object_hash
        self.authentication = authentication
        self.record_seal = RecordSeal(authentication, signed_object_hash, secret)

    @property
    def element(self):
        """
        Build the PyXB element for SignatureRecord

        :return: The completed element
        :rtype: :py:class: pybrreg.xml.generated.frivintVerifisertMelding.SignatureRecord
        """
        elem = frivintVerifisertMelding.SignatureRecord()
        elem.SignedObjectHash = frivintVerifisertMelding.SignedObjectHash(self.signed_object_hash,
                                                                          algorithm=self._algorithm)
        elem.Authentication = base64.b64encode(self.authentication)
        elem.RecordSeal = self.record_seal.element
        return elem


class RecordSeal(object):
    """
    brreg:frivintVerifisertMelding:RecordSeal

    Seal for a single signature, used to verify when received.
    """

    _algorithm = 'SHA-512'

    def __init__(self, authentication, signed_object_hash, secret):
        """
        New instance.

        :param authentication: SAML assertion for the signature to be sealed
        :type authentication: basestring,
        :param signed_object_hash: Calculated SOH: :py:data: pybrreg.models.sdo.SDO.signed_object_hash
        :type signed_object_hash: basestring,
        :param secret: Pre-shared secret from Brreg
        :type secret: basestring
        """
        self.authentication = authentication
        self.signed_object_hash = signed_object_hash
        self.secret = secret

    @property
    def element(self):
        """
        Get the PyXB element for RecordSeal.

        :return: Completed element
        :rtype: :py:class: pybrreg.xml.generated.frivintVerifisertMelding.RecordSeal
        """
        elem = frivintVerifisertMelding.RecordSeal(self.value, algorithm=self._algorithm)
        return elem

    @property
    def value(self):
        """
        Calculate the RecordSeal value.

        Base64(SHA-512(Signed Object Hash + Base64(SAML:Assertion) + Secret)

        :return: The calculated value
        :rtype: basestring
        """
        hashed = hashlib.sha512()
        hashed.update(self.signed_object_hash)
        hashed.update(base64.b64encode(self.authentication))
        hashed.update(self.secret)
        encoded = base64.b64encode(hashed.digest())
        return encoded
