# ./applikasjonskvittering.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:21998ead96cc3ad9dda441739fdd5f491eef5dd5
# Generated 2019-04-03 12:11:37.852115 by PyXB version 1.2.4 using Python 2.7.15.final.0
# Namespace http://schema.brreg.no/postmottak/applikasjonskvittering

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:de1e2716-55f8-11e9-a732-c03fd5608144')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://schema.brreg.no/postmottak/applikasjonskvittering', create_if_missing=True)
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
    _XSDLocation = pyxb.utils.utility.Location('xsd/applikasjonskvittering.xsd', 10, 15)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.NotSet = STD_ANON._CF_enumeration.addEnumeration(unicode_value='NotSet', tag='NotSet')
STD_ANON.OK = STD_ANON._CF_enumeration.addEnumeration(unicode_value='OK', tag='OK')
STD_ANON.UnExpectedError = STD_ANON._CF_enumeration.addEnumeration(unicode_value='UnExpectedError', tag='UnExpectedError')
STD_ANON.ValidationFailed = STD_ANON._CF_enumeration.addEnumeration(unicode_value='ValidationFailed', tag='ValidationFailed')
STD_ANON.Rejected = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Rejected', tag='Rejected')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Beskriver kvittering som sendes til avsender"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('xsd/applikasjonskvittering.xsd', 7, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schema.brreg.no/postmottak/applikasjonskvittering}Status uses Python identifier Status
    __Status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Status'), 'Status', '__httpschema_brreg_nopostmottakapplikasjonskvittering_CTD_ANON_httpschema_brreg_nopostmottakapplikasjonskvitteringStatus', False, pyxb.utils.utility.Location('xsd/applikasjonskvittering.xsd', 9, 12), )

    
    Status = property(__Status.value, __Status.set, None, None)

    
    # Element {http://schema.brreg.no/postmottak/applikasjonskvittering}StatusTekst uses Python identifier StatusTekst
    __StatusTekst = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StatusTekst'), 'StatusTekst', '__httpschema_brreg_nopostmottakapplikasjonskvittering_CTD_ANON_httpschema_brreg_nopostmottakapplikasjonskvitteringStatusTekst', False, pyxb.utils.utility.Location('xsd/applikasjonskvittering.xsd', 20, 12), )

    
    StatusTekst = property(__StatusTekst.value, __StatusTekst.set, None, None)

    
    # Element {http://schema.brreg.no/postmottak/applikasjonskvittering}StatusKode uses Python identifier StatusKode
    __StatusKode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StatusKode'), 'StatusKode', '__httpschema_brreg_nopostmottakapplikasjonskvittering_CTD_ANON_httpschema_brreg_nopostmottakapplikasjonskvitteringStatusKode', False, pyxb.utils.utility.Location('xsd/applikasjonskvittering.xsd', 21, 12), )

    
    StatusKode = property(__StatusKode.value, __StatusKode.set, None, None)

    
    # Element {http://schema.brreg.no/postmottak/applikasjonskvittering}MeldingsReferanse uses Python identifier MeldingsReferanse
    __MeldingsReferanse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MeldingsReferanse'), 'MeldingsReferanse', '__httpschema_brreg_nopostmottakapplikasjonskvittering_CTD_ANON_httpschema_brreg_nopostmottakapplikasjonskvitteringMeldingsReferanse', False, pyxb.utils.utility.Location('xsd/applikasjonskvittering.xsd', 22, 12), )

    
    MeldingsReferanse = property(__MeldingsReferanse.value, __MeldingsReferanse.set, None, None)

    
    # Element {http://schema.brreg.no/postmottak/applikasjonskvittering}HenvendelsesReferanse uses Python identifier HenvendelsesReferanse
    __HenvendelsesReferanse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'HenvendelsesReferanse'), 'HenvendelsesReferanse', '__httpschema_brreg_nopostmottakapplikasjonskvittering_CTD_ANON_httpschema_brreg_nopostmottakapplikasjonskvitteringHenvendelsesReferanse', False, pyxb.utils.utility.Location('xsd/applikasjonskvittering.xsd', 23, 12), )

    
    HenvendelsesReferanse = property(__HenvendelsesReferanse.value, __HenvendelsesReferanse.set, None, None)

    
    # Element {http://schema.brreg.no/postmottak/applikasjonskvittering}AvsendersReferanse uses Python identifier AvsendersReferanse
    __AvsendersReferanse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AvsendersReferanse'), 'AvsendersReferanse', '__httpschema_brreg_nopostmottakapplikasjonskvittering_CTD_ANON_httpschema_brreg_nopostmottakapplikasjonskvitteringAvsendersReferanse', False, pyxb.utils.utility.Location('xsd/applikasjonskvittering.xsd', 24, 12), )

    
    AvsendersReferanse = property(__AvsendersReferanse.value, __AvsendersReferanse.set, None, None)

    _ElementMap.update({
        __Status.name() : __Status,
        __StatusTekst.name() : __StatusTekst,
        __StatusKode.name() : __StatusKode,
        __MeldingsReferanse.name() : __MeldingsReferanse,
        __HenvendelsesReferanse.name() : __HenvendelsesReferanse,
        __AvsendersReferanse.name() : __AvsendersReferanse
    })
    _AttributeMap.update({
        
    })



Applikasjonskvittering = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Applikasjonskvittering'), CTD_ANON, documentation='Beskriver kvittering som sendes til avsender', location=pyxb.utils.utility.Location('xsd/applikasjonskvittering.xsd', 3, 3))
Namespace.addCategoryObject('elementBinding', Applikasjonskvittering.name().localName(), Applikasjonskvittering)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Status'), STD_ANON, scope=CTD_ANON, location=pyxb.utils.utility.Location('xsd/applikasjonskvittering.xsd', 9, 12)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StatusTekst'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('xsd/applikasjonskvittering.xsd', 20, 12)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StatusKode'), pyxb.binding.datatypes.int, scope=CTD_ANON, location=pyxb.utils.utility.Location('xsd/applikasjonskvittering.xsd', 21, 12)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MeldingsReferanse'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('xsd/applikasjonskvittering.xsd', 22, 12)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'HenvendelsesReferanse'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('xsd/applikasjonskvittering.xsd', 23, 12)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AvsendersReferanse'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('xsd/applikasjonskvittering.xsd', 24, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('xsd/applikasjonskvittering.xsd', 23, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('xsd/applikasjonskvittering.xsd', 24, 12))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Status')), pyxb.utils.utility.Location('xsd/applikasjonskvittering.xsd', 9, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StatusTekst')), pyxb.utils.utility.Location('xsd/applikasjonskvittering.xsd', 20, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StatusKode')), pyxb.utils.utility.Location('xsd/applikasjonskvittering.xsd', 21, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MeldingsReferanse')), pyxb.utils.utility.Location('xsd/applikasjonskvittering.xsd', 22, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'HenvendelsesReferanse')), pyxb.utils.utility.Location('xsd/applikasjonskvittering.xsd', 23, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AvsendersReferanse')), pyxb.utils.utility.Location('xsd/applikasjonskvittering.xsd', 24, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()

