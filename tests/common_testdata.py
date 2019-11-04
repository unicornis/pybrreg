# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import base64
from zipfile import ZipFile

import os
from io import BytesIO


class BrregTestPackage(object):
    loc = os.path.join(os.path.dirname(__file__), "test_files")
    manifest = None
    recipients = None
    henvendelse = None
    attachments = None

    def __init__(self, manifest=None, recipients=None, henvendelse=None, attachments=None,
                 subfolder=None):
        if subfolder:
            self.loc = os.path.join(self.loc, subfolder)
        if manifest:
            with open(os.path.join(self.loc, manifest), "r") as f:
                self.manifest = f.read()

        if recipients:
            with open(os.path.join(self.loc, recipients), "r") as f:
                self.recipients = f.read()

        if henvendelse:
            with open(os.path.join(self.loc, henvendelse), "r") as f:
                self.henvendelse = f.read()

        if attachments:
            self.attachments = list()
            for file_name in attachments:
                with open(os.path.join(self.loc, file_name), "r") as f:
                    self.attachments.append(BrregTestAttachment(file_name, f.read()))

    @property
    def zip(self):
        package_file = BytesIO()
        with ZipFile(package_file, mode="w") as f:
            if self.henvendelse:
                f.writestr("henvendelse.xml", self.henvendelse)
            if self.manifest:
                f.writestr("manifest.xml", self.manifest)
            if self.recipients:
                f.writestr("recipients.xml", self.recipients)
            # Add attachments
            if self.attachments:
                for att in self.attachments:
                    f.writestr(att.filename, att.file_data)

        return base64.b64encode(package_file.getvalue())


class BrregTestAttachment(object):

    def __init__(self, filename, file_data):
        self.filename = filename
        self.file_data = file_data
