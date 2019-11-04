# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
import unittest

from mock import mock

from pybrreg.soap.client import BrregSOAPClient
from pybrreg.soap.exceptions import (InvalidUsernameException, InvalidPasswordException, InvalidServiceURLException,
                                     InvalidLocationURLException)

class ClientTests(unittest.TestCase):

    def setUp(self):
        self.service_url = "http://example.com"
        self.username = "username"
        self.password = "password"
        self.location_url = "location_url"

    def test_service_url(self):
        bad_inputs = [None, "", "http:/example.com", 123, 2.0]

        for val in bad_inputs:
            args = (val, self.username, self.password)
            with self.assertRaises(InvalidServiceURLException):
                BrregSOAPClient(*args)

    def test_username(self):
        bad_inputs = [None, ""]

        for val in bad_inputs:
            args = (self.service_url, val, self.password)
            with self.assertRaises(InvalidUsernameException):
                BrregSOAPClient(*args)

    def test_password(self):
        bad_inputs = [None, ""]

        for val in bad_inputs:
            args = (self.service_url, self.username, val)
            with self.assertRaises(InvalidPasswordException):
                BrregSOAPClient(*args)

    def test_location_url(self):
        bad_inputs = ["http:/example.com", 123, 2.0]
        args = (self.service_url, self.username, self.password)
        for val in bad_inputs:
            with self.assertRaises(InvalidLocationURLException):
                BrregSOAPClient(*args, location_url=val)

    @mock.patch("pybrreg.soap.client.BrregSOAPClient._setup_client", side_effect=lambda **kwargs: True)
    def test_get_logger(self, mocked_setup):
        log_args = {
            'log_level': logging.INFO,
            'log_name': 'pybrreg_test'
        }
        brreg_client = BrregSOAPClient(self.service_url, self.username, self.password, **log_args)
        mocked_setup.assert_called_with(faults=False, wsse=False)
        log = brreg_client.get_logger()
        self.assertEqual(len(log.handlers), 1)
        self.assertEqual(log.level, logging.INFO)
        self.assertEqual(log.name, 'pybrreg.pybrreg.soap.client')

        # Test handler duplication
        log2 = brreg_client.get_logger()
        self.assertEqual(len(log2.handlers), 1)

        # Test handlers
        handler = log.handlers[0]
        self.assertEqual(handler.level, logging.INFO)



