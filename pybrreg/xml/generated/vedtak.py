# ./vedtak.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:4fc5c7413205275a62d9d9ef5eb6b54189f72f38
# Generated 2016-10-28 08:41:31.796198 by PyXB version 1.2.4 using Python 2.7.12.final.0
# Namespace http://schema.brreg.no/intef/integrasjonERFV_Vedtak

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:8fe9b87e-9cd9-11e6-8f24-eca86bfbeec6')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://schema.brreg.no/intef/integrasjonERFV_Vedtak', create_if_missing=True)
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


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('xsd/integrasjonERFV_Vedtak.xsd', 8, 5)
    _Documentation = None
STD_ANON._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(4))
STD_ANON._InitializeFacetMap(STD_ANON._CF_totalDigits)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('xsd/integrasjonERFV_Vedtak.xsd', 15, 5)
    _Documentation = None
STD_ANON_._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_minLength,
   STD_ANON_._CF_maxLength)

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('xsd/integrasjonERFV_Vedtak.xsd', 23, 5)
    _Documentation = None
STD_ANON_2._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(9))
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_length)

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('xsd/integrasjonERFV_Vedtak.xsd', 30, 5)
    _Documentation = None
STD_ANON_3._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_length)

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('xsd/integrasjonERFV_Vedtak.xsd', 37, 5)
    _Documentation = None
STD_ANON_4._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_length)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('xsd/integrasjonERFV_Vedtak.xsd', 5, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schema.brreg.no/intef/integrasjonERFV_Vedtak}SLsysId uses Python identifier SLsysId
    __SLsysId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SLsysId'), 'SLsysId', '__httpschema_brreg_nointefintegrasjonERFV_Vedtak_CTD_ANON_httpschema_brreg_nointefintegrasjonERFV_VedtakSLsysId', False, pyxb.utils.utility.Location('xsd/integrasjonERFV_Vedtak.xsd', 7, 4), )

    
    SLsysId = property(__SLsysId.value, __SLsysId.set, None, None)

    
    # Element {http://schema.brreg.no/intef/integrasjonERFV_Vedtak}SLsysMeldingsId uses Python identifier SLsysMeldingsId
    __SLsysMeldingsId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SLsysMeldingsId'), 'SLsysMeldingsId', '__httpschema_brreg_nointefintegrasjonERFV_Vedtak_CTD_ANON_httpschema_brreg_nointefintegrasjonERFV_VedtakSLsysMeldingsId', False, pyxb.utils.utility.Location('xsd/integrasjonERFV_Vedtak.xsd', 14, 4), )

    
    SLsysMeldingsId = property(__SLsysMeldingsId.value, __SLsysMeldingsId.set, None, None)

    
    # Element {http://schema.brreg.no/intef/integrasjonERFV_Vedtak}organisasjonsnummer uses Python identifier organisasjonsnummer
    __organisasjonsnummer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'organisasjonsnummer'), 'organisasjonsnummer', '__httpschema_brreg_nointefintegrasjonERFV_Vedtak_CTD_ANON_httpschema_brreg_nointefintegrasjonERFV_Vedtakorganisasjonsnummer', False, pyxb.utils.utility.Location('xsd/integrasjonERFV_Vedtak.xsd', 22, 4), )

    
    organisasjonsnummer = property(__organisasjonsnummer.value, __organisasjonsnummer.set, None, None)

    
    # Element {http://schema.brreg.no/intef/integrasjonERFV_Vedtak}ERSaksstatus uses Python identifier ERSaksstatus
    __ERSaksstatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ERSaksstatus'), 'ERSaksstatus', '__httpschema_brreg_nointefintegrasjonERFV_Vedtak_CTD_ANON_httpschema_brreg_nointefintegrasjonERFV_VedtakERSaksstatus', False, pyxb.utils.utility.Location('xsd/integrasjonERFV_Vedtak.xsd', 29, 4), )

    
    ERSaksstatus = property(__ERSaksstatus.value, __ERSaksstatus.set, None, None)

    
    # Element {http://schema.brreg.no/intef/integrasjonERFV_Vedtak}FVSaksstatus uses Python identifier FVSaksstatus
    __FVSaksstatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FVSaksstatus'), 'FVSaksstatus', '__httpschema_brreg_nointefintegrasjonERFV_Vedtak_CTD_ANON_httpschema_brreg_nointefintegrasjonERFV_VedtakFVSaksstatus', False, pyxb.utils.utility.Location('xsd/integrasjonERFV_Vedtak.xsd', 36, 4), )

    
    FVSaksstatus = property(__FVSaksstatus.value, __FVSaksstatus.set, None, None)

    _ElementMap.update({
        __SLsysId.name() : __SLsysId,
        __SLsysMeldingsId.name() : __SLsysMeldingsId,
        __organisasjonsnummer.name() : __organisasjonsnummer,
        __ERSaksstatus.name() : __ERSaksstatus,
        __FVSaksstatus.name() : __FVSaksstatus
    })
    _AttributeMap.update({
        
    })



IntegrasjonERFV_Vedtak = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IntegrasjonERFV_Vedtak'), CTD_ANON, location=pyxb.utils.utility.Location('xsd/integrasjonERFV_Vedtak.xsd', 4, 1))
Namespace.addCategoryObject('elementBinding', IntegrasjonERFV_Vedtak.name().localName(), IntegrasjonERFV_Vedtak)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SLsysId'), STD_ANON, scope=CTD_ANON, location=pyxb.utils.utility.Location('xsd/integrasjonERFV_Vedtak.xsd', 7, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SLsysMeldingsId'), STD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('xsd/integrasjonERFV_Vedtak.xsd', 14, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'organisasjonsnummer'), STD_ANON_2, scope=CTD_ANON, location=pyxb.utils.utility.Location('xsd/integrasjonERFV_Vedtak.xsd', 22, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ERSaksstatus'), STD_ANON_3, scope=CTD_ANON, location=pyxb.utils.utility.Location('xsd/integrasjonERFV_Vedtak.xsd', 29, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FVSaksstatus'), STD_ANON_4, scope=CTD_ANON, location=pyxb.utils.utility.Location('xsd/integrasjonERFV_Vedtak.xsd', 36, 4)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SLsysId')), pyxb.utils.utility.Location('xsd/integrasjonERFV_Vedtak.xsd', 7, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SLsysMeldingsId')), pyxb.utils.utility.Location('xsd/integrasjonERFV_Vedtak.xsd', 14, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'organisasjonsnummer')), pyxb.utils.utility.Location('xsd/integrasjonERFV_Vedtak.xsd', 22, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ERSaksstatus')), pyxb.utils.utility.Location('xsd/integrasjonERFV_Vedtak.xsd', 29, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FVSaksstatus')), pyxb.utils.utility.Location('xsd/integrasjonERFV_Vedtak.xsd', 36, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()

