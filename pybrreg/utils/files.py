# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import base64
from datetime import datetime
from zipfile import ZipFile
from io import BytesIO
from pyxb.exceptions_ import PyXBException

from ..xml import generated
from .brreg_response import get_attachment_metadata


def unpack_brreg_response_file(file_data):
    if not file_data:
        raise ValueError("No file data received")
    decoded = base64.b64decode(file_data)

    mem_file = BytesIO(decoded)
    package_contents = dict()
    with ZipFile(mem_file, "r") as f:
        for _file in f.infolist():
            opened_file = f.open(_file)
            filename = opened_file.name
            content = opened_file.read()
            package_contents.update({filename.lower(): {"content": content}})

    # Manifest
    if "manifest.xml" not in package_contents.keys():
        raise ValueError("No Manifest.xml in package.")

    manifest_raw = package_contents.pop("manifest.xml").get("content")
    try:
        dom = generated.manifest.CreateFromDocument(manifest_raw)
        manifest = unicode(dom.toxml(encoding='utf-8'), 'utf-8')
    except PyXBException as error:
        raise ValueError("Error in parsing Brreg response: {}".format(error))

    if "henvendelse.xml" not in package_contents.keys():
        raise ValueError("No Henvendelse.xml in package")
    henvendelse_raw = package_contents.pop("henvendelse.xml").get("content")
    try:
        dom = generated.melding.CreateFromDocument(henvendelse_raw)
        henvendelse = unicode(dom.toxml(encoding='utf-8'), 'utf-8')
    except PyXBException as error:
        raise ValueError("Error in parsing Brreg response: {}".format(error))

    # Recipients
    recipients = None
    if "recipients.xml" in package_contents.keys():
        recipients_raw = package_contents.pop("recipients.xml").get("content")
        try:
            dom = generated.recipients.CreateFromDocument(recipients_raw)
            recipients = unicode(dom.toxml(encoding='utf-8'), 'utf-8')
        except PyXBException as error:
            raise ValueError("Error in parsing Brreg response: {}".format(error))

    # Add attachment metadata to attachments
    attachments = package_contents if len(package_contents) > 0 else None
    if attachments:
        att_metadata = get_attachment_metadata(henvendelse_raw)
        for att in attachments.keys():
            attachments[att]["metadata"] = att_metadata[att]
    return manifest, henvendelse, recipients, attachments
