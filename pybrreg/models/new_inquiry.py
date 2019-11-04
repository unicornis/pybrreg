# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from hashlib import md5
import re
import pyxb

from pyxb.namespace.builtin import XMLSchema_instance as xsi

from ..xml.generated import melding

from .decree import BrregDecree
from .application_receipt import BrregApplicationReceipt


class BrregNewInquiry(object):
    """
    brreg:Melding.

    XSD: https://schema.brreg.no/postmottak/melding.xsd
    Documentation: https://confluence.brreg.no/display/FRIVINTDOK/XSD+for+melding

    Example dict structure (please note that not all values are required, please see the XSD for details):
    inquiry = {
            'id': '[uuid reference]',
            'recipient': {
                'id': '[identifying value]',
                'id_type': '[type of identifying value]',
            },
            'sender': {
                'id': '[identifying value]',
                'id_type': '[type of identifying value]',
            },
            'service_action': '[action to be requested]',
            'content': {
                'data': '[your message]',
            },
            'message': {
                'id': '[uuid reference]',
                'recipient': {
                    'id': '[identifying value]',
                    'id_type': '[type of identifying value]',
                },
                'sender': {
                    'id': '[identifying value]',
                    'id_type': '[type of identifying value]',
                },
                'attachments': [{
                    'type': '[attachment type]',
                    'name': '[attachment name]',
                    'file_name': '[attachment file name]',
                    'sequence_no': '[which file in the collection]'
                }]
            }
        }
    """

    _version = '4.0'
    _service = 'intef'

    def __init__(self, id=None, recipient=None, sender=None, message=None, xml=None,
                    service_action=None, reference=None, content=None, attachments=[]):
        """
        Construct a new instance. If a document is passed in the xml variable, other variables are
        ignored in favor of it, as it implies constructing a full instance based on that XML document.

        :param id: UUID for this inquiry, identical to Manifest:SendersReference
        :type id: basestring
        :param recipient: Recipient party for the inquiry, likely Brønnøysundregistrene
        :type recipient: dict
        :param sender: Sending party for the inquiry
        :type sender: dict
        :param message: The message contents of this inquiry
        :type message: dict
        :param xml: Raw XML document of the type Melding
        :param xml: basestring
        """
        self.schemaLocation = "http://schema.brreg.no/postmottak/melding.xsd"
        if xml:
            self._parse_from_xml(xml)
            return

        self.id = id
        self.recipient = BrregAdressee(**recipient) if recipient else None
        self.sender = BrregAdressee(**sender) if sender else None

        self.service_action = service_action
        self.reference = reference
        self.reference = BrregReference(**reference) if reference else None
        self.content = Content(**content) if content else None
        atts = []
        for att in attachments:
            atts.append(BrregInquiryAttachment(**att))
        self.random = atts
        self.attachments = atts

    @property
    def element(self):
        """
        Build a PyXB element of this instance.

        Eeach sub-element of this element is constructed from its classes, compiling into a full, valid document.

        :return: The completed element
        :rtype: py:class: pybrreg.xml.generated.melding.Melding
        """
        elem = melding.Melding()
        elem.id = self.id
        elem.Mottaker = self.recipient.element
        elem.Avsender = self.sender.element
        
        elem.tjenestehandling = self.service_action
        elem.Innhold = self.content.element

        for attachment in self.attachments:
            elem.Vedlegg.append(attachment.element)

        elem.versjon = self._version
        elem.tjeneste = self._service

        if self.reference:
            elem.Referanse.append(self.reference.element)

        return elem


    def to_xml(self, encoding='utf-8'):
        """
        Get an XML document from this instance and its values.

        :param encoding: Character encoding to declare the XML document with. Default: utf-8
        :type encoding: basestring
        :return: The complete XML document of brreg:Melding
        :rtype: unicode
        """
        bds = pyxb.utils.domutils.BindingDOMSupport()
        bds.setDefaultNamespace(melding.Namespace)
        bds.declareNamespace(xsi)
        elem_dom = self.element.toDOM(bds)
        bds.addAttribute(elem_dom.documentElement, xsi.createExpandedName(
            'schemaLocation'), self.schemaLocation)
        bds.addXMLNSDeclaration(elem_dom.documentElement, xsi)
        return elem_dom.toxml(encoding=encoding)

    def _parse_from_xml(self, xml):
        elem = melding.CreateFromDocument(xml)
        self.id = elem.id
        self.recipient = BrregAdressee(element=elem.Mottaker)
        self.sender = BrregAdressee(element=elem.Avsender)
        self.content = Content(element=elem.Innhold)
        self.attachments = [BrregInquiryAttachment(element=element) for element in elem.Vedlegg]
        self.service_action = elem.tjenestehandling
        self.reference = BrregReference(element=elem.Referanse[0])

    def get_content(self):
        """
        Get the actual contents of the inquiry.

        See :py:func: pybrreg.models.inquiry.Content.parse
        """
        return self.content.parse()

    def get_reference(self):
        return self.get_reference()

    def get_attachment(self, file_name):
        for att in self.attachments:
            if att.file_name.lower() == file_name.lower():
                return att
        return None


