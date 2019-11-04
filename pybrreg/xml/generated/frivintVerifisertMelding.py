# ./frivintVerifisertMelding.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:325aba29c5a264440aef6aefcfffe72c7e79ceed
# Generated 2016-06-20 16:07:34.832697 by PyXB version 1.2.4 using Python 2.7.5.final.0
# Namespace http://schema.brreg.no/postmottak/frivintVerifisertMelding

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:563a1802-36f0-11e6-b3c8-eca86bfbeec6')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://schema.brreg.no/postmottak/frivintVerifisertMelding', create_if_missing=True)
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
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('xsd/frivintVerifisertMelding.xsd', 39, 5)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.SHA_256 = STD_ANON._CF_enumeration.addEnumeration(unicode_value='SHA-256', tag='SHA_256')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('xsd/frivintVerifisertMelding.xsd', 52, 5)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.SHA_512 = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='SHA-512', tag='SHA_512')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('xsd/frivintVerifisertMelding.xsd', 4, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schema.brreg.no/postmottak/frivintVerifisertMelding}SignedObject uses Python identifier SignedObject
    __SignedObject = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SignedObject'), 'SignedObject', '__httpschema_brreg_nopostmottakfrivintVerifisertMelding_CTD_ANON_httpschema_brreg_nopostmottakfrivintVerifisertMeldingSignedObject', False, pyxb.utils.utility.Location('xsd/frivintVerifisertMelding.xsd', 6, 4), )

    
    SignedObject = property(__SignedObject.value, __SignedObject.set, None, 'Base64-encoded content')

    
    # Element {http://schema.brreg.no/postmottak/frivintVerifisertMelding}Signatures uses Python identifier Signatures
    __Signatures = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Signatures'), 'Signatures', '__httpschema_brreg_nopostmottakfrivintVerifisertMelding_CTD_ANON_httpschema_brreg_nopostmottakfrivintVerifisertMeldingSignatures', False, pyxb.utils.utility.Location('xsd/frivintVerifisertMelding.xsd', 11, 4), )

    
    Signatures = property(__Signatures.value, __Signatures.set, None, None)

    _ElementMap.update({
        __SignedObject.name() : __SignedObject,
        __Signatures.name() : __Signatures
    })
    _AttributeMap.update({
        
    })



