# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from ..xml.generated import manifest


class BrregManifest(object):
    """
    altinn:BrokerServiceManifest

    XSD: https://confluence.brreg.no/download/attachments/43128450/Manifest.xsd?version=1&modificationDate=1470728918000&api=v2
    Example XML: https://confluence.brreg.no/download/attachments/43128450/manifest.xml?version=1&modificationDate=1495520498000&api=v2

    Example dict structure:
    data = {
        'senders_reference': '[UUID reference]',
        'reportee': '[reportee ID]',
        'file_list': [
            ('[file name]', '[checksum]'),
            ('[file name 2]', '[checksum 2]'),
        ],
        'property_list': [
            ('[property]', '[value]'),
            ('[property 2]', '[value 2]')
        ]
    }
    """

    _external_service_code = '4202'
    _external_service_edition_code = '1'
    _timestamp_format = '%Y-%m-%dT%H:%M:%S'

    def __init__(self, senders_reference=None, reportee=None, file_list=(), property_list=(), xml=None):
        """
        Construct a Manifest

        :param senders_reference: UUID reference for the shipment, same as Henvendelse:id
        :type senders_reference: basestring
        :param reportee: Organisation or social security number of the sender
        :type reportee: basestring
        :param file_list: List of the files in the shipment, in the format of (file_name, checksum)
        :type file_list: list or tuple
        :param property_list: List of extra properties, in the format of (property_key, value)
        :type property_list: list or tuple
        :param xml: XML Document of BrokerServiceManifest
        :type xml: basestring
        """
        if xml:
            self._from_xml(xml)
            return

        self.senders_reference = senders_reference
        self.sent_date = datetime.now().strftime(self._timestamp_format)
        self.reportee = reportee
        self.file_list = file_list
        self.property_list = property_list

    @property
    def element(self):
        """
        Get the PyXB element for BrokerServiceManifest

        :return: Completed element
        :rtype: :py:class: pybrreg.xml.generated.CTD_ANON()
        """
        elem = manifest.BrokerServiceManifest()
        elem.ExternalServiceCode = self._external_service_code
        elem.ExternalServiceEditionCode = self._external_service_edition_code
        elem.SendersReference = self.senders_reference
        elem.Reportee = self.reportee
        elem.sentDate = self.sent_date

        if self.file_list:
            elem.FileList = manifest.CTD_ANON_()
            for file_ in self.file_list:
                if isinstance(file_, tuple):
                    file_name, checksum = file_
                else:
                    file_name = file_
                    checksum = None
                file_elem = manifest.CTD_ANON_2()
                file_elem.FileName = file_name
                if checksum:
                    file_elem.CheckSum = checksum
                elem.FileList.append(file_elem)

        if self.property_list:
            elem.PropertyList = manifest.CTD_ANON_3()
            for key, value in self.property_list:
                prop_elem = manifest.CTD_ANON_4()
                prop_elem.PropertyKey = key
                prop_elem.PropertyValue = value
                elem.PropertyList.append(prop_elem)

        return elem

    def _from_xml(self, xml):
        element = manifest.CreateFromDocument(xml)
        self.senders_reference = element.SendersReference
        self.reportee = element.Reportee
        self.sent_date = element.SentDate
        self.file_list = []
        self.property_list = []

        if hasattr(element.FileList, 'File'):
            for file_ in element.FileList.File:
                file_name = file_.FileName
                checksum = file_.CheckSum
                if checksum:
                    self.file_list.append((file_name, checksum))
                else:
                    self.file_list.append(file_name)

        if hasattr(element.PropertyList, 'Property'):
            for prop in element.PropertyList.Property:
                self.property_list.append((prop.PropertyKey, prop.PropertyValue))

    def to_xml(self, encoding='utf-16'):
        """
        Get the manifest as a valid XML document

        :param encoding: Encoding for the document declaration. Default: utf-16
        :type encoding: basestring,
        :return: XML document of BrokerServiceManifest
        :rtype: basestring
        """
        return self.element.toxml(encoding=encoding)
