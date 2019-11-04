# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from suds.plugin import MessagePlugin

from ..utils.logging import getLogger


class LogPlugin(MessagePlugin):

    def __init__(self, logger_name):
        if not logger_name.startswith('pybrreg'):
            logger_name = 'pybrreg.{}'.format(logger_name)
        self.logger_name = logger_name

    def sending(self, context):
        logger = getLogger(self.logger_name)
        logger.info(unicode(context.envelope))

    def received(self, context):
        logger = getLogger(self.logger_name)
        logger.info(unicode(context.reply))
