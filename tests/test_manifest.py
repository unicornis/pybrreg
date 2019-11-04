# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import datetime
import mock

from freezegun import freeze_time

from pybrreg.xml import manifest

minimal_xml = """<?xml version="1.0" encoding="utf-8"?><BrokerServiceManifest xmlns:ns1="http://schema.altinn.no/services/ServiceEngine/Broker/2015/06"><ns1:ExternalServiceCode>4202</ns1:ExternalServiceCode><ns1:ExternalServiceEditionCode>1</ns1:ExternalServiceEditionCode><ns1:SendersReference>Refno</ns1:SendersReference><ns1:Reportee>992838728</ns1:Reportee><ns1:SentDate>2016-01-01T15:21:34</ns1:SentDate></BrokerServiceManifest>"""  # NOQA

xml_with_files = """<?xml version="1.0" encoding="utf-8"?><BrokerServiceManifest xmlns:ns1="http://schema.altinn.no/services/ServiceEngine/Broker/2015/06"><ns1:ExternalServiceCode>4202</ns1:ExternalServiceCode><ns1:ExternalServiceEditionCode>1</ns1:ExternalServiceEditionCode><ns1:SendersReference>Refno</ns1:SendersReference><ns1:Reportee>992838728</ns1:Reportee><ns1:SentDate>2016-01-01T15:21:34</ns1:SentDate><ns1:FileList><ns1:File><ns1:FileName>testfile1</ns1:FileName><ns1:CheckSum>testfile1checksum</ns1:CheckSum></ns1:File></ns1:FileList></BrokerServiceManifest>"""  # NOQA

xml_with_files_and_properties = """<?xml version="1.0" encoding="utf-8"?><BrokerServiceManifest xmlns:ns1="http://schema.altinn.no/services/ServiceEngine/Broker/2015/06"><ns1:ExternalServiceCode>4202</ns1:ExternalServiceCode><ns1:ExternalServiceEditionCode>1</ns1:ExternalServiceEditionCode><ns1:SendersReference>Refno</ns1:SendersReference><ns1:Reportee>992838728</ns1:Reportee><ns1:SentDate>2016-01-01T15:21:34</ns1:SentDate><ns1:FileList><ns1:File><ns1:FileName>testfile1</ns1:FileName><ns1:CheckSum>testfile1checksum</ns1:CheckSum></ns1:File></ns1:FileList><ns1:PropertyList><ns1:Property><ns1:PropertyKey>key</ns1:PropertyKey><ns1:PropertyValue>value</ns1:PropertyValue></ns1:Property><ns1:Property><ns1:PropertyKey>key2</ns1:PropertyKey><ns1:PropertyValue>value2</ns1:PropertyValue></ns1:Property></ns1:PropertyList></BrokerServiceManifest>"""  # NOQA


def datetime_override():
    return datetime.datetime(2016, 01, 01, hour=15, minute=21, second=34)


class BrokerServiceManifestTests(unittest.TestCase):

    def setUp(self):
        self.files = [("testfile1", "testfile1checksum")]
        self.properties = [("key", "value"), ("key2", "value2")]

    @freeze_time("2016-01-01 15:21:34")
    def test_minimal_xml(self):
        broker_manifest = manifest.create_broker_service_manifest("4202", "1", "Refno", "992838728")

        result = broker_manifest.toxml(element_name="BrokerServiceManifest", encoding="utf-8")

        self.assertEqual(result, minimal_xml)

    @freeze_time("2016-01-01 15:21:34")
    def test_with_files(self):
        broker_manifest = manifest.create_broker_service_manifest("4202", "1", "Refno", "992838728",
                                                                  files=self.files)

        result = broker_manifest.toxml(element_name="BrokerServiceManifest", encoding="utf-8")
        self.assertEqual(result, xml_with_files)

    @freeze_time("2016-01-01 15:21:34")
    def test_with_files_and_properties(self):
        broker_manifest = manifest.create_broker_service_manifest("4202", "1", "Refno", "992838728",
                                                                  files=self.files,
                                                                  properties=self.properties)

        result = broker_manifest.toxml(element_name="BrokerServiceManifest", encoding="utf-8")
        self.assertEqual(result, xml_with_files_and_properties)
