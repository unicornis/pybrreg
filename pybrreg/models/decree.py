# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..xml.generated import vedtak


class BrregDecree(object):

    def __init__(self, xml):
        element = vedtak.CreateFromDocument(xml)
        self.system_id = element.SLsysId
        self.system_message_id = element.SLsysMeldingsId
        self.organisation_number = element.organisasjonsnummer
        self.er_status = element.ERSaksstatus
        self.fv_status = element.FVSaksstatus
