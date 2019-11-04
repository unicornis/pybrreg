# -*- coding: utf-8 -*-
from datetime import datetime

from generated import manifest
from ..utils.validation import validate_party


def create_broker_service_manifest(external_service_code, external_service_edition_code,
                                   senders_reference, reportee, files=None, properties=None):
    """
    Create an XML schema describing the Broker Service Manifest to be sent via Altinn.

    Example:
    ::
        <?xml version="1.0" encoding="utf-8"?>
        <BrokerServiceManifest xmlns:ns1="http://...">
            <ns1:ExternalServiceCode>4202</ns1:ExternalServiceCode>
            <ns1:ExternalServiceEditionCode>1</ns1:ExternalServiceEditionCode>
            <ns1:SendersReference>Refno</ns1:SendersReference>
            <ns1:Reportee>992838728</ns1:Reportee>
            <ns1:SentDate>2016-01-01T15:21:34</ns1:SentDate>
            <ns1:FileList>
                <ns1:File>
                    <ns1:FileName>testfile1</ns1:FileName>
                    <ns1:CheckSum>testfile1checksum</ns1:CheckSum>
                </ns1:File>
            </ns1:FileList>
            <ns1:PropertyList>
                <ns1:Property>
                    <ns1:PropertyKey>key</ns1:PropertyKey>
                    <ns1:PropertyValue>value</ns1:PropertyValue>
                </ns1:Property>
                <ns1:Property>
                    <ns1:PropertyKey>key2</ns1:PropertyKey>
                    <ns1:PropertyValue>value2</ns1:PropertyValue>
                </ns1:Property>
            </ns1:PropertyList>
        </BrokerServiceManifest>

    :param external_service_code: Service code for the request
    :type external_service_code: int, basestring
    :param external_service_edition_code: Service edition code for this request
    :type external_service_edition_code: int, basestring
    :param senders_reference: Sender reference for the request
    :type senders_reference: basestring
    :param reportee: Sender of file
    :type reportee: basestring
    :param files: Files in a list of tuples (filename, checksum)
    :type files: list, tuple
    :param properties: Properties in a list of tuple (key, value)
    :type properties: list, tuple
    :returns: Manifest XML instance
    :rtype: :py:class:`pybrreg.xml.generated.manifest.CTD_ANON()`
    """
    broker_manifest = manifest.CTD_ANON()
    broker_manifest.ExternalServiceEditionCode = unicode(external_service_edition_code)
    broker_manifest.ExternalServiceCode = unicode(external_service_code)
    broker_manifest.SendersReference = unicode(senders_reference)
    try:
        broker_manifest.Reportee = validate_party(unicode(reportee))
    except ValueError:
        err_msg = "Reportee: {} is not a valid value.".format(reportee)
        raise ValueError(err_msg)

    now = datetime.now()
    sent_date = now.strftime("%Y-%m-%dT%H:%M:%S")
    broker_manifest.SentDate = sent_date

    if files:
        file_list = manifest.CTD_ANON_()
        for file_info in files:
            file_list.append(create_file(*file_info))

        broker_manifest.FileList = file_list

    if properties:
        property_list = manifest.CTD_ANON_3()
        for prop in properties:
            property_list.append(create_property(*prop))

        broker_manifest.PropertyList = property_list

    return broker_manifest


def create_file(file_name, checksum):
    """
    Create an XML schema describing a file.

    Example:
    ::
        <ns1:File>
            <ns1:FileName>testfile1</ns1:FileName>
            <ns1:CheckSum>testfile1checksum</ns1:CheckSum>
        </ns1:File>

    :param file_name: File name of file to add
    :type file_name: basestring
    :param checksum: Checksum of file contents
    :type checksum: basestring
    :returns: XML element
    :rtype: :py:class:`pybrreg.xml.generated.manifest.CTD_ANON_2`
    """
    attachment_file = manifest.CTD_ANON_2()
    attachment_file.FileName = unicode(file_name)
    attachment_file.CheckSum = unicode(checksum)

    return attachment_file


def create_property(key, value):
    """
    Generate an XML schema describing a property.

    Example:
    ::
        <ns1:Property>
            <ns1:PropertyKey>key2</ns1:PropertyKey>
            <ns1:PropertyValue>value2</ns1:PropertyValue>
        </ns1:Property>

    :param key: Key for the property
    :type key: basestring
    :param value: Value of the property
    :type value: basestring
    :returns: XML element
    :rtype: :py:class:`pybrreg.xml.generated.manifest.CTD_ANON_4()`
    """

    prop = manifest.CTD_ANON_4()
    prop.PropertyKey = unicode(key)
    prop.PropertyValue = unicode(value)

    return prop
