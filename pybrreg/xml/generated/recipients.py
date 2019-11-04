# ./recipients.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:c3674a9b44a4a4edf84a5ac08485c938ac789a94
# Generated 2016-08-10 10:55:46.153776 by PyXB version 1.2.4 using Python 2.7.5.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:3a0db804-5ed8-11e6-9e1c-eca86bfbeec6')

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
    """This type is the recipient list root element."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('xsd/Recipients.xsd', 8, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schema.altinn.no/services/ServiceEngine/Broker/2015/06}Recipient uses Python identifier Recipient
    __Recipient = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Recipient'), 'Recipient', '__httpschema_altinn_noservicesServiceEngineBroker201506_CTD_ANON_httpschema_altinn_noservicesServiceEngineBroker201506Recipient', True, pyxb.utils.utility.Location('xsd/Recipients.xsd', 13, 4), )

    
    Recipient = property(__Recipient.value, __Recipient.set, None, None)

    _ElementMap.update({
        __Recipient.name() : __Recipient
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """This property should hold information about a recipient."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('xsd/Recipients.xsd', 14, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schema.altinn.no/services/ServiceEngine/Broker/2015/06}PartyNumber uses Python identifier PartyNumber
    __PartyNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PartyNumber'), 'PartyNumber', '__httpschema_altinn_noservicesServiceEngineBroker201506_CTD_ANON__httpschema_altinn_noservicesServiceEngineBroker201506PartyNumber', False, pyxb.utils.utility.Location('xsd/Recipients.xsd', 19, 7), )

    
    PartyNumber = property(__PartyNumber.value, __PartyNumber.set, None, 'This property should be either an organization number or social security number.')

    _ElementMap.update({
        __PartyNumber.name() : __PartyNumber
    })
    _AttributeMap.update({
        
    })



BrokerServiceRecipientList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BrokerServiceRecipientList'), CTD_ANON, location=pyxb.utils.utility.Location('xsd/Recipients.xsd', 7, 1))
Namespace.addCategoryObject('elementBinding', BrokerServiceRecipientList.name().localName(), BrokerServiceRecipientList)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Recipient'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('xsd/Recipients.xsd', 13, 4)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Recipient')), pyxb.utils.utility.Location('xsd/Recipients.xsd', 13, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PartyNumber'), pyxb.binding.datatypes.string, scope=CTD_ANON_, documentation='This property should be either an organization number or social security number.', location=pyxb.utils.utility.Location('xsd/Recipients.xsd', 19, 7)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PartyNumber')), pyxb.utils.utility.Location('xsd/Recipients.xsd', 19, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()

