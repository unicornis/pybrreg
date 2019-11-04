from __future__ import unicode_literals

import unittest

from pybrreg.xml import recipients


class PartyNumberTests(unittest.TestCase):

    def setUp(self):
        self.org_no = "992838728"
        self.ssn = "18048100232"

        self.expected_org_no = """<?xml version="1.0" ?><PartyNumber xmlns:ns1="http://schema.altinn.no/services/ServiceEngine/Broker/2015/06"><ns1:PartyNumber>992838728</ns1:PartyNumber></PartyNumber>"""  # NOQA
        self.expected_ssn = """<?xml version="1.0" ?><PartyNumber xmlns:ns1="http://schema.altinn.no/services/ServiceEngine/Broker/2015/06"><ns1:PartyNumber>18048100232</ns1:PartyNumber></PartyNumber>"""  # NOQA

    def test_invalid(self):
        with self.assertRaises(ValueError):
            recipients.create_recipient(None)

        with self.assertRaises(ValueError):
            recipients.create_recipient(False)

    def test_invalid_org_no(self):
        with self.assertRaises(ValueError):
            recipients.create_recipient("9105143500")

    def test_valid_org_no(self):
        party_number = recipients.create_recipient(self.org_no)

        result = party_number.toxml(element_name="PartyNumber")

        self.assertEqual(self.expected_org_no, result)

    def test_invalid_ssn(self):
        with self.assertRaises(ValueError):
            recipients.create_recipient("01010750165")

    def test_valid_ssn(self):
        party_number = recipients.create_recipient(self.ssn)

        result = party_number.toxml(element_name="PartyNumber")

        self.assertEqual(self.expected_ssn, result)


class BrokerServiceRecipientListTests(unittest.TestCase):

    def setUp(self):
        self.org_no = "992838728"
        self.ssn = "18048100232"

        self.expected_multiple = """<?xml version="1.0" ?><BrokerServiceRecipientList xmlns:ns1="http://schema.altinn.no/services/ServiceEngine/Broker/2015/06"><ns1:Recipient><ns1:PartyNumber>992838728</ns1:PartyNumber></ns1:Recipient><ns1:Recipient><ns1:PartyNumber>18048100232</ns1:PartyNumber></ns1:Recipient></BrokerServiceRecipientList>"""  # NOQA
        self.expected_single = """<?xml version="1.0" ?><BrokerServiceRecipientList xmlns:ns1="http://schema.altinn.no/services/ServiceEngine/Broker/2015/06"><ns1:Recipient><ns1:PartyNumber>992838728</ns1:PartyNumber></ns1:Recipient></BrokerServiceRecipientList>"""  # NOQA

    def test_single(self):
        rec = recipients.create_broker_service_recipient_list([self.org_no])
        result = rec.toxml(element_name="BrokerServiceRecipientList")
        self.assertEqual(self.expected_single, result)

    def test_multiple(self):
        rec = recipients.create_broker_service_recipient_list([self.org_no, self.ssn])
        result = rec.toxml(element_name="BrokerServiceRecipientList")
        self.assertEqual(self.expected_multiple, result)
