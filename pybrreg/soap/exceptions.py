# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class BrregException(Exception):
    pass


class BrregClientError(BrregException):
    pass


class InvalidServiceURLException(BrregClientError):
    pass


class InvalidUsernameException(BrregClientError):
    pass


class InvalidPasswordException(BrregClientError):
    pass


class InvalidLocationURLException(BrregClientError):
    pass


class NoResponseFromBrregException(BrregClientError):
    pass


class BrregServiceError(BrregException):

    def __init__(self, message, http_code=None, main_status_code=None, sub_status_code=None):
        super(BrregServiceError, self).__init__(message)

        self.http_code = http_code
        self.main_status_code = main_status_code
        self.sub_status_code = sub_status_code

    def __unicode__(self):
        args = {
            "message": self.message,
            "main_code": self.main_status_code,
            "sub_code": self.sub_status_code,
            "http_code": self.http_code
        }
        msg = "{message} (Error code: {main_code}, Sub code: {sub_code}, HTTP: {http_code})"
        return msg.format(**args)

    def __str__(self):
        return self.__unicode__()