# Complex type {http://schema.brreg.no/postmottak/frivintVerifisertMelding}Signatures with content type ELEMENT_ONLY
class Signatures (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://schema.brreg.no/postmottak/frivintVerifisertMelding}Signatures with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Signatures')
    _XSDLocation = pyxb.utils.utility.Location('xsd/frivintVerifisertMelding.xsd', 15, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schema.brreg.no/postmottak/frivintVerifisertMelding}SignatureRecord uses Python identifier SignatureRecord
    __SignatureRecord = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SignatureRecord'), 'SignatureRecord', '__httpschema_brreg_nopostmottakfrivintVerifisertMelding_Signatures_httpschema_brreg_nopostmottakfrivintVerifisertMeldingSignatureRecord', True, pyxb.utils.utility.Location('xsd/frivintVerifisertMelding.xsd', 17, 3), )

    
    SignatureRecord = property(__SignatureRecord.value, __SignatureRecord.set, None, None)

    _ElementMap.update({
        __SignatureRecord.name() : __SignatureRecord
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'Signatures', Signatures)


# Complex type {http://schema.brreg.no/postmottak/frivintVerifisertMelding}SignatureRecord with content type ELEMENT_ONLY
class SignatureRecord (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://schema.brreg.no/postmottak/frivintVerifisertMelding}SignatureRecord with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SignatureRecord')
    _XSDLocation = pyxb.utils.utility.Location('xsd/frivintVerifisertMelding.xsd', 20, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schema.brreg.no/postmottak/frivintVerifisertMelding}SignedObjectHash uses Python identifier SignedObjectHash
    __SignedObjectHash = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SignedObjectHash'), 'SignedObjectHash', '__httpschema_brreg_nopostmottakfrivintVerifisertMelding_SignatureRecord_httpschema_brreg_nopostmottakfrivintVerifisertMeldingSignedObjectHash', False, pyxb.utils.utility.Location('xsd/frivintVerifisertMelding.xsd', 22, 3), )

    
    SignedObjectHash = property(__SignedObjectHash.value, __SignedObjectHash.set, None, None)

    
    # Element {http://schema.brreg.no/postmottak/frivintVerifisertMelding}Authentication uses Python identifier Authentication
    __Authentication = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Authentication'), 'Authentication', '__httpschema_brreg_nopostmottakfrivintVerifisertMelding_SignatureRecord_httpschema_brreg_nopostmottakfrivintVerifisertMeldingAuthentication', False, pyxb.utils.utility.Location('xsd/frivintVerifisertMelding.xsd', 23, 3), )

    
    Authentication = property(__Authentication.value, __Authentication.set, None, 'Base64-encoded signed SAML assertion')

    
    # Element {http://schema.brreg.no/postmottak/frivintVerifisertMelding}RecordSeal uses Python identifier RecordSeal
    __RecordSeal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RecordSeal'), 'RecordSeal', '__httpschema_brreg_nopostmottakfrivintVerifisertMelding_SignatureRecord_httpschema_brreg_nopostmottakfrivintVerifisertMeldingRecordSeal', False, pyxb.utils.utility.Location('xsd/frivintVerifisertMelding.xsd', 28, 3), )

    
    RecordSeal = property(__RecordSeal.value, __RecordSeal.set, None, 'Hash of SignedObjectHash, Authentication and pre-shared key')

    _ElementMap.update({
        __SignedObjectHash.name() : __SignedObjectHash,
        __Authentication.name() : __Authentication,
        __RecordSeal.name() : __RecordSeal
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'SignatureRecord', SignatureRecord)


# Complex type {http://schema.brreg.no/postmottak/frivintVerifisertMelding}SignedObjectHash with content type SIMPLE
class SignedObjectHash (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://schema.brreg.no/postmottak/frivintVerifisertMelding}SignedObjectHash with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SignedObjectHash')
    _XSDLocation = pyxb.utils.utility.Location('xsd/frivintVerifisertMelding.xsd', 35, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute algorithm uses Python identifier algorithm
    __algorithm = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'algorithm'), 'algorithm', '__httpschema_brreg_nopostmottakfrivintVerifisertMelding_SignedObjectHash_algorithm', STD_ANON, required=True)
    __algorithm._DeclarationLocation = pyxb.utils.utility.Location('xsd/frivintVerifisertMelding.xsd', 38, 4)
    __algorithm._UseLocation = pyxb.utils.utility.Location('xsd/frivintVerifisertMelding.xsd', 38, 4)
    
    algorithm = property(__algorithm.value, __algorithm.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __algorithm.name() : __algorithm
    })
Namespace.addCategoryObject('typeBinding', 'SignedObjectHash', SignedObjectHash)


# Complex type {http://schema.brreg.no/postmottak/frivintVerifisertMelding}RecordSeal with content type SIMPLE
class RecordSeal (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://schema.brreg.no/postmottak/frivintVerifisertMelding}RecordSeal with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RecordSeal')
    _XSDLocation = pyxb.utils.utility.Location('xsd/frivintVerifisertMelding.xsd', 48, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute algorithm uses Python identifier algorithm
    __algorithm = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'algorithm'), 'algorithm', '__httpschema_brreg_nopostmottakfrivintVerifisertMelding_RecordSeal_algorithm', STD_ANON_, required=True)
    __algorithm._DeclarationLocation = pyxb.utils.utility.Location('xsd/frivintVerifisertMelding.xsd', 51, 4)
    __algorithm._UseLocation = pyxb.utils.utility.Location('xsd/frivintVerifisertMelding.xsd', 51, 4)
    
    algorithm = property(__algorithm.value, __algorithm.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __algorithm.name() : __algorithm
    })
Namespace.addCategoryObject('typeBinding', 'RecordSeal', RecordSeal)


SDO = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SDO'), CTD_ANON, location=pyxb.utils.utility.Location('xsd/frivintVerifisertMelding.xsd', 3, 1))
Namespace.addCategoryObject('elementBinding', SDO.name().localName(), SDO)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SignedObject'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation='Base64-encoded content', location=pyxb.utils.utility.Location('xsd/frivintVerifisertMelding.xsd', 6, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Signatures'), Signatures, scope=CTD_ANON, location=pyxb.utils.utility.Location('xsd/frivintVerifisertMelding.xsd', 11, 4)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SignedObject')), pyxb.utils.utility.Location('xsd/frivintVerifisertMelding.xsd', 6, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Signatures')), pyxb.utils.utility.Location('xsd/frivintVerifisertMelding.xsd', 11, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




Signatures._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SignatureRecord'), SignatureRecord, scope=Signatures, location=pyxb.utils.utility.Location('xsd/frivintVerifisertMelding.xsd', 17, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Signatures._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SignatureRecord')), pyxb.utils.utility.Location('xsd/frivintVerifisertMelding.xsd', 17, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Signatures._Automaton = _BuildAutomaton_()




SignatureRecord._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SignedObjectHash'), SignedObjectHash, scope=SignatureRecord, location=pyxb.utils.utility.Location('xsd/frivintVerifisertMelding.xsd', 22, 3)))

SignatureRecord._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Authentication'), pyxb.binding.datatypes.string, scope=SignatureRecord, documentation='Base64-encoded signed SAML assertion', location=pyxb.utils.utility.Location('xsd/frivintVerifisertMelding.xsd', 23, 3)))

SignatureRecord._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RecordSeal'), RecordSeal, scope=SignatureRecord, documentation='Hash of SignedObjectHash, Authentication and pre-shared key', location=pyxb.utils.utility.Location('xsd/frivintVerifisertMelding.xsd', 28, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SignatureRecord._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SignedObjectHash')), pyxb.utils.utility.Location('xsd/frivintVerifisertMelding.xsd', 22, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SignatureRecord._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Authentication')), pyxb.utils.utility.Location('xsd/frivintVerifisertMelding.xsd', 23, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SignatureRecord._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RecordSeal')), pyxb.utils.utility.Location('xsd/frivintVerifisertMelding.xsd', 28, 3))
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
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SignatureRecord._Automaton = _BuildAutomaton_2()

