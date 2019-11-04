# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from ..exceptions import BrregServiceError
from ..utils.response import parse_response

from pybrreg.utils.logging import getLogger


log = getLogger(__name__)


def verify_procuration_signature(client, organisation_number):
    log.info("Preparing to request Brreg:hentProkuraSignaturFdato")
    log.info("Querying orgno: {}".format(unicode(organisation_number)))
    input_fields = {
        "userid": client.username,
        "password": client.password,
        "orgnr": unicode(organisation_number)
    }

    log.debug("Dispatching request to service.")
    brreg_response = client.get_procuration_signature_fdate(**input_fields)
    log.debug("Received response from service.")

    log.debug("Parsing response from service.")
    try:
        header, content = parse_response(brreg_response)
        log.debug("Parsing complete.")
    except BrregServiceError as error:
        log.error(error)
        raise
    log.info("Response:Header --- {}".format(json.dumps(header)))
    log.info("Response:Content --- {}".format(json.dumps(content)))
    return header, content
