# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import base64
from io import BytesIO
from zipfile import ZipFile

from .new_inquiry import BrregNewInquiry
from .manifest import BrregManifest
from .recipients import BrregRecipientList


class BrregPackage(object):
    """
    Class for unpacking shipments from Brreg.
    """
    manifest = None
    inquiry = None
    recipients = None
    attachments = ()

    def __init__(self, file_data=None, b64_encoded=True):
        """
        Unpack and verify an incoming package.

        :param file_data: The file data stream from the package
        :type file_data: str
        :param b64_encoded: Flag to set if file_data is b64_encoded
        :type b64_encoded: bool
        """
        if file_data:
            self._read_package_file(file_data, b64_encoded=b64_encoded)

    def _read_package_file(self, file_data, b64_encoded=True):
        decoded = base64.b64decode(file_data) if b64_encoded else file_data
        memory_file = BytesIO(decoded)

        package_contents = {}
        with ZipFile(memory_file, "r") as f:
            for _file in f.infolist():
                opened_file = f.open(_file)
                filename = opened_file.name
                content = opened_file.read()
                package_contents[filename.lower()] = content

        manifest_xml = package_contents.pop('manifest.xml', None)
        if not manifest_xml:
            raise ValueError('Missing manifest.xml in package file.')

        self.manifest = BrregManifest(xml=manifest_xml)

        recipients_xml = package_contents.pop('recipients.xml', None)
        if recipients_xml:
            self.recipients = BrregRecipientList(xml=recipients_xml)

        inquiry_xml = package_contents.pop('henvendelse.xml', None)
        if not inquiry_xml:
            raise ValueError('Missing henvendelse.xml in package file.')
        self.inquiry = BrregNewInquiry(xml=inquiry_xml)

        for file_name, file_data in package_contents.items():
            att = self.inquiry.get_attachment(file_name)
            if att:
                att.file_data = file_data
        self.attachments = self.inquiry.attachments

    def get_attachment(self, file_name):
        return self.inquiry.get_attachment(file_name)
