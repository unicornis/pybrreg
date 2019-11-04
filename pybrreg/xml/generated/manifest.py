# ./manifest.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:c3674a9b44a4a4edf84a5ac08485c938ac789a94
# Generated 2016-08-10 10:54:40.034890 by PyXB version 1.2.4 using Python 2.7.5.final.0
# Namespace http://schema.altinn.no/services/ServiceEngine/Broker/2015/06

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:129fbad8-5ed8-11e6-af5b-eca86bfbeec6')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://schema.altinn.no/services/ServiceEngine/Broker/2015/06', create_if_missing=True)
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


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """This type is the manifest root element. The container of all the file meta-data."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('xsd/Manifest.xsd', 8, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schema.altinn.no/services/ServiceEngine/Broker/2015/06}ExternalServiceCode uses Python identifier ExternalServiceCode
    __ExternalServiceCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExternalServiceCode'), 'ExternalServiceCode', '__httpschema_altinn_noservicesServiceEngineBroker201506_CTD_ANON_httpschema_altinn_noservicesServiceEngineBroker201506ExternalServiceCode', False, pyxb.utils.utility.Location('xsd/Manifest.xsd', 13, 4), )

    
    ExternalServiceCode = property(__ExternalServiceCode.value, __ExternalServiceCode.set, None, 'This property should hold the service code of the BrokerService being used. Value is required.')

    
    # Element {http://schema.altinn.no/services/ServiceEngine/Broker/2015/06}ExternalServiceEditionCode uses Python identifier ExternalServiceEditionCode
    __ExternalServiceEditionCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExternalServiceEditionCode'), 'ExternalServiceEditionCode', '__httpschema_altinn_noservicesServiceEngineBroker201506_CTD_ANON_httpschema_altinn_noservicesServiceEngineBroker201506ExternalServiceEditionCode', False, pyxb.utils.utility.Location('xsd/Manifest.xsd', 18, 4), )

    
    ExternalServiceEditionCode = property(__ExternalServiceEditionCode.value, __ExternalServiceEditionCode.set, None, 'This property should hold the service edition code of the BrokerService being used. Value is required.')

    
    # Element {http://schema.altinn.no/services/ServiceEngine/Broker/2015/06}SendersReference uses Python identifier SendersReference
    __SendersReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SendersReference'), 'SendersReference', '__httpschema_altinn_noservicesServiceEngineBroker201506_CTD_ANON_httpschema_altinn_noservicesServiceEngineBroker201506SendersReference', False, pyxb.utils.utility.Location('xsd/Manifest.xsd', 23, 4), )

    
    SendersReference = property(__SendersReference.value, __SendersReference.set, None, 'This property should hold a reference value defined by the file creator. Value is required.')

    
    # Element {http://schema.altinn.no/services/ServiceEngine/Broker/2015/06}Reportee uses Python identifier Reportee
    __Reportee = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Reportee'), 'Reportee', '__httpschema_altinn_noservicesServiceEngineBroker201506_CTD_ANON_httpschema_altinn_noservicesServiceEngineBroker201506Reportee', False, pyxb.utils.utility.Location('xsd/Manifest.xsd', 28, 4), )

    
    Reportee = property(__Reportee.value, __Reportee.set, None, 'This property will hold the organization number or social security number of the file source. Value is required.')

    
    # Element {http://schema.altinn.no/services/ServiceEngine/Broker/2015/06}SentDate uses Python identifier SentDate
    __SentDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SentDate'), 'SentDate', '__httpschema_altinn_noservicesServiceEngineBroker201506_CTD_ANON_httpschema_altinn_noservicesServiceEngineBroker201506SentDate', False, pyxb.utils.utility.Location('xsd/Manifest.xsd', 33, 4), )

    
    SentDate = property(__SentDate.value, __SentDate.set, None, 'This property will hold the date and time for when the file was received in Altinn. Property value is added by Altinn.')

    
    # Element {http://schema.altinn.no/services/ServiceEngine/Broker/2015/06}FileList uses Python identifier FileList
    __FileList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FileList'), 'FileList', '__httpschema_altinn_noservicesServiceEngineBroker201506_CTD_ANON_httpschema_altinn_noservicesServiceEngineBroker201506FileList', False, pyxb.utils.utility.Location('xsd/Manifest.xsd', 38, 4), )

    
    FileList = property(__FileList.value, __FileList.set, None, None)

    
    # Element {http://schema.altinn.no/services/ServiceEngine/Broker/2015/06}PropertyList uses Python identifier PropertyList
    __PropertyList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PropertyList'), 'PropertyList', '__httpschema_altinn_noservicesServiceEngineBroker201506_CTD_ANON_httpschema_altinn_noservicesServiceEngineBroker201506PropertyList', False, pyxb.utils.utility.Location('xsd/Manifest.xsd', 66, 4), )

    
    PropertyList = property(__PropertyList.value, __PropertyList.set, None, None)

    _ElementMap.update({
        __ExternalServiceCode.name() : __ExternalServiceCode,
        __ExternalServiceEditionCode.name() : __ExternalServiceEditionCode,
        __SendersReference.name() : __SendersReference,
        __Reportee.name() : __Reportee,
        __SentDate.name() : __SentDate,
        __FileList.name() : __FileList,
        __PropertyList.name() : __PropertyList
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """This property should hold a list of the files included in the shipment. This is optional."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('xsd/Manifest.xsd', 39, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schema.altinn.no/services/ServiceEngine/Broker/2015/06}File uses Python identifier File
    __File = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'File'), 'File', '__httpschema_altinn_noservicesServiceEngineBroker201506_CTD_ANON__httpschema_altinn_noservicesServiceEngineBroker201506File', True, pyxb.utils.utility.Location('xsd/Manifest.xsd', 44, 7), )

    
    File = property(__File.value, __File.set, None, None)

    _ElementMap.update({
        __File.name() : __File
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """This property should hold information about a file in the package."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('xsd/Manifest.xsd', 45, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schema.altinn.no/services/ServiceEngine/Broker/2015/06}FileName uses Python identifier FileName
    __FileName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FileName'), 'FileName', '__httpschema_altinn_noservicesServiceEngineBroker201506_CTD_ANON_2_httpschema_altinn_noservicesServiceEngineBroker201506FileName', False, pyxb.utils.utility.Location('xsd/Manifest.xsd', 50, 10), )

    
    FileName = property(__FileName.value, __FileName.set, None, 'This property should hold the name of the file.')

    
    # Element {http://schema.altinn.no/services/ServiceEngine/Broker/2015/06}CheckSum uses Python identifier CheckSum
    __CheckSum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CheckSum'), 'CheckSum', '__httpschema_altinn_noservicesServiceEngineBroker201506_CTD_ANON_2_httpschema_altinn_noservicesServiceEngineBroker201506CheckSum', False, pyxb.utils.utility.Location('xsd/Manifest.xsd', 55, 10), )

    
    CheckSum = property(__CheckSum.value, __CheckSum.set, None, 'This property should hold the checksum of the file.')

    _ElementMap.update({
        __FileName.name() : __FileName,
        __CheckSum.name() : __CheckSum
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """This property can hold a list of custom values agreed upon between sender and receivers. This is optional."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('xsd/Manifest.xsd', 67, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schema.altinn.no/services/ServiceEngine/Broker/2015/06}Property uses Python identifier Property
    __Property = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Property'), 'Property', '__httpschema_altinn_noservicesServiceEngineBroker201506_CTD_ANON_3_httpschema_altinn_noservicesServiceEngineBroker201506Property', True, pyxb.utils.utility.Location('xsd/Manifest.xsd', 72, 7), )

    
    Property = property(__Property.value, __Property.set, None, None)

    _ElementMap.update({
        __Property.name() : __Property
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('xsd/Manifest.xsd', 73, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schema.altinn.no/services/ServiceEngine/Broker/2015/06}PropertyKey uses Python identifier PropertyKey
    __PropertyKey = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PropertyKey'), 'PropertyKey', '__httpschema_altinn_noservicesServiceEngineBroker201506_CTD_ANON_4_httpschema_altinn_noservicesServiceEngineBroker201506PropertyKey', False, pyxb.utils.utility.Location('xsd/Manifest.xsd', 75, 10), )

    
    PropertyKey = property(__PropertyKey.value, __PropertyKey.set, None, None)

    
    # Element {http://schema.altinn.no/services/ServiceEngine/Broker/2015/06}PropertyValue uses Python identifier PropertyValue
    __PropertyValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PropertyValue'), 'PropertyValue', '__httpschema_altinn_noservicesServiceEngineBroker201506_CTD_ANON_4_httpschema_altinn_noservicesServiceEngineBroker201506PropertyValue', False, pyxb.utils.utility.Location('xsd/Manifest.xsd', 76, 10), )

    
    PropertyValue = property(__PropertyValue.value, __PropertyValue.set, None, None)

    _ElementMap.update({
        __PropertyKey.name() : __PropertyKey,
        __PropertyValue.name() : __PropertyValue
    })
    _AttributeMap.update({
        
    })



BrokerServiceManifest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BrokerServiceManifest'), CTD_ANON, location=pyxb.utils.utility.Location('xsd/Manifest.xsd', 7, 1))
Namespace.addCategoryObject('elementBinding', BrokerServiceManifest.name().localName(), BrokerServiceManifest)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExternalServiceCode'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation='This property should hold the service code of the BrokerService being used. Value is required.', location=pyxb.utils.utility.Location('xsd/Manifest.xsd', 13, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExternalServiceEditionCode'), pyxb.binding.datatypes.integer, scope=CTD_ANON, documentation='This property should hold the service edition code of the BrokerService being used. Value is required.', location=pyxb.utils.utility.Location('xsd/Manifest.xsd', 18, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SendersReference'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation='This property should hold a reference value defined by the file creator. Value is required.', location=pyxb.utils.utility.Location('xsd/Manifest.xsd', 23, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Reportee'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation='This property will hold the organization number or social security number of the file source. Value is required.', location=pyxb.utils.utility.Location('xsd/Manifest.xsd', 28, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SentDate'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON, documentation='This property will hold the date and time for when the file was received in Altinn. Property value is added by Altinn.', location=pyxb.utils.utility.Location('xsd/Manifest.xsd', 33, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FileList'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('xsd/Manifest.xsd', 38, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropertyList'), CTD_ANON_3, scope=CTD_ANON, location=pyxb.utils.utility.Location('xsd/Manifest.xsd', 66, 4)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('xsd/Manifest.xsd', 33, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('xsd/Manifest.xsd', 38, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('xsd/Manifest.xsd', 66, 4))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExternalServiceCode')), pyxb.utils.utility.Location('xsd/Manifest.xsd', 13, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExternalServiceEditionCode')), pyxb.utils.utility.Location('xsd/Manifest.xsd', 18, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SendersReference')), pyxb.utils.utility.Location('xsd/Manifest.xsd', 23, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Reportee')), pyxb.utils.utility.Location('xsd/Manifest.xsd', 28, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SentDate')), pyxb.utils.utility.Location('xsd/Manifest.xsd', 33, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FileList')), pyxb.utils.utility.Location('xsd/Manifest.xsd', 38, 4))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PropertyList')), pyxb.utils.utility.Location('xsd/Manifest.xsd', 66, 4))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
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
    transitions.append(fac.Transition(st_6, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'File'), CTD_ANON_2, scope=CTD_ANON_, location=pyxb.utils.utility.Location('xsd/Manifest.xsd', 44, 7)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('xsd/Manifest.xsd', 44, 7))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'File')), pyxb.utils.utility.Location('xsd/Manifest.xsd', 44, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FileName'), pyxb.binding.datatypes.string, scope=CTD_ANON_2, documentation='This property should hold the name of the file.', location=pyxb.utils.utility.Location('xsd/Manifest.xsd', 50, 10)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CheckSum'), pyxb.binding.datatypes.string, scope=CTD_ANON_2, documentation='This property should hold the checksum of the file.', location=pyxb.utils.utility.Location('xsd/Manifest.xsd', 55, 10)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('xsd/Manifest.xsd', 55, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FileName')), pyxb.utils.utility.Location('xsd/Manifest.xsd', 50, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CheckSum')), pyxb.utils.utility.Location('xsd/Manifest.xsd', 55, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Property'), CTD_ANON_4, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('xsd/Manifest.xsd', 72, 7)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('xsd/Manifest.xsd', 72, 7))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Property')), pyxb.utils.utility.Location('xsd/Manifest.xsd', 72, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_3()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropertyKey'), pyxb.binding.datatypes.string, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('xsd/Manifest.xsd', 75, 10)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropertyValue'), pyxb.binding.datatypes.string, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('xsd/Manifest.xsd', 76, 10)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PropertyKey')), pyxb.utils.utility.Location('xsd/Manifest.xsd', 75, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PropertyValue')), pyxb.utils.utility.Location('xsd/Manifest.xsd', 76, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_4()

