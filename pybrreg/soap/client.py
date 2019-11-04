# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import inspect
import json
import logging 
from logging.handlers import TimedRotatingFileHandler
import os

from suds.client import Client
from suds.wsse import Security, UsernameToken
import validators

from ..models.roles import RoleData
from ..utils.converters import convert_signature_procuration
from ..utils.logging import getLogger

from .exceptions import (InvalidLocationURLException, InvalidServiceURLException, InvalidPasswordException,
                         InvalidUsernameException, BrregClientError, NoResponseFromBrregException)
from .plugins import LogPlugin
from .utils.response import transform_brreg_data


log = getLogger(__name__)


class BrregSOAPClient(object):
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"
    LOG_ROLLOVER = 'midnight'

    _suds_client = None
    _service_url = None
    _username = None
    _password = None
    _location_url = None

    def __init__(self, service_url, username, password, location_url=None, faults=False, wsse=False, **kwargs):

        if kwargs:
            stack = inspect.stack()
            stack_funcs = [s[3] for s in stack]
            log.warning('Invalid args passed to BrregSOAPClient: {} (stack funcs: {})'.format(repr(kwargs),
                                                                                              stack_funcs))
        self.service_url = service_url
        self.username = username
        self.password = password
        if location_url:
            self.location_url = location_url

        # set up logging
        self.log_name = kwargs.pop('log_name', '')
        self.log_level = kwargs.pop('log_level', logging.INFO)
        self.log_format = self.LOG_FORMAT
        self.log_rollover = self.LOG_ROLLOVER
        self.log_location = kwargs.pop('log_location', '.')
        self._setup_client(faults=faults, wsse=wsse)

    @property
    def service_url(self):
        """ The WSDL location for this service. """
        return self._service_url

    @service_url.setter
    def service_url(self, value):
        if not value:
            raise InvalidServiceURLException('Service url is required')
        service_url = unicode(value)
        if not validators.url(service_url):
            raise InvalidServiceURLException('{} is not a valid url'.format(service_url))
        self._service_url = service_url

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not value:
            raise InvalidUsernameException('Username is required.')
        self._username = unicode(value)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if not value:
            raise InvalidPasswordException('Password is required.')
        self._password = unicode(value)

    @property
    def location_url(self):
        return self._location_url

    @location_url.setter
    def location_url(self, value):
        if not value:
            raise InvalidLocationURLException('Service url is required')
        location_url = unicode(value)
        if not validators.url(location_url):
            raise InvalidLocationURLException('{} is not a valid url'.format(location_url))
        self._location_url = location_url

    def get_logger(self):
        if len(log.handlers) >= 1:
            # Just return the globally defined logger if it's already correctly
            # set up
            return log
        if not os.path.exists(self.log_location):
            os.makedirs(self.log_location)
        log_file = os.path.join(self.log_location, '{}.log'.format(self.log_name))

        file_handler = TimedRotatingFileHandler(log_file, when=self.log_rollover)
        file_handler.setLevel(self.log_level)
        file_handler.setFormatter(logging.Formatter(self.log_format))
        log.addHandler(file_handler)
        log.setLevel(self.log_level)
        return log

    def _setup_client(self, faults=False, wsse=False):
        client_args = {
            'url': self.service_url,
            'faults': faults,
            'plugins': [LogPlugin(self.log_name)],
            'timeout': 100,
        }
        log.info("Setting up SOAP client with WSDL at {wsdl_url}".format(wsdl_url=self.service_url))
        if self.location_url:
            log.info("Overloading default location url with {url}".format(url=self.location_url))
            client_args['location'] = self.location_url
        if wsse:
            log.info("Using WSSE for authentication.")
            security = Security()
            # noinspection PyTypeChecker
            security.tokens.append(UsernameToken(self.username, self.password))
            client_args['wsse'] = security
        else:
            log.info("NOT using WSSE for authentication.")

        try:
            suds_client = Client(**client_args)
        except Exception as error:
            import traceback
            log.error(traceback.format_exc())
            err_prefix = "Could not create SOAP client at {url}. Error message: {err}"
            err_msg = err_prefix.format(url=self.service_url, err=unicode(error))
            raise BrregClientError(err_msg)

        self._suds_client = suds_client


class PrecontrolServiceClient(BrregSOAPClient):
    def __init__(self, *args, **kwargs):
        kwargs['faults'] = True
        kwargs['wsse'] = True
        super(PrecontrolServiceClient, self).__init__(*args, **kwargs)

    @staticmethod
    def error(brreg_error):
        return {
            'message': brreg_error.get('#text'),
            'code': brreg_error.get('@id'),
        }

    def validate_input(self, xml):
        return self._suds_client.service.validereInput(xml)

    def perform_precontrol(self, xml):
        from .service.precontrol import perform_precontrol
        return perform_precontrol(self, xml)


class VolunteerRegistryServiceClient(BrregSOAPClient):

    def call_ws(self, endpoint, org):
        log.info("Requesting {endpoint} with organisation {org}".format(endpoint=endpoint, org=org))
        ws_endpoint = getattr(self._suds_client.service, endpoint)
        args = {
            'userid': self.username,
            'password': self.password,
            'orgnr': unicode(org)
        }
        log.info("Dispatching request")
        response_code, response = ws_endpoint(**args)
        log.info("Parsing response")
        transformed = transform_brreg_data(response, endpoint)  # We could do better response types
        log.info("Response: {}".format(json.dumps(transformed)))
        return transformed

    def get_volunteering(self, **kwargs):
        return self._suds_client.service.hentFrivillighet(**kwargs)

    def get_volunteer_data(self, organisation):
        return self.call_ws('hentFrivillighet', organisation)


class UnitRegistryServiceClient(BrregSOAPClient):

    def call_ws(self, endpoint, org=None, transform=True):
        log.info("Requesting {endpoint} with organisation {org}".format(endpoint=endpoint, org=org))
        ws_endpoint = getattr(self._suds_client.service, endpoint)
        args = {
            'userid': self.username,
            'password': self.password,
        }
        if org:
            args['orgnr'] = unicode(org)
        log.info("Dispatching request")
        response_code, response = ws_endpoint(**args)
        log.info("Parsing response")

        if not transform:
            log.info("Transform is disabled, returning raw response.")
            return response
        if response == None:
            raise NoResponseFromBrregException()
        transformed = transform_brreg_data(response, endpoint)
        log.info("Response: {}".format(json.dumps(transformed)))
        return transformed

    def get_base_data(self, **kwargs):
        return self._suds_client.service.hentBasisdata(**kwargs)

    def get_base_data_fdate(self, **kwargs):
        return self._suds_client.service.hentBasisdataFdato(**kwargs)

    def get_procuration_signature_fdate(self, **kwargs):
        return self._suds_client.service.hentProkuraSignaturFdato(**kwargs)

    def get_contact_data(self, **kwargs):
        return self._suds_client.service.hentKontaktdata(**kwargs)

    def verify_procuration_signature(self, organisation_number):
        from .service.unit import verify_procuration_signature
        header, content = verify_procuration_signature(self, organisation_number)
        return convert_signature_procuration(content)

    def get_base_data_for_org(self, organisation):
        return self.call_ws('hentBasisdataFdato', organisation)

    def get_roles_for_org(self, organisation):
        response = self.call_ws('hentRollerFdato', organisation, transform=False)
        return RoleData(response).json()

    def get_contact_data_for_org(self, organisation):
        return self.call_ws('hentKontaktdata', organisation)
