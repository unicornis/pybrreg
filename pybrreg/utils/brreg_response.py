# -*- coding utf-8 -*-
from __future__ import unicode_literals

from hashlib import md5

from pyxb.exceptions_ import PyXBException

from ..xml.generated import melding
from ..xml.generated import applikasjonskvittering, vedtak


def get_reference_from_henvendelse_melding(henvendelse):
    ns = "http://schema.brreg.no/postmottak/henvendelse"
    melding_ = melding.CreateFromDocument(henvendelse, ns)
    return melding_.Referanse[0].referanse


def get_attachment_metadata(henvendelse):
    attachments = {}
    xml = melding.CreateFromDocument(henvendelse)
    attachment_list = xml.Vedlegg
    for a in attachment_list:
        att_info = {
            a.Vedleggsdel[0].filnavn: {
                'type': a.type,
                'description': a.navn,
                'file_format': a.Vedleggsdel[0].DataRef.referanseFormat,
                'checksum': md5(a.Vedleggsdel[0].DataRef.sjekksum).hexdigest(),
            }
        }
        attachments.update(att_info)
    return attachments


def get_response_content(henvendelse):
    """
    Get the response type and content from a Henvendelse XML document.

    :param henvendelse: The relevant inquiry
    :type henvendelse: unicode
    :return: The type of response and its content
    :rtype: tuple(unicode, dict)
    """
    if isinstance(henvendelse, str):
        henvendelse = unicode(henvendelse, 'utf-8')
    parsers = {
        'application_receipt': applikasjonskvittering.CreateFromDocument,
        'decree': vedtak.CreateFromDocument
    }

    melding_ = melding.CreateFromDocument(henvendelse)
    content_xml = melding_.Innhold.Data.value()
    response_type = 'application_receipt' if "Applikasjonskvittering" in content_xml else 'decree'
    return response_type, parsers[response_type](content_xml)
