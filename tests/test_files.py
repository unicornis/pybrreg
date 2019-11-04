# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

from pybrreg.utils.files import unpack_brreg_response_file
from .common_testdata import BrregTestPackage
from pybrreg.xml import generated


class ReadZipFileTests(unittest.TestCase):
    pdf_attachment_list = ["20170000416650-001-2017022675.pdf",
                           "20170000416650-001-2017022676.pdf"]

    def test_missing_henvendelse(self):
        contents = {
            "manifest": "manifest.xml",
            "recipients": "recipients.xml",
            "attachments": self.pdf_attachment_list,
            "subfolder": "vedtak"
        }
        package = BrregTestPackage(**contents).zip
        with self.assertRaises(ValueError):
            unpack_brreg_response_file(package)

    def test_missing_manifest(self):
        contents = {
            "henvendelse": "vedtak_melding.xml",
            "recipients": "recipients.xml",
            "attachments": self.pdf_attachment_list,
            "subfolder": "vedtak"
        }
        package = BrregTestPackage(**contents).zip
        with self.assertRaises(ValueError):
            unpack_brreg_response_file(package)

    def test_complete(self):
        contents = {
            "manifest": "manifest.xml",
            "henvendelse": "vedtak_melding_m_vedlegg.xml",
            "recipients": "recipients.xml",
            "attachments": self.pdf_attachment_list,
            "subfolder": "vedtak"
        }
        package = BrregTestPackage(**contents)

        manifest, henvendelse, recipients, attachments = unpack_brreg_response_file(package.zip)

        correct_manifest = generated.manifest.CreateFromDocument(package.manifest).toxml(encoding='utf-8')
        correct_henvendelse = generated.melding.CreateFromDocument(package.henvendelse).toxml(encoding='utf-8')
        correct_recipients = generated.recipients.CreateFromDocument(package.recipients).toxml(encoding='utf-8')
        self.assertEqual(manifest, correct_manifest)
        self.assertEqual(henvendelse, correct_henvendelse)
        self.assertEqual(recipients, correct_recipients)
        for att in package.attachments:
            self.assertEqual(att.file_data, attachments[att.filename]["content"])

    def test_application_receipt(self):
        contents = {
            'manifest': 'manifest.xml',
            'henvendelse': 'melding_henvendelse.xml',
            'recipients': 'recipients.xml',
            'subfolder': 'applikasjonskvittering'
        }
        package = BrregTestPackage(**contents)
        manifest, henvendelse, recipients, attachments = unpack_brreg_response_file(package.zip)

        correct_manifest = generated.manifest.CreateFromDocument(package.manifest).toxml(encoding='utf-8')
        correct_henvendelse = generated.melding.CreateFromDocument(package.henvendelse).toxml(encoding='utf-8')
        correct_recipients = generated.recipients.CreateFromDocument(package.recipients).toxml(encoding='utf-8')

        self.assertEqual(manifest, unicode(correct_manifest, 'utf-8'))

        self.assertEqual(henvendelse, unicode(correct_henvendelse, 'utf-8'))
        self.assertEqual(recipients, unicode(correct_recipients, 'utf-8'))
        self.assertIsNone(attachments)
