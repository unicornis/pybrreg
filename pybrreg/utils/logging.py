# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import logging


def getLogger(name=None):
    """Prepends 'pybrreg.<project>' to the standard dotted path given by `name`.

    Normal usage:
        from pybrreg.utils import logging
        logging.getLogger(__name__)
    """
    logger_name = 'pybrreg.{}'.format(name)
    return logging.getLogger(logger_name)
