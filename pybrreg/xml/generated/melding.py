# ./melding.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:4a7f9ce82092d717db9bdc93ab4e90e43dfb3822
# Generated 2019-04-02 14:58:49.794345 by PyXB version 1.2.4 using Python 2.7.15.final.0
# Namespace http://schema.brreg.no/postmottak/henvendelse

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:0f32e6fa-5547-11e9-a343-c03fd5608144')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://schema.brreg.no/postmottak/henvendelse', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://schema.brreg.no/postmottak/henvendelse}stGUID
class stGUID (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stGUID')
    _XSDLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 47, 1)
    _Documentation = None
stGUID._CF_pattern = pyxb.binding.facets.CF_pattern()
stGUID._CF_pattern.addPattern(pattern='[A-Za-z0-9._-]{32,36}@?[A-Za-z0-9.-]{0,11}')
stGUID._InitializeFacetMap(stGUID._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'stGUID', stGUID)

# Atomic simple type: {http://schema.brreg.no/postmottak/henvendelse}stTekst32
class stTekst32 (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stTekst32')
    _XSDLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 186, 1)
    _Documentation = None
stTekst32._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(32))
stTekst32._InitializeFacetMap(stTekst32._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stTekst32', stTekst32)

# Atomic simple type: {http://schema.brreg.no/postmottak/henvendelse}stTekst64
class stTekst64 (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stTekst64')
    _XSDLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 191, 1)
    _Documentation = None
stTekst64._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(64))
stTekst64._InitializeFacetMap(stTekst64._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stTekst64', stTekst64)

# Atomic simple type: {http://schema.brreg.no/postmottak/henvendelse}stID
class stID (stGUID):

    """GUID"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stID')
    _XSDLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 52, 1)
    _Documentation = 'GUID'
stID._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stID', stID)

# Complex type {http://schema.brreg.no/postmottak/henvendelse}ctInnhold with content type ELEMENT_ONLY
class ctInnhold (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://schema.brreg.no/postmottak/henvendelse}ctInnhold with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctInnhold')
    _XSDLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 105, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schema.brreg.no/postmottak/henvendelse}Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Data'), 'Data', '__httpschema_brreg_nopostmottakhenvendelse_ctInnhold_httpschema_brreg_nopostmottakhenvendelseData', False, pyxb.utils.utility.Location('xsd/melding.xsd', 108, 4), )

    
    Data = property(__Data.value, __Data.set, None, 'Inkludert i xml dokumentet')

    
    # Element {http://schema.brreg.no/postmottak/henvendelse}DataRef uses Python identifier DataRef
    __DataRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataRef'), 'DataRef', '__httpschema_brreg_nopostmottakhenvendelse_ctInnhold_httpschema_brreg_nopostmottakhenvendelseDataRef', False, pyxb.utils.utility.Location('xsd/melding.xsd', 124, 4), )

    
    DataRef = property(__DataRef.value, __DataRef.set, None, 'Referanse til eksternt dokument (strukturert/ustrukturert)')

    _ElementMap.update({
        __Data.name() : __Data,
        __DataRef.name() : __DataRef
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ctInnhold', ctInnhold)


# Complex type {http://schema.brreg.no/postmottak/henvendelse}ctVedlegg with content type ELEMENT_ONLY
class ctVedlegg (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://schema.brreg.no/postmottak/henvendelse}ctVedlegg with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctVedlegg')
    _XSDLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 132, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schema.brreg.no/postmottak/henvendelse}Vedleggsdel uses Python identifier Vedleggsdel
    __Vedleggsdel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Vedleggsdel'), 'Vedleggsdel', '__httpschema_brreg_nopostmottakhenvendelse_ctVedlegg_httpschema_brreg_nopostmottakhenvendelseVedleggsdel', True, pyxb.utils.utility.Location('xsd/melding.xsd', 134, 3), )

    
    Vedleggsdel = property(__Vedleggsdel.value, __Vedleggsdel.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpschema_brreg_nopostmottakhenvendelse_ctVedlegg_type', pyxb.binding.datatypes.anySimpleType, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 153, 2)
    __type._UseLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 153, 2)
    
    type = property(__type.value, __type.set, None, 'type vedlegg, stiftelsesdokument, vedtekter, mm')

    
    # Attribute navn uses Python identifier navn
    __navn = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'navn'), 'navn', '__httpschema_brreg_nopostmottakhenvendelse_ctVedlegg_navn', pyxb.binding.datatypes.anySimpleType, required=True)
    __navn._DeclarationLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 158, 2)
    __navn._UseLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 158, 2)
    
    navn = property(__navn.value, __navn.set, None, 'navn p\xe5 vedlegget, kan benyttes for sporing til orginalvedlegg')

    _ElementMap.update({
        __Vedleggsdel.name() : __Vedleggsdel
    })
    _AttributeMap.update({
        __type.name() : __type,
        __navn.name() : __navn
    })
Namespace.addCategoryObject('typeBinding', 'ctVedlegg', ctVedlegg)


# Complex type {http://schema.brreg.no/postmottak/henvendelse}ctMeldingsKonvolutt with content type ELEMENT_ONLY
class ctMeldingsKonvolutt (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://schema.brreg.no/postmottak/henvendelse}ctMeldingsKonvolutt with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctMeldingsKonvolutt')
    _XSDLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 16, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schema.brreg.no/postmottak/henvendelse}Mottaker uses Python identifier Mottaker
    __Mottaker = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Mottaker'), 'Mottaker', '__httpschema_brreg_nopostmottakhenvendelse_ctMeldingsKonvolutt_httpschema_brreg_nopostmottakhenvendelseMottaker', False, pyxb.utils.utility.Location('xsd/melding.xsd', 18, 3), )

    
    Mottaker = property(__Mottaker.value, __Mottaker.set, None, None)

    
    # Element {http://schema.brreg.no/postmottak/henvendelse}Avsender uses Python identifier Avsender
    __Avsender = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Avsender'), 'Avsender', '__httpschema_brreg_nopostmottakhenvendelse_ctMeldingsKonvolutt_httpschema_brreg_nopostmottakhenvendelseAvsender', False, pyxb.utils.utility.Location('xsd/melding.xsd', 19, 3), )

    
    Avsender = property(__Avsender.value, __Avsender.set, None, None)

    
    # Element {http://schema.brreg.no/postmottak/henvendelse}Referanse uses Python identifier Referanse
    __Referanse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Referanse'), 'Referanse', '__httpschema_brreg_nopostmottakhenvendelse_ctMeldingsKonvolutt_httpschema_brreg_nopostmottakhenvendelseReferanse', True, pyxb.utils.utility.Location('xsd/melding.xsd', 20, 3), )

    
    Referanse = property(__Referanse.value, __Referanse.set, None, 'Kan brukes til \xe5 referere til tidligere sendte meldinger')

    
    # Attribute versjon uses Python identifier versjon
    __versjon = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'versjon'), 'versjon', '__httpschema_brreg_nopostmottakhenvendelse_ctMeldingsKonvolutt_versjon', stTekst32, required=True)
    __versjon._DeclarationLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 26, 2)
    __versjon._UseLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 26, 2)
    
    versjon = property(__versjon.value, __versjon.set, None, 'XSD versjon')

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpschema_brreg_nopostmottakhenvendelse_ctMeldingsKonvolutt_id', stGUID, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 31, 2)
    __id._UseLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 31, 2)
    
    id = property(__id.value, __id.set, None, 'UUID for melding')

    
    # Attribute tjeneste uses Python identifier tjeneste
    __tjeneste = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tjeneste'), 'tjeneste', '__httpschema_brreg_nopostmottakhenvendelse_ctMeldingsKonvolutt_tjeneste', stTekst64, required=True)
    __tjeneste._DeclarationLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 36, 2)
    __tjeneste._UseLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 36, 2)
    
    tjeneste = property(__tjeneste.value, __tjeneste.set, None, 'Registermelding, bestilling, brevsak, mm')

    
    # Attribute tjenestehandling uses Python identifier tjenestehandling
    __tjenestehandling = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tjenestehandling'), 'tjenestehandling', '__httpschema_brreg_nopostmottakhenvendelse_ctMeldingsKonvolutt_tjenestehandling', stTekst64, required=True)
    __tjenestehandling._DeclarationLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 41, 2)
    __tjenestehandling._UseLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 41, 2)
    
    tjenestehandling = property(__tjenestehandling.value, __tjenestehandling.set, None, 'Unik identifikasjon p\xe5 tjenestetype')

    _ElementMap.update({
        __Mottaker.name() : __Mottaker,
        __Avsender.name() : __Avsender,
        __Referanse.name() : __Referanse
    })
    _AttributeMap.update({
        __versjon.name() : __versjon,
        __id.name() : __id,
        __tjeneste.name() : __tjeneste,
        __tjenestehandling.name() : __tjenestehandling
    })
Namespace.addCategoryObject('typeBinding', 'ctMeldingsKonvolutt', ctMeldingsKonvolutt)


# Complex type {http://schema.brreg.no/postmottak/henvendelse}ctReferanse with content type EMPTY
class ctReferanse (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://schema.brreg.no/postmottak/henvendelse}ctReferanse with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctReferanse')
    _XSDLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 58, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute referanse uses Python identifier referanse
    __referanse = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'referanse'), 'referanse', '__httpschema_brreg_nopostmottakhenvendelse_ctReferanse_referanse', stTekst64, required=True)
    __referanse._DeclarationLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 59, 2)
    __referanse._UseLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 59, 2)
    
    referanse = property(__referanse.value, __referanse.set, None, 'Fritekst: URI, UUID, orgnr, formatert tekststreng, mm')

    
    # Attribute referanseType uses Python identifier referanseType
    __referanseType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'referanseType'), 'referanseType', '__httpschema_brreg_nopostmottakhenvendelse_ctReferanse_referanseType', stTekst32, required=True)
    __referanseType._DeclarationLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 64, 2)
    __referanseType._UseLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 64, 2)
    
    referanseType = property(__referanseType.value, __referanseType.set, None, 'Kan v\xe6re meldingsreferanse, avsenderreferanse, mm')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __referanse.name() : __referanse,
        __referanseType.name() : __referanseType
    })
Namespace.addCategoryObject('typeBinding', 'ctReferanse', ctReferanse)


# Complex type {http://schema.brreg.no/postmottak/henvendelse}ctAdresseID with content type SIMPLE
class ctAdresseID (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://schema.brreg.no/postmottak/henvendelse}ctAdresseID with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctAdresseID')
    _XSDLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 70, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpschema_brreg_nopostmottakhenvendelse_ctAdresseID_id', stTekst64, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 73, 4)
    __id._UseLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 73, 4)
    
    id = property(__id.value, __id.set, None, 'Fritekst: Orgnr, fnr, kundenr, formatert tekststreng, mm')

    
    # Attribute idType uses Python identifier idType
    __idType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'idType'), 'idType', '__httpschema_brreg_nopostmottakhenvendelse_ctAdresseID_idType', stTekst32, required=True)
    __idType._DeclarationLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 78, 4)
    __idType._UseLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 78, 4)
    
    idType = property(__idType.value, __idType.set, None, 'Forteller formatet p\xe5 ID')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __idType.name() : __idType
    })
Namespace.addCategoryObject('typeBinding', 'ctAdresseID', ctAdresseID)


# Complex type {http://schema.brreg.no/postmottak/henvendelse}ctAdressat with content type SIMPLE
class ctAdressat (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://schema.brreg.no/postmottak/henvendelse}ctAdressat with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctAdressat')
    _XSDLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 86, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpschema_brreg_nopostmottakhenvendelse_ctAdressat_id', stTekst64, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 92, 4)
    __id._UseLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 92, 4)
    
    id = property(__id.value, __id.set, None, 'Fritekst: Orgnr, fnr, kundenr, formatert tekststreng, mm')

    
    # Attribute idType uses Python identifier idType
    __idType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'idType'), 'idType', '__httpschema_brreg_nopostmottakhenvendelse_ctAdressat_idType', stTekst32, required=True)
    __idType._DeclarationLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 97, 4)
    __idType._UseLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 97, 4)
    
    idType = property(__idType.value, __idType.set, None, 'Forteller formatet p\xe5 ID')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __idType.name() : __idType
    })
Namespace.addCategoryObject('typeBinding', 'ctAdressat', ctAdressat)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Inkludert i xml dokumentet"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 112, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'format'), 'format', '__httpschema_brreg_nopostmottakhenvendelse_CTD_ANON_format', stTekst64, required=True)
    __format._DeclarationLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 115, 8)
    __format._UseLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 115, 8)
    
    format = property(__format.value, __format.set, None, 'Angir formatet p\xe5 data xml, pdf, doc, mm')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __format.name() : __format
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (ctInnhold):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 135, 4)
    _ElementMap = ctInnhold._ElementMap.copy()
    _AttributeMap = ctInnhold._AttributeMap.copy()
    # Base type is ctInnhold
    
    # Element Data ({http://schema.brreg.no/postmottak/henvendelse}Data) inherited from {http://schema.brreg.no/postmottak/henvendelse}ctInnhold
    
    # Element DataRef ({http://schema.brreg.no/postmottak/henvendelse}DataRef) inherited from {http://schema.brreg.no/postmottak/henvendelse}ctInnhold
    
    # Attribute sekvensnr uses Python identifier sekvensnr
    __sekvensnr = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sekvensnr'), 'sekvensnr', '__httpschema_brreg_nopostmottakhenvendelse_CTD_ANON__sekvensnr', pyxb.binding.datatypes.anySimpleType, required=True)
    __sekvensnr._DeclarationLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 138, 7)
    __sekvensnr._UseLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 138, 7)
    
    sekvensnr = property(__sekvensnr.value, __sekvensnr.set, None, 'Ved flere vedlegg, angi rekkef\xf8lge')

    
    # Attribute filnavn uses Python identifier filnavn
    __filnavn = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'filnavn'), 'filnavn', '__httpschema_brreg_nopostmottakhenvendelse_CTD_ANON__filnavn', pyxb.binding.datatypes.anySimpleType)
    __filnavn._DeclarationLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 143, 7)
    __filnavn._UseLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 143, 7)
    
    filnavn = property(__filnavn.value, __filnavn.set, None, 'navn p\xe5 vedleggsdel')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __sekvensnr.name() : __sekvensnr,
        __filnavn.name() : __filnavn
    })



# Complex type {http://schema.brreg.no/postmottak/henvendelse}ctDokumentReferanse with content type EMPTY
class ctDokumentReferanse (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://schema.brreg.no/postmottak/henvendelse}ctDokumentReferanse with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctDokumentReferanse')
    _XSDLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 164, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute referanse uses Python identifier referanse
    __referanse = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'referanse'), 'referanse', '__httpschema_brreg_nopostmottakhenvendelse_ctDokumentReferanse_referanse', stTekst64, required=True)
    __referanse._DeclarationLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 165, 2)
    __referanse._UseLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 165, 2)
    
    referanse = property(__referanse.value, __referanse.set, None, 'Fritekst: URI, UUID, formatert tekststreng, mm')

    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'format'), 'format', '__httpschema_brreg_nopostmottakhenvendelse_ctDokumentReferanse_format', stTekst64, required=True)
    __format._DeclarationLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 170, 2)
    __format._UseLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 170, 2)
    
    format = property(__format.value, __format.set, None, 'Angir formatet p\xe5 data xml, pdf, doc, mm')

    
    # Attribute referanseFormat uses Python identifier referanseFormat
    __referanseFormat = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'referanseFormat'), 'referanseFormat', '__httpschema_brreg_nopostmottakhenvendelse_ctDokumentReferanse_referanseFormat', stTekst32)
    __referanseFormat._DeclarationLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 175, 2)
    __referanseFormat._UseLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 175, 2)
    
    referanseFormat = property(__referanseFormat.value, __referanseFormat.set, None, 'Forteller formatet p\xe5 referansen')

    
    # Attribute sjekksum uses Python identifier sjekksum
    __sjekksum = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sjekksum'), 'sjekksum', '__httpschema_brreg_nopostmottakhenvendelse_ctDokumentReferanse_sjekksum', pyxb.binding.datatypes.hexBinary)
    __sjekksum._DeclarationLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 180, 2)
    __sjekksum._UseLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 180, 2)
    
    sjekksum = property(__sjekksum.value, __sjekksum.set, None, 'Brukt for \xe5 oppbevare hashverdi (hvis den eksisterer) for den eksterne referansen')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __referanse.name() : __referanse,
        __format.name() : __format,
        __referanseFormat.name() : __referanseFormat,
        __sjekksum.name() : __sjekksum
    })
Namespace.addCategoryObject('typeBinding', 'ctDokumentReferanse', ctDokumentReferanse)


# Complex type {http://schema.brreg.no/postmottak/henvendelse}ctMelding with content type ELEMENT_ONLY
class ctMelding (ctMeldingsKonvolutt):
    """Complex type {http://schema.brreg.no/postmottak/henvendelse}ctMelding with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctMelding')
    _XSDLocation = pyxb.utils.utility.Location('xsd/melding.xsd', 5, 1)
    _ElementMap = ctMeldingsKonvolutt._ElementMap.copy()
    _AttributeMap = ctMeldingsKonvolutt._AttributeMap.copy()
    # Base type is ctMeldingsKonvolutt
    
    # Element {http://schema.brreg.no/postmottak/henvendelse}Innhold uses Python identifier Innhold
    __Innhold = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Innhold'), 'Innhold', '__httpschema_brreg_nopostmottakhenvendelse_ctMelding_httpschema_brreg_nopostmottakhenvendelseInnhold', False, pyxb.utils.utility.Location('xsd/melding.xsd', 9, 5), )

    
    Innhold = property(__Innhold.value, __Innhold.set, None, None)

    
    # Element {http://schema.brreg.no/postmottak/henvendelse}Vedlegg uses Python identifier Vedlegg
    __Vedlegg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Vedlegg'), 'Vedlegg', '__httpschema_brreg_nopostmottakhenvendelse_ctMelding_httpschema_brreg_nopostmottakhenvendelseVedlegg', True, pyxb.utils.utility.Location('xsd/melding.xsd', 10, 5), )

    
    Vedlegg = property(__Vedlegg.value, __Vedlegg.set, None, None)

    
    # Element {http://schema.brreg.no/postmottak/henvendelse}Signatur uses Python identifier Signatur
    __Signatur = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Signatur'), 'Signatur', '__httpschema_brreg_nopostmottakhenvendelse_ctMelding_httpschema_brreg_nopostmottakhenvendelseSignatur', False, pyxb.utils.utility.Location('xsd/melding.xsd', 11, 5), )

    
    Signatur = property(__Signatur.value, __Signatur.set, None, None)

    
    # Element Mottaker ({http://schema.brreg.no/postmottak/henvendelse}Mottaker) inherited from {http://schema.brreg.no/postmottak/henvendelse}ctMeldingsKonvolutt
    
    # Element Avsender ({http://schema.brreg.no/postmottak/henvendelse}Avsender) inherited from {http://schema.brreg.no/postmottak/henvendelse}ctMeldingsKonvolutt
    
    # Element Referanse ({http://schema.brreg.no/postmottak/henvendelse}Referanse) inherited from {http://schema.brreg.no/postmottak/henvendelse}ctMeldingsKonvolutt
    
    # Attribute versjon inherited from {http://schema.brreg.no/postmottak/henvendelse}ctMeldingsKonvolutt
    
    # Attribute id inherited from {http://schema.brreg.no/postmottak/henvendelse}ctMeldingsKonvolutt
    
    # Attribute tjeneste inherited from {http://schema.brreg.no/postmottak/henvendelse}ctMeldingsKonvolutt
    
    # Attribute tjenestehandling inherited from {http://schema.brreg.no/postmottak/henvendelse}ctMeldingsKonvolutt
    _ElementMap.update({
        __Innhold.name() : __Innhold,
        __Vedlegg.name() : __Vedlegg,
        __Signatur.name() : __Signatur
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ctMelding', ctMelding)


Melding = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Melding'), ctMelding, location=pyxb.utils.utility.Location('xsd/melding.xsd', 4, 1))
Namespace.addCategoryObject('elementBinding', Melding.name().localName(), Melding)



ctInnhold._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Data'), CTD_ANON, scope=ctInnhold, documentation='Inkludert i xml dokumentet', location=pyxb.utils.utility.Location('xsd/melding.xsd', 108, 4)))

ctInnhold._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataRef'), ctDokumentReferanse, scope=ctInnhold, documentation='Referanse til eksternt dokument (strukturert/ustrukturert)', location=pyxb.utils.utility.Location('xsd/melding.xsd', 124, 4)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctInnhold._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Data')), pyxb.utils.utility.Location('xsd/melding.xsd', 108, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctInnhold._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataRef')), pyxb.utils.utility.Location('xsd/melding.xsd', 124, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ctInnhold._Automaton = _BuildAutomaton()




ctVedlegg._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Vedleggsdel'), CTD_ANON_, scope=ctVedlegg, location=pyxb.utils.utility.Location('xsd/melding.xsd', 134, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctVedlegg._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Vedleggsdel')), pyxb.utils.utility.Location('xsd/melding.xsd', 134, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ctVedlegg._Automaton = _BuildAutomaton_()




ctMeldingsKonvolutt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Mottaker'), ctAdressat, scope=ctMeldingsKonvolutt, location=pyxb.utils.utility.Location('xsd/melding.xsd', 18, 3)))

ctMeldingsKonvolutt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Avsender'), ctAdressat, scope=ctMeldingsKonvolutt, location=pyxb.utils.utility.Location('xsd/melding.xsd', 19, 3)))

ctMeldingsKonvolutt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Referanse'), ctReferanse, scope=ctMeldingsKonvolutt, documentation='Kan brukes til \xe5 referere til tidligere sendte meldinger', location=pyxb.utils.utility.Location('xsd/melding.xsd', 20, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('xsd/melding.xsd', 20, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ctMeldingsKonvolutt._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Mottaker')), pyxb.utils.utility.Location('xsd/melding.xsd', 18, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctMeldingsKonvolutt._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Avsender')), pyxb.utils.utility.Location('xsd/melding.xsd', 19, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctMeldingsKonvolutt._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Referanse')), pyxb.utils.utility.Location('xsd/melding.xsd', 20, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ctMeldingsKonvolutt._Automaton = _BuildAutomaton_2()




def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Data')), pyxb.utils.utility.Location('xsd/melding.xsd', 108, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataRef')), pyxb.utils.utility.Location('xsd/melding.xsd', 124, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_3()




ctMelding._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Innhold'), ctInnhold, scope=ctMelding, location=pyxb.utils.utility.Location('xsd/melding.xsd', 9, 5)))

ctMelding._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Vedlegg'), ctVedlegg, scope=ctMelding, location=pyxb.utils.utility.Location('xsd/melding.xsd', 10, 5)))

ctMelding._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Signatur'), pyxb.binding.datatypes.anyType, scope=ctMelding, location=pyxb.utils.utility.Location('xsd/melding.xsd', 11, 5)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('xsd/melding.xsd', 20, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('xsd/melding.xsd', 10, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('xsd/melding.xsd', 11, 5))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ctMelding._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Mottaker')), pyxb.utils.utility.Location('xsd/melding.xsd', 18, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ctMelding._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Avsender')), pyxb.utils.utility.Location('xsd/melding.xsd', 19, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ctMelding._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Referanse')), pyxb.utils.utility.Location('xsd/melding.xsd', 20, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctMelding._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Innhold')), pyxb.utils.utility.Location('xsd/melding.xsd', 9, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ctMelding._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Vedlegg')), pyxb.utils.utility.Location('xsd/melding.xsd', 10, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ctMelding._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Signatur')), pyxb.utils.utility.Location('xsd/melding.xsd', 11, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ctMelding._Automaton = _BuildAutomaton_4()

