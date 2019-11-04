# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..xml.generated import recipients


class BrregRecipientList(object):
    """
    altinn:BrokerServiceRecipientList

    XSD: https://confluence.brreg.no/pages/viewpage.action?pageId=43128450&preview=/43128450/52043785/Recipients.xsd

    Example dict structure:
    data = {
        'parties': [
            '[recipient 1]',
            '[recipient 2]'
        ]
    }
    """

    def __init__(self, parties=(), xml=None):
        """
        Construct a new recipient list

        Passing a value in xml will ignore any other arguments in favor of it.

        :param parties: Parties that are recipients for the package, each as a string
        :type parties: list or tuple
        :param xml: XML document of BrokerServiceRecipientList
        :type xml: basestring
        """
        if xml:
            element = recipients.CreateFromDocument(xml)
            self.parties = [recipient.PartyNumber for recipient in element.Recipient]
            return

        self.parties = parties

    @property
    def element(self):
        """
        PyXB element for BrokerServiceRecipientList

        :return: Complete element
        :rtype: :py:class: pybrreg.xml.generated.recipients.BrokerServiceRecipientList
        """
        elem = recipients.BrokerServiceRecipientList()
        for party in self.parties:
            elem.append(recipients.CTD_ANON_(party))
        return elem

    def to_xml(self, encoding='utf-8'):
        """
        Get a BrokerServiceRecipientList XML document.

        :param encoding: Character encoding for the document declaration. Default: 'utf-8'
        :type encoding: basestring
        :return: XML document of BrokerServiceRecipientList
        :rtype: basestring
        """
        return self.element.toxml(encoding=encoding)
