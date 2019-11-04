# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import os

import unittest

from pybrreg.utils.brreg_response import get_reference_from_henvendelse_melding



# NEW NEW NEW
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
