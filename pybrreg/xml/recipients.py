from generated import recipients
from ..utils.validation import validate_party


def create_recipient(party):
    """
    Create an XML instance containing the a party number

    Example:
    ::
        <ns1:Recipient>
            <ns1:PartyNumber>992838728</ns1:PartyNumber>
        </ns1:Recipient>


    :param party: The party to add as a recipient
    :type party: basestring
    :returns: A new element with the party
    :rtype: :py:class:`pybrreg.xml.generated.recipients.CTD_ANON_`

    """

    value = unicode(party)
    valid_value = validate_party(value)
    return recipients.CTD_ANON_(valid_value)


def create_broker_service_recipient_list(parties):
    """
    Create an XML instance containing a list of recipients.

    Example:
    ::
        <?xml version="1.0" ?>
        <BrokerServiceRecipientList xmlns:ns1="http://schema.altinn.n....">
            <ns1:Recipient>
                <ns1:PartyNumber>992838728</ns1:PartyNumber>
            </ns1:Recipient>
        </BrokerServiceRecipientList>


    :param parties: An iterable of parties that are to be recipients:
    :type parties: list, tuple
    :returns: XML element with the list of parties
    :rtype: :py:class:`pybrreg.xml.generated.recipients.BrokerServiceRecipientList`
    """

    recipient_list = recipients.BrokerServiceRecipientList()

    for party in parties:
        recipient = create_recipient(party)
        recipient_list.append(recipient)

    return recipient_list
