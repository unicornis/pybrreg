# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import os

import unittest

from pybrreg.utils.brreg_response import (get_reference_from_henvendelse_melding, get_response_content,
    get_attachment_metadata)


class ReferenceFromMeldingTests(unittest.TestCase):
    def setUp(self):
        base_path = os.path.dirname(os.path.realpath(__name__))
        xml_file = os.path.join('tests', 'test_files', 'applikasjonskvittering', 'melding_henvendelse.xml')
        file_path = os.path.join(base_path, xml_file)
        with open(file_path, 'r') as xml_file:
            self.xml = xml_file.read()

    def test_get_reference(self):
        reference = get_reference_from_henvendelse_melding(self.xml)
        self.assertEqual('6185bdd3-07ea-4788-b240-f7da281e3cdc', reference)


# This might not be needed
class ResponseContentTests(unittest.TestCase):

    def setUp(self):
        self.base_path = os.path.dirname(os.path.realpath(__name__))

    def test_get_response_content_applikasjonskvittering(self):
        xml_file = os.path.join('tests', 'test_files', 'applikasjonskvittering', 'melding_henvendelse.xml')
        file_path = os.path.join(self.base_path, xml_file)
        with open(file_path, 'r') as xml_file:
            xml = xml_file.read()

        result_type, content = get_response_content(unicode(xml, 'utf-8'))
        self.assertEqual(result_type, 'application_receipt')

    def test_get_response_content_applikasjonskvittering_with_error(self):
        xml_file = os.path.join('tests', 'test_files', 'applikasjonskvittering', 'app_receipt_reject_example.xml')
        file_path = os.path.join(self.base_path, xml_file)
        with open(file_path, 'r') as xml_file:
            xml = xml_file.read()

        result_type, content = get_response_content(xml)
        self.assertEqual(result_type, 'application_receipt')

    def test_get_response_content_decree_inc_attachment(self):
        xml_file = os.path.join('tests', 'test_files', 'vedtak', 'vedtak_melding_m_vedlegg.xml')
        file_path = os.path.join(self.base_path, xml_file)
        with open(file_path, 'r') as xml_file:
            xml = xml_file.read()
        result_type, content = get_response_content(unicode(xml, 'utf-8'))
        self.assertEqual(result_type, 'decree')

    def test_get_response_content_decree(self):
        xml_file = os.path.join('tests', 'test_files', 'vedtak', 'vedtak_melding_m_vedlegg.xml')
        file_path = os.path.join(self.base_path, xml_file)
        with open(file_path, 'r') as xml_file:
            xml = xml_file.read()
        result_type, content = get_response_content(unicode(xml, 'utf-8'))
        self.assertEqual(result_type, 'decree')


class AttachmentInfoTests(unittest.TestCase):

    def setUp(self):
        base_path = os.path.dirname(os.path.realpath(__name__))
        xml_file = os.path.join('tests', 'test_files', 'vedtak', 'vedtak_melding_m_vedlegg.xml')
        file_path = os.path.join(base_path, xml_file)
        with open(file_path, 'r') as xml_file:
            self.xml = xml_file.read()

    def test_get_attachments(self):
        response = get_attachment_metadata(self.xml)
        self.assertEqual(len(response), 2)
