# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..xml.generated import applikasjonskvittering


class BrregApplicationReceipt(object):
    """
    brreg:Applikasjonskvittering
    """

    def __init__(self, xml):
        element = applikasjonskvittering.CreateFromDocument(xml)
        self.status = element.Status
        self.status_text = element.StatusTekst
        self.status_code = element.StatusKode
        self.message_reference = element.MeldingsReferanse
        self.sender_reference = element.AvsendersReferanse

    @property
    def has_error(self):
        """
        Check if this application receipt contains an error.

        :rtype: bool
        """
        return self.status == 'OK'