class BrregReference(object):
    """
    NEW
    brreg:EksternReferanse

    External (custom) reference for tracking in the client application.
    """

    def __init__(self, reference=None, reference_type=None, element=None):
        """
        If element is supplied, all other arguments are ignored.

        :param reference: The reference value
        :type reference: basestring
        :param reference_type: The type of reference, see documentation for valid values
        :type reference_type: basestring
        :param element: PyXB element of EksternReferanse
        :type element: :py:class: pybrreg.xml.generated.basic.ctEksternReferanse
        """
        if element:
            self.reference = element.referanse
            self.reference_type = element.referanseType
            return

        self.reference = reference
        self.reference_type = reference_type

    @property
    def element(self):
        """
        Get the PyXB element for Referanse.


        :return: Completed element
        :rtype: :py:class: pybrreg.xml.generated.basic.ctEksternReferanse
        """
        elem = melding.ctReferanse()
        elem.referanse = self.reference
        elem.referanseType = self.reference_type
        return elem


class BrregInquiryAttachment(object):
    """
    brreg:Melding:Vedlegg

    Attachments for the inquiry.
    """
    def __init__(self, type=None, name=None, file_name=None, reference_format=None,
                 checksum=None, sequence_no='1', element=None, file_data=None,
                format=None):
        """
        If element is provided, all other arguments are ignored.


        :param type: Attachment type
        :type type: basestring
        :param name: Name of the file
        :type name: basestring
        :param file_name: Filename (Can be identical to name)
        :type file_name: basestring
        :param reference_format: Format of the reference
        :type reference_format: basestring
        :param checksum: MD5 checksum of the document contents
        :type checksum: basestring
        :param sequence_no: Number in the collection (defaults to 1, as it is always valid)
        :type sequence_no: basestring
        :param element: PyXB element of Vedlegg
        :type element: :py:class: pybrreg.xml.generated.henvendelse.CTD_ANON_()
        """
        if element:
            self.type = element.type
            self.name = element.navn
            self.file_name = element.Vedleggsdel[0].filnavn
            self.reference_format = element.Vedleggsdel[0].DataRef.referanseFormat
            self.format = element.Vedleggsdel[0].DataRef.format
            self.sequence_no = element.Vedleggsdel[0].sekvensnr
            self.checksum = md5(element.Vedleggsdel[0].DataRef.sjekksum).hexdigest()
            return

        self.type = type
        self.name = name
        self.file_name = file_name
        self.format = format
        self.sequence_no = sequence_no
        self.reference_format = reference_format
        self.checksum = checksum
        self.file_data = file_data


    @property
    def element(self):
        """
        Get the PyXB element for Vedlegg.

        :return: The completed element
        :rtype: :py:class: pybrreg.xml.generated.henvendelse.CTD_ANON_()
        """
        elem = melding.ctVedlegg()
        elem.type = self.type
        elem.navn = self.name

        details = melding.CTD_ANON_()
        details.sekvensnr = self.sequence_no
        details.filnavn = self.file_name


        reference = melding.ctDokumentReferanse()
        reference.referanse = self.file_name
        reference.referanseFormat = self.reference_format
        reference.checksum = self.checksum
        reference.format = self.format

        details.DataRef = reference
        
        elem.append(details)
        return elem


class BrregAdressee(object):
    """
    NEW
    brreg:basic:AdressatType

    Used for recipient or sender
    """

    def __init__(self, id=None, id_type=None, element=None):
        """
        If element is provided, all other arguments are ignored.

        :param id: Identifier for addressee
        :type id: basestring
        :param id_type: Type of identifier
        :type id_type: basestring
        :param element: PyXB element of AdressatType
        :type element: :py:class: pybrreg.xml.generated.basic.ctAdressat
        """
        if element:
            self.id = element.id
            self.id_type = element.idType
            return

        self.id_type = id_type
        self.id = id

    @property
    def element(self):
        """
        Get the PyXB element for AdressatType

        :return: Completed element
        :rtype: :py:class: pybrreg.xml.generated.basic.ctAdressat
        """
        elem = melding.ctAdressat()
        elem.id = self.id
        elem.idType = self.id_type
        return elem


class Content(object):
    """
    brreg:Henvendelse:SkjemaInnhold

    Contents of the inquiry.
    """
    def __init__(self, data=None, format='XML', element=None):
        """
        If element is provided, all other arguments are ignored.

        :param data: Raw document that you wish to send
        :type data: basestring
        :param format: Format of the document you are sending, defaults to 'XML'
        :type format: basestring
        :param element: PyXB element of SkjemaInnhold
        :type element: :py:class: pybrreg.xml.generated.basic.ctInnhold
        """
        if element:
            self.data = element.Data.value()
            self.format = element.Data.format
            return
        self.data = data
        self.format = format


        



    @property
    def element(self):
        """
        Get the PyXB element for this instance.

        :return: The completed element
        :rtype: :py:class: pybrreg.xml.generated.basic.ctInnhold
        """
        elem = melding.ctInnhold()

        data = melding.CTD_ANON(self.data)
        data.format = self.format

        elem.Data = data
        
        return elem

    def parse(self):
        pattern = re.compile('<(\w+)\s')
        object_map = {
            'IntegrasjonERFV_Vedtak': BrregDecree,
            'Applikasjonskvittering': BrregApplicationReceipt
        }
        if self.format.lower() == 'XML'.lower():
            cont_type = pattern.match(self.data).groups()[0]
            cls = object_map.get(cont_type)
            return cls(self.data) if cls else self.data

        return self.data
