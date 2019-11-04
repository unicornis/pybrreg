# ./hentRoller.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2017-06-08 13:29:31.256552 by PyXB version 1.2.4 using Python 2.7.10.final.0
# Namespace AbsentNamespace0

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:bd560830-4c3d-11e7-ad9f-600308a51954')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
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
class STD_ANON (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 34, 28)
    _Documentation = None
STD_ANON._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40))
STD_ANON._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON._InitializeFacetMap(STD_ANON._CF_maxLength,
   STD_ANON._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 124, 56)
    _Documentation = None
STD_ANON_._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(11))
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_length)

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 131, 56)
    _Documentation = None
STD_ANON_2._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(10))
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_length)

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 139, 52)
    _Documentation = None
STD_ANON_3._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50))
STD_ANON_3._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_maxLength,
   STD_ANON_3._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 147, 52)
    _Documentation = None
STD_ANON_4._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50))
STD_ANON_4._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_maxLength,
   STD_ANON_4._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_5 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 155, 52)
    _Documentation = None
STD_ANON_5._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50))
STD_ANON_5._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_5._InitializeFacetMap(STD_ANON_5._CF_maxLength,
   STD_ANON_5._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_6 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 163, 52)
    _Documentation = None
STD_ANON_6._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
STD_ANON_6._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_6._InitializeFacetMap(STD_ANON_6._CF_maxLength,
   STD_ANON_6._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_7 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 171, 52)
    _Documentation = None
STD_ANON_7._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
STD_ANON_7._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_7._InitializeFacetMap(STD_ANON_7._CF_maxLength,
   STD_ANON_7._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_8 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 179, 52)
    _Documentation = None
STD_ANON_8._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
STD_ANON_8._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_8._InitializeFacetMap(STD_ANON_8._CF_maxLength,
   STD_ANON_8._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_9 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 187, 52)
    _Documentation = None
STD_ANON_9._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(9))
STD_ANON_9._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
STD_ANON_9._InitializeFacetMap(STD_ANON_9._CF_maxLength,
   STD_ANON_9._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_10 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 195, 52)
    _Documentation = None
STD_ANON_10._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
STD_ANON_10._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_10._InitializeFacetMap(STD_ANON_10._CF_maxLength,
   STD_ANON_10._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_11 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 225, 52)
    _Documentation = None
STD_ANON_11._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_11._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_11, enum_prefix=None)
STD_ANON_11.K = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='K', tag='K')
STD_ANON_11.R = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='R', tag='R')
STD_ANON_11.F = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='F', tag='F')
STD_ANON_11.N = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='N', tag='N')
STD_ANON_11._InitializeFacetMap(STD_ANON_11._CF_length,
   STD_ANON_11._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_12 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 236, 52)
    _Documentation = None
STD_ANON_12._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(8))
STD_ANON_12._InitializeFacetMap(STD_ANON_12._CF_length)

# Atomic simple type: [anonymous]
class STD_ANON_13 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 255, 52)
    _Documentation = None
STD_ANON_13._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(9))
STD_ANON_13._InitializeFacetMap(STD_ANON_13._CF_length)

# Atomic simple type: [anonymous]
class STD_ANON_14 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 262, 52)
    _Documentation = None
STD_ANON_14._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
STD_ANON_14._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_14._InitializeFacetMap(STD_ANON_14._CF_maxLength,
   STD_ANON_14._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_15 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 270, 52)
    _Documentation = None
STD_ANON_15._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
STD_ANON_15._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_15._InitializeFacetMap(STD_ANON_15._CF_maxLength,
   STD_ANON_15._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_16 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 278, 52)
    _Documentation = None
STD_ANON_16._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
STD_ANON_16._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_16._InitializeFacetMap(STD_ANON_16._CF_maxLength,
   STD_ANON_16._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_17 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 286, 52)
    _Documentation = None
STD_ANON_17._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
STD_ANON_17._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_17._InitializeFacetMap(STD_ANON_17._CF_maxLength,
   STD_ANON_17._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_18 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 294, 52)
    _Documentation = None
STD_ANON_18._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
STD_ANON_18._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_18._InitializeFacetMap(STD_ANON_18._CF_maxLength,
   STD_ANON_18._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_19 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 302, 52)
    _Documentation = None
STD_ANON_19._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
STD_ANON_19._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_19._InitializeFacetMap(STD_ANON_19._CF_maxLength,
   STD_ANON_19._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_20 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 310, 52)
    _Documentation = None
STD_ANON_20._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
STD_ANON_20._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_20._InitializeFacetMap(STD_ANON_20._CF_maxLength,
   STD_ANON_20._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_21 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 318, 52)
    _Documentation = None
STD_ANON_21._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
STD_ANON_21._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_21._InitializeFacetMap(STD_ANON_21._CF_maxLength,
   STD_ANON_21._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_22 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 326, 52)
    _Documentation = None
STD_ANON_22._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(9))
STD_ANON_22._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
STD_ANON_22._InitializeFacetMap(STD_ANON_22._CF_maxLength,
   STD_ANON_22._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_23 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 334, 52)
    _Documentation = None
STD_ANON_23._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
STD_ANON_23._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_23._InitializeFacetMap(STD_ANON_23._CF_maxLength,
   STD_ANON_23._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_24 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 364, 52)
    _Documentation = None
STD_ANON_24._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_24._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_24, enum_prefix=None)
STD_ANON_24.K = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='K', tag='K')
STD_ANON_24.R = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='R', tag='R')
STD_ANON_24.F = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='F', tag='F')
STD_ANON_24.N = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='N', tag='N')
STD_ANON_24._InitializeFacetMap(STD_ANON_24._CF_length,
   STD_ANON_24._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_25 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 375, 52)
    _Documentation = None
STD_ANON_25._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(8))
STD_ANON_25._InitializeFacetMap(STD_ANON_25._CF_length)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Bekskriver tjenesten hentRoller"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 9, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element responseHeader uses Python identifier responseHeader
    __responseHeader = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'responseHeader'), 'responseHeader', '__AbsentNamespace0_CTD_ANON_responseHeader', False, pyxb.utils.utility.Location('hentRoller.xsd', 11, 16), )

    
    responseHeader = property(__responseHeader.value, __responseHeader.set, None, None)

    
    # Element melding uses Python identifier melding
    __melding = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'melding'), 'melding', '__AbsentNamespace0_CTD_ANON_melding', False, pyxb.utils.utility.Location('hentRoller.xsd', 43, 16), )

    
    melding = property(__melding.value, __melding.set, None, None)

    _ElementMap.update({
        __responseHeader.name() : __responseHeader,
        __melding.name() : __melding
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 17, 32)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element underStatusMelding uses Python identifier underStatusMelding
    __underStatusMelding = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'underStatusMelding'), 'underStatusMelding', '__AbsentNamespace0_CTD_ANON__underStatusMelding', True, pyxb.utils.utility.Location('hentRoller.xsd', 19, 40), )

    
    underStatusMelding = property(__underStatusMelding.value, __underStatusMelding.set, None, None)

    _ElementMap.update({
        __underStatusMelding.name() : __underStatusMelding
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 20, 44)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute kode uses Python identifier kode
    __kode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kode'), 'kode', '__AbsentNamespace0_CTD_ANON_2_kode', pyxb.binding.datatypes.int, required=True)
    __kode._DeclarationLocation = pyxb.utils.utility.Location('hentRoller.xsd', 23, 56)
    __kode._UseLocation = pyxb.utils.utility.Location('hentRoller.xsd', 23, 56)
    
    kode = property(__kode.value, __kode.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __kode.name() : __kode
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 44, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element organisasjonsnummer uses Python identifier organisasjonsnummer
    __organisasjonsnummer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'organisasjonsnummer'), 'organisasjonsnummer', '__AbsentNamespace0_CTD_ANON_3_organisasjonsnummer', False, pyxb.utils.utility.Location('hentRoller.xsd', 46, 28), )

    
    organisasjonsnummer = property(__organisasjonsnummer.value, __organisasjonsnummer.set, None, None)

    
    # Element kontaktperson uses Python identifier kontaktperson
    __kontaktperson = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'kontaktperson'), 'kontaktperson', '__AbsentNamespace0_CTD_ANON_3_kontaktperson', False, pyxb.utils.utility.Location('hentRoller.xsd', 55, 28), )

    
    kontaktperson = property(__kontaktperson.value, __kontaktperson.set, None, None)

    
    # Element deltakere uses Python identifier deltakere
    __deltakere = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'deltakere'), 'deltakere', '__AbsentNamespace0_CTD_ANON_3_deltakere', False, pyxb.utils.utility.Location('hentRoller.xsd', 60, 28), )

    
    deltakere = property(__deltakere.value, __deltakere.set, None, None)

    
    # Element komplementar uses Python identifier komplementar
    __komplementar = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'komplementar'), 'komplementar', '__AbsentNamespace0_CTD_ANON_3_komplementar', False, pyxb.utils.utility.Location('hentRoller.xsd', 65, 28), )

    
    komplementar = property(__komplementar.value, __komplementar.set, None, None)

    
    # Element sameiere uses Python identifier sameiere
    __sameiere = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sameiere'), 'sameiere', '__AbsentNamespace0_CTD_ANON_3_sameiere', False, pyxb.utils.utility.Location('hentRoller.xsd', 70, 28), )

    
    sameiere = property(__sameiere.value, __sameiere.set, None, None)

    
    # Element styre uses Python identifier styre
    __styre = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'styre'), 'styre', '__AbsentNamespace0_CTD_ANON_3_styre', False, pyxb.utils.utility.Location('hentRoller.xsd', 75, 28), )

    
    styre = property(__styre.value, __styre.set, None, None)

    
    # Element revisor uses Python identifier revisor
    __revisor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'revisor'), 'revisor', '__AbsentNamespace0_CTD_ANON_3_revisor', False, pyxb.utils.utility.Location('hentRoller.xsd', 80, 28), )

    
    revisor = property(__revisor.value, __revisor.set, None, None)

    
    # Element regnskapsfoerer uses Python identifier regnskapsfoerer
    __regnskapsfoerer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'regnskapsfoerer'), 'regnskapsfoerer', '__AbsentNamespace0_CTD_ANON_3_regnskapsfoerer', False, pyxb.utils.utility.Location('hentRoller.xsd', 85, 28), )

    
    regnskapsfoerer = property(__regnskapsfoerer.value, __regnskapsfoerer.set, None, None)

    
    # Element eierkommune uses Python identifier eierkommune
    __eierkommune = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'eierkommune'), 'eierkommune', '__AbsentNamespace0_CTD_ANON_3_eierkommune', False, pyxb.utils.utility.Location('hentRoller.xsd', 90, 28), )

    
    eierkommune = property(__eierkommune.value, __eierkommune.set, None, None)

    
    # Attribute tjeneste uses Python identifier tjeneste
    __tjeneste = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tjeneste'), 'tjeneste', '__AbsentNamespace0_CTD_ANON_3_tjeneste', pyxb.binding.datatypes.string, required=True)
    __tjeneste._DeclarationLocation = pyxb.utils.utility.Location('hentRoller.xsd', 96, 24)
    __tjeneste._UseLocation = pyxb.utils.utility.Location('hentRoller.xsd', 96, 24)
    
    tjeneste = property(__tjeneste.value, __tjeneste.set, None, None)

    _ElementMap.update({
        __organisasjonsnummer.name() : __organisasjonsnummer,
        __kontaktperson.name() : __kontaktperson,
        __deltakere.name() : __deltakere,
        __komplementar.name() : __komplementar,
        __sameiere.name() : __sameiere,
        __styre.name() : __styre,
        __revisor.name() : __revisor,
        __regnskapsfoerer.name() : __regnskapsfoerer,
        __eierkommune.name() : __eierkommune
    })
    _AttributeMap.update({
        __tjeneste.name() : __tjeneste
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 47, 32)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute registreringsDato uses Python identifier registreringsDato
    __registreringsDato = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'registreringsDato'), 'registreringsDato', '__AbsentNamespace0_CTD_ANON_4_registreringsDato', pyxb.binding.datatypes.date, required=True)
    __registreringsDato._DeclarationLocation = pyxb.utils.utility.Location('hentRoller.xsd', 50, 44)
    __registreringsDato._UseLocation = pyxb.utils.utility.Location('hentRoller.xsd', 50, 44)
    
    registreringsDato = property(__registreringsDato.value, __registreringsDato.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __registreringsDato.name() : __registreringsDato
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 56, 32)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element samendring uses Python identifier samendring
    __samendring = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'samendring'), 'samendring', '__AbsentNamespace0_CTD_ANON_5_samendring', True, pyxb.utils.utility.Location('hentRoller.xsd', 107, 12), )

    
    samendring = property(__samendring.value, __samendring.set, None, 'Samendring (SAMtidig ENDRING): Samling av roller som h\xc3\xb8rer naturlig sammen, og som endres samtidig.Samendring (SAMtidig ENDRING): Samling av roller som h\xc3\xb8rer naturlig sammen, og som endres samtidig.')

    _ElementMap.update({
        __samendring.name() : __samendring
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 61, 32)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element samendring uses Python identifier samendring
    __samendring = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'samendring'), 'samendring', '__AbsentNamespace0_CTD_ANON_6_samendring', True, pyxb.utils.utility.Location('hentRoller.xsd', 107, 12), )

    
    samendring = property(__samendring.value, __samendring.set, None, 'Samendring (SAMtidig ENDRING): Samling av roller som h\xc3\xb8rer naturlig sammen, og som endres samtidig.Samendring (SAMtidig ENDRING): Samling av roller som h\xc3\xb8rer naturlig sammen, og som endres samtidig.')

    _ElementMap.update({
        __samendring.name() : __samendring
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 66, 32)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element samendring uses Python identifier samendring
    __samendring = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'samendring'), 'samendring', '__AbsentNamespace0_CTD_ANON_7_samendring', True, pyxb.utils.utility.Location('hentRoller.xsd', 107, 12), )

    
    samendring = property(__samendring.value, __samendring.set, None, 'Samendring (SAMtidig ENDRING): Samling av roller som h\xc3\xb8rer naturlig sammen, og som endres samtidig.Samendring (SAMtidig ENDRING): Samling av roller som h\xc3\xb8rer naturlig sammen, og som endres samtidig.')

    _ElementMap.update({
        __samendring.name() : __samendring
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 71, 32)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element samendring uses Python identifier samendring
    __samendring = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'samendring'), 'samendring', '__AbsentNamespace0_CTD_ANON_8_samendring', True, pyxb.utils.utility.Location('hentRoller.xsd', 107, 12), )

    
    samendring = property(__samendring.value, __samendring.set, None, 'Samendring (SAMtidig ENDRING): Samling av roller som h\xc3\xb8rer naturlig sammen, og som endres samtidig.Samendring (SAMtidig ENDRING): Samling av roller som h\xc3\xb8rer naturlig sammen, og som endres samtidig.')

    _ElementMap.update({
        __samendring.name() : __samendring
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 76, 32)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element samendring uses Python identifier samendring
    __samendring = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'samendring'), 'samendring', '__AbsentNamespace0_CTD_ANON_9_samendring', True, pyxb.utils.utility.Location('hentRoller.xsd', 107, 12), )

    
    samendring = property(__samendring.value, __samendring.set, None, 'Samendring (SAMtidig ENDRING): Samling av roller som h\xc3\xb8rer naturlig sammen, og som endres samtidig.Samendring (SAMtidig ENDRING): Samling av roller som h\xc3\xb8rer naturlig sammen, og som endres samtidig.')

    _ElementMap.update({
        __samendring.name() : __samendring
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 81, 32)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element samendring uses Python identifier samendring
    __samendring = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'samendring'), 'samendring', '__AbsentNamespace0_CTD_ANON_10_samendring', True, pyxb.utils.utility.Location('hentRoller.xsd', 107, 12), )

    
    samendring = property(__samendring.value, __samendring.set, None, 'Samendring (SAMtidig ENDRING): Samling av roller som h\xc3\xb8rer naturlig sammen, og som endres samtidig.Samendring (SAMtidig ENDRING): Samling av roller som h\xc3\xb8rer naturlig sammen, og som endres samtidig.')

    _ElementMap.update({
        __samendring.name() : __samendring
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 86, 32)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element samendring uses Python identifier samendring
    __samendring = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'samendring'), 'samendring', '__AbsentNamespace0_CTD_ANON_11_samendring', True, pyxb.utils.utility.Location('hentRoller.xsd', 107, 12), )

    
    samendring = property(__samendring.value, __samendring.set, None, 'Samendring (SAMtidig ENDRING): Samling av roller som h\xc3\xb8rer naturlig sammen, og som endres samtidig.Samendring (SAMtidig ENDRING): Samling av roller som h\xc3\xb8rer naturlig sammen, og som endres samtidig.')

    _ElementMap.update({
        __samendring.name() : __samendring
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 91, 32)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element samendring uses Python identifier samendring
    __samendring = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'samendring'), 'samendring', '__AbsentNamespace0_CTD_ANON_12_samendring', True, pyxb.utils.utility.Location('hentRoller.xsd', 107, 12), )

    
    samendring = property(__samendring.value, __samendring.set, None, 'Samendring (SAMtidig ENDRING): Samling av roller som h\xc3\xb8rer naturlig sammen, og som endres samtidig.Samendring (SAMtidig ENDRING): Samling av roller som h\xc3\xb8rer naturlig sammen, og som endres samtidig.')

    _ElementMap.update({
        __samendring.name() : __samendring
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """Samendring (SAMtidig ENDRING): Samling av roller som hÃ¸rer naturlig sammen, og som endres samtidig.Samendring (SAMtidig ENDRING): Samling av roller som hÃ¸rer naturlig sammen, og som endres samtidig."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 112, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element headerTekst uses Python identifier headerTekst
    __headerTekst = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'headerTekst'), 'headerTekst', '__AbsentNamespace0_CTD_ANON_13_headerTekst', False, pyxb.utils.utility.Location('hentRoller.xsd', 114, 24), )

    
    headerTekst = property(__headerTekst.value, __headerTekst.set, None, None)

    
    # Element rolle uses Python identifier rolle
    __rolle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'rolle'), 'rolle', '__AbsentNamespace0_CTD_ANON_13_rolle', True, pyxb.utils.utility.Location('hentRoller.xsd', 115, 24), )

    
    rolle = property(__rolle.value, __rolle.set, None, None)

    
    # Element trailerTekst uses Python identifier trailerTekst
    __trailerTekst = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'trailerTekst'), 'trailerTekst', '__AbsentNamespace0_CTD_ANON_13_trailerTekst', False, pyxb.utils.utility.Location('hentRoller.xsd', 395, 24), )

    
    trailerTekst = property(__trailerTekst.value, __trailerTekst.set, None, None)

    
    # Attribute registreringsDato uses Python identifier registreringsDato
    __registreringsDato = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'registreringsDato'), 'registreringsDato', '__AbsentNamespace0_CTD_ANON_13_registreringsDato', pyxb.binding.datatypes.date, required=True)
    __registreringsDato._DeclarationLocation = pyxb.utils.utility.Location('hentRoller.xsd', 397, 20)
    __registreringsDato._UseLocation = pyxb.utils.utility.Location('hentRoller.xsd', 397, 20)
    
    registreringsDato = property(__registreringsDato.value, __registreringsDato.set, None, None)

    
    # Attribute beskrivelse uses Python identifier beskrivelse
    __beskrivelse = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'beskrivelse'), 'beskrivelse', '__AbsentNamespace0_CTD_ANON_13_beskrivelse', pyxb.binding.datatypes.string, required=True)
    __beskrivelse._DeclarationLocation = pyxb.utils.utility.Location('hentRoller.xsd', 398, 20)
    __beskrivelse._UseLocation = pyxb.utils.utility.Location('hentRoller.xsd', 398, 20)
    
    beskrivelse = property(__beskrivelse.value, __beskrivelse.set, None, None)

    
    # Attribute samendringstype uses Python identifier samendringstype
    __samendringstype = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'samendringstype'), 'samendringstype', '__AbsentNamespace0_CTD_ANON_13_samendringstype', pyxb.binding.datatypes.string, required=True)
    __samendringstype._DeclarationLocation = pyxb.utils.utility.Location('hentRoller.xsd', 399, 20)
    __samendringstype._UseLocation = pyxb.utils.utility.Location('hentRoller.xsd', 399, 20)
    
    samendringstype = property(__samendringstype.value, __samendringstype.set, None, None)

    
    # Attribute kjonnsrepresentasjon uses Python identifier kjonnsrepresentasjon
    __kjonnsrepresentasjon = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kjonnsrepresentasjon'), 'kjonnsrepresentasjon', '__AbsentNamespace0_CTD_ANON_13_kjonnsrepresentasjon', pyxb.binding.datatypes.string)
    __kjonnsrepresentasjon._DeclarationLocation = pyxb.utils.utility.Location('hentRoller.xsd', 400, 20)
    __kjonnsrepresentasjon._UseLocation = pyxb.utils.utility.Location('hentRoller.xsd', 400, 20)
    
    kjonnsrepresentasjon = property(__kjonnsrepresentasjon.value, __kjonnsrepresentasjon.set, None, None)

    _ElementMap.update({
        __headerTekst.name() : __headerTekst,
        __rolle.name() : __rolle,
        __trailerTekst.name() : __trailerTekst
    })
    _AttributeMap.update({
        __registreringsDato.name() : __registreringsDato,
        __beskrivelse.name() : __beskrivelse,
        __samendringstype.name() : __samendringstype,
        __kjonnsrepresentasjon.name() : __kjonnsrepresentasjon
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 116, 28)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element person uses Python identifier person
    __person = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'person'), 'person', '__AbsentNamespace0_CTD_ANON_14_person', True, pyxb.utils.utility.Location('hentRoller.xsd', 118, 36), )

    
    person = property(__person.value, __person.set, None, None)

    
    # Element enhet uses Python identifier enhet
    __enhet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'enhet'), 'enhet', '__AbsentNamespace0_CTD_ANON_14_enhet', True, pyxb.utils.utility.Location('hentRoller.xsd', 251, 36), )

    
    enhet = property(__enhet.value, __enhet.set, None, None)

    
    # Attribute beskrivelse uses Python identifier beskrivelse
    __beskrivelse = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'beskrivelse'), 'beskrivelse', '__AbsentNamespace0_CTD_ANON_14_beskrivelse', pyxb.binding.datatypes.string, required=True)
    __beskrivelse._DeclarationLocation = pyxb.utils.utility.Location('hentRoller.xsd', 391, 32)
    __beskrivelse._UseLocation = pyxb.utils.utility.Location('hentRoller.xsd', 391, 32)
    
    beskrivelse = property(__beskrivelse.value, __beskrivelse.set, None, None)

    
    # Attribute rolletype uses Python identifier rolletype
    __rolletype = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rolletype'), 'rolletype', '__AbsentNamespace0_CTD_ANON_14_rolletype', pyxb.binding.datatypes.string, required=True)
    __rolletype._DeclarationLocation = pyxb.utils.utility.Location('hentRoller.xsd', 392, 32)
    __rolletype._UseLocation = pyxb.utils.utility.Location('hentRoller.xsd', 392, 32)
    
    rolletype = property(__rolletype.value, __rolletype.set, None, None)

    _ElementMap.update({
        __person.name() : __person,
        __enhet.name() : __enhet
    })
    _AttributeMap.update({
        __beskrivelse.name() : __beskrivelse,
        __rolletype.name() : __rolletype
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 119, 40)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element vergeTekst uses Python identifier vergeTekst
    __vergeTekst = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vergeTekst'), 'vergeTekst', '__AbsentNamespace0_CTD_ANON_15_vergeTekst', False, pyxb.utils.utility.Location('hentRoller.xsd', 121, 48), )

    
    vergeTekst = property(__vergeTekst.value, __vergeTekst.set, None, None)

    
    # Element fodselsnr uses Python identifier fodselsnr
    __fodselsnr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'fodselsnr'), 'fodselsnr', '__AbsentNamespace0_CTD_ANON_15_fodselsnr', False, pyxb.utils.utility.Location('hentRoller.xsd', 123, 52), )

    
    fodselsnr = property(__fodselsnr.value, __fodselsnr.set, None, None)

    
    # Element fodselsdato uses Python identifier fodselsdato
    __fodselsdato = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'fodselsdato'), 'fodselsdato', '__AbsentNamespace0_CTD_ANON_15_fodselsdato', False, pyxb.utils.utility.Location('hentRoller.xsd', 130, 52), )

    
    fodselsdato = property(__fodselsdato.value, __fodselsdato.set, None, None)

    
    # Element fornavn uses Python identifier fornavn
    __fornavn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'fornavn'), 'fornavn', '__AbsentNamespace0_CTD_ANON_15_fornavn', False, pyxb.utils.utility.Location('hentRoller.xsd', 138, 48), )

    
    fornavn = property(__fornavn.value, __fornavn.set, None, None)

    
    # Element mellomnavn uses Python identifier mellomnavn
    __mellomnavn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mellomnavn'), 'mellomnavn', '__AbsentNamespace0_CTD_ANON_15_mellomnavn', False, pyxb.utils.utility.Location('hentRoller.xsd', 146, 48), )

    
    mellomnavn = property(__mellomnavn.value, __mellomnavn.set, None, None)

    
    # Element slektsnavn uses Python identifier slektsnavn
    __slektsnavn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'slektsnavn'), 'slektsnavn', '__AbsentNamespace0_CTD_ANON_15_slektsnavn', False, pyxb.utils.utility.Location('hentRoller.xsd', 154, 48), )

    
    slektsnavn = property(__slektsnavn.value, __slektsnavn.set, None, None)

    
    # Element adresse1 uses Python identifier adresse1
    __adresse1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'adresse1'), 'adresse1', '__AbsentNamespace0_CTD_ANON_15_adresse1', False, pyxb.utils.utility.Location('hentRoller.xsd', 162, 48), )

    
    adresse1 = property(__adresse1.value, __adresse1.set, None, None)

    
    # Element adresse2 uses Python identifier adresse2
    __adresse2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'adresse2'), 'adresse2', '__AbsentNamespace0_CTD_ANON_15_adresse2', False, pyxb.utils.utility.Location('hentRoller.xsd', 170, 48), )

    
    adresse2 = property(__adresse2.value, __adresse2.set, None, None)

    
    # Element adresse3 uses Python identifier adresse3
    __adresse3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'adresse3'), 'adresse3', '__AbsentNamespace0_CTD_ANON_15_adresse3', False, pyxb.utils.utility.Location('hentRoller.xsd', 178, 48), )

    
    adresse3 = property(__adresse3.value, __adresse3.set, None, None)

    
    # Element postnr uses Python identifier postnr
    __postnr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'postnr'), 'postnr', '__AbsentNamespace0_CTD_ANON_15_postnr', False, pyxb.utils.utility.Location('hentRoller.xsd', 186, 48), )

    
    postnr = property(__postnr.value, __postnr.set, None, None)

    
    # Element poststed uses Python identifier poststed
    __poststed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'poststed'), 'poststed', '__AbsentNamespace0_CTD_ANON_15_poststed', False, pyxb.utils.utility.Location('hentRoller.xsd', 194, 48), )

    
    poststed = property(__poststed.value, __poststed.set, None, None)

    
    # Element land uses Python identifier land
    __land = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'land'), 'land', '__AbsentNamespace0_CTD_ANON_15_land', False, pyxb.utils.utility.Location('hentRoller.xsd', 202, 48), )

    
    land = property(__land.value, __land.set, None, None)

    
    # Element valgtAv uses Python identifier valgtAv
    __valgtAv = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'valgtAv'), 'valgtAv', '__AbsentNamespace0_CTD_ANON_15_valgtAv', False, pyxb.utils.utility.Location('hentRoller.xsd', 211, 48), )

    
    valgtAv = property(__valgtAv.value, __valgtAv.set, None, None)

    
    # Element ansvarsandel uses Python identifier ansvarsandel
    __ansvarsandel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ansvarsandel'), 'ansvarsandel', '__AbsentNamespace0_CTD_ANON_15_ansvarsandel', False, pyxb.utils.utility.Location('hentRoller.xsd', 220, 48), )

    
    ansvarsandel = property(__ansvarsandel.value, __ansvarsandel.set, None, None)

    
    # Element fratraadt uses Python identifier fratraadt
    __fratraadt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'fratraadt'), 'fratraadt', '__AbsentNamespace0_CTD_ANON_15_fratraadt', False, pyxb.utils.utility.Location('hentRoller.xsd', 221, 48), )

    
    fratraadt = property(__fratraadt.value, __fratraadt.set, None, 'K,R,F = Fratr\xc3\xa5dt - N = Ikke fratr\xc3\xa5dt')

    
    # Element fratraadtTekst uses Python identifier fratraadtTekst
    __fratraadtTekst = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'fratraadtTekst'), 'fratraadtTekst', '__AbsentNamespace0_CTD_ANON_15_fratraadtTekst', False, pyxb.utils.utility.Location('hentRoller.xsd', 235, 48), )

    
    fratraadtTekst = property(__fratraadtTekst.value, __fratraadtTekst.set, None, None)

    
    # Element revisorKategori uses Python identifier revisorKategori
    __revisorKategori = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'revisorKategori'), 'revisorKategori', '__AbsentNamespace0_CTD_ANON_15_revisorKategori', False, pyxb.utils.utility.Location('hentRoller.xsd', 242, 48), )

    
    revisorKategori = property(__revisorKategori.value, __revisorKategori.set, None, None)

    
    # Element revisorRkode uses Python identifier revisorRkode
    __revisorRkode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'revisorRkode'), 'revisorRkode', '__AbsentNamespace0_CTD_ANON_15_revisorRkode', False, pyxb.utils.utility.Location('hentRoller.xsd', 243, 48), )

    
    revisorRkode = property(__revisorRkode.value, __revisorRkode.set, None, None)

    
    # Element reTekst uses Python identifier reTekst
    __reTekst = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'reTekst'), 'reTekst', '__AbsentNamespace0_CTD_ANON_15_reTekst', False, pyxb.utils.utility.Location('hentRoller.xsd', 244, 48), )

    
    reTekst = property(__reTekst.value, __reTekst.set, None, None)

    
    # Element rolleFritekst uses Python identifier rolleFritekst
    __rolleFritekst = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'rolleFritekst'), 'rolleFritekst', '__AbsentNamespace0_CTD_ANON_15_rolleFritekst', False, pyxb.utils.utility.Location('hentRoller.xsd', 245, 48), )

    
    rolleFritekst = property(__rolleFritekst.value, __rolleFritekst.set, None, None)

    
    # Attribute beskrivelse uses Python identifier beskrivelse
    __beskrivelse = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'beskrivelse'), 'beskrivelse', '__AbsentNamespace0_CTD_ANON_15_beskrivelse', pyxb.binding.datatypes.string, required=True)
    __beskrivelse._DeclarationLocation = pyxb.utils.utility.Location('hentRoller.xsd', 247, 44)
    __beskrivelse._UseLocation = pyxb.utils.utility.Location('hentRoller.xsd', 247, 44)
    
    beskrivelse = property(__beskrivelse.value, __beskrivelse.set, None, None)

    
    # Attribute statuskode uses Python identifier statuskode
    __statuskode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'statuskode'), 'statuskode', '__AbsentNamespace0_CTD_ANON_15_statuskode', pyxb.binding.datatypes.string, required=True)
    __statuskode._DeclarationLocation = pyxb.utils.utility.Location('hentRoller.xsd', 248, 44)
    __statuskode._UseLocation = pyxb.utils.utility.Location('hentRoller.xsd', 248, 44)
    
    statuskode = property(__statuskode.value, __statuskode.set, None, None)

    _ElementMap.update({
        __vergeTekst.name() : __vergeTekst,
        __fodselsnr.name() : __fodselsnr,
        __fodselsdato.name() : __fodselsdato,
        __fornavn.name() : __fornavn,
        __mellomnavn.name() : __mellomnavn,
        __slektsnavn.name() : __slektsnavn,
        __adresse1.name() : __adresse1,
        __adresse2.name() : __adresse2,
        __adresse3.name() : __adresse3,
        __postnr.name() : __postnr,
        __poststed.name() : __poststed,
        __land.name() : __land,
        __valgtAv.name() : __valgtAv,
        __ansvarsandel.name() : __ansvarsandel,
        __fratraadt.name() : __fratraadt,
        __fratraadtTekst.name() : __fratraadtTekst,
        __revisorKategori.name() : __revisorKategori,
        __revisorRkode.name() : __revisorRkode,
        __reTekst.name() : __reTekst,
        __rolleFritekst.name() : __rolleFritekst
    })
    _AttributeMap.update({
        __beskrivelse.name() : __beskrivelse,
        __statuskode.name() : __statuskode
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 203, 52)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute landkode4 uses Python identifier landkode4
    __landkode4 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'landkode4'), 'landkode4', '__AbsentNamespace0_CTD_ANON_16_landkode4', pyxb.binding.datatypes.string, required=True)
    __landkode4._DeclarationLocation = pyxb.utils.utility.Location('hentRoller.xsd', 206, 64)
    __landkode4._UseLocation = pyxb.utils.utility.Location('hentRoller.xsd', 206, 64)
    
    landkode4 = property(__landkode4.value, __landkode4.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __landkode4.name() : __landkode4
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_17 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 212, 52)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute kode uses Python identifier kode
    __kode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kode'), 'kode', '__AbsentNamespace0_CTD_ANON_17_kode', pyxb.binding.datatypes.string, required=True)
    __kode._DeclarationLocation = pyxb.utils.utility.Location('hentRoller.xsd', 215, 64)
    __kode._UseLocation = pyxb.utils.utility.Location('hentRoller.xsd', 215, 64)
    
    kode = property(__kode.value, __kode.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __kode.name() : __kode
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_18 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 252, 40)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element orgnr uses Python identifier orgnr
    __orgnr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'orgnr'), 'orgnr', '__AbsentNamespace0_CTD_ANON_18_orgnr', False, pyxb.utils.utility.Location('hentRoller.xsd', 254, 48), )

    
    orgnr = property(__orgnr.value, __orgnr.set, None, None)

    
    # Element navn1 uses Python identifier navn1
    __navn1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'navn1'), 'navn1', '__AbsentNamespace0_CTD_ANON_18_navn1', False, pyxb.utils.utility.Location('hentRoller.xsd', 261, 48), )

    
    navn1 = property(__navn1.value, __navn1.set, None, None)

    
    # Element navn2 uses Python identifier navn2
    __navn2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'navn2'), 'navn2', '__AbsentNamespace0_CTD_ANON_18_navn2', False, pyxb.utils.utility.Location('hentRoller.xsd', 269, 48), )

    
    navn2 = property(__navn2.value, __navn2.set, None, None)

    
    # Element navn3 uses Python identifier navn3
    __navn3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'navn3'), 'navn3', '__AbsentNamespace0_CTD_ANON_18_navn3', False, pyxb.utils.utility.Location('hentRoller.xsd', 277, 48), )

    
    navn3 = property(__navn3.value, __navn3.set, None, None)

    
    # Element navn4 uses Python identifier navn4
    __navn4 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'navn4'), 'navn4', '__AbsentNamespace0_CTD_ANON_18_navn4', False, pyxb.utils.utility.Location('hentRoller.xsd', 285, 48), )

    
    navn4 = property(__navn4.value, __navn4.set, None, None)

    
    # Element navn5 uses Python identifier navn5
    __navn5 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'navn5'), 'navn5', '__AbsentNamespace0_CTD_ANON_18_navn5', False, pyxb.utils.utility.Location('hentRoller.xsd', 293, 48), )

    
    navn5 = property(__navn5.value, __navn5.set, None, None)

    
    # Element adresse1 uses Python identifier adresse1
    __adresse1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'adresse1'), 'adresse1', '__AbsentNamespace0_CTD_ANON_18_adresse1', False, pyxb.utils.utility.Location('hentRoller.xsd', 301, 48), )

    
    adresse1 = property(__adresse1.value, __adresse1.set, None, None)

    
    # Element adresse2 uses Python identifier adresse2
    __adresse2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'adresse2'), 'adresse2', '__AbsentNamespace0_CTD_ANON_18_adresse2', False, pyxb.utils.utility.Location('hentRoller.xsd', 309, 48), )

    
    adresse2 = property(__adresse2.value, __adresse2.set, None, None)

    
    # Element adresse3 uses Python identifier adresse3
    __adresse3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'adresse3'), 'adresse3', '__AbsentNamespace0_CTD_ANON_18_adresse3', False, pyxb.utils.utility.Location('hentRoller.xsd', 317, 48), )

    
    adresse3 = property(__adresse3.value, __adresse3.set, None, None)

    
    # Element postnr uses Python identifier postnr
    __postnr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'postnr'), 'postnr', '__AbsentNamespace0_CTD_ANON_18_postnr', False, pyxb.utils.utility.Location('hentRoller.xsd', 325, 48), )

    
    postnr = property(__postnr.value, __postnr.set, None, None)

    
    # Element poststed uses Python identifier poststed
    __poststed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'poststed'), 'poststed', '__AbsentNamespace0_CTD_ANON_18_poststed', False, pyxb.utils.utility.Location('hentRoller.xsd', 333, 48), )

    
    poststed = property(__poststed.value, __poststed.set, None, None)

    
    # Element land uses Python identifier land
    __land = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'land'), 'land', '__AbsentNamespace0_CTD_ANON_18_land', False, pyxb.utils.utility.Location('hentRoller.xsd', 341, 48), )

    
    land = property(__land.value, __land.set, None, None)

    
    # Element valgtAv uses Python identifier valgtAv
    __valgtAv = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'valgtAv'), 'valgtAv', '__AbsentNamespace0_CTD_ANON_18_valgtAv', False, pyxb.utils.utility.Location('hentRoller.xsd', 350, 48), )

    
    valgtAv = property(__valgtAv.value, __valgtAv.set, None, None)

    
    # Element ansvarsandel uses Python identifier ansvarsandel
    __ansvarsandel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ansvarsandel'), 'ansvarsandel', '__AbsentNamespace0_CTD_ANON_18_ansvarsandel', False, pyxb.utils.utility.Location('hentRoller.xsd', 359, 48), )

    
    ansvarsandel = property(__ansvarsandel.value, __ansvarsandel.set, None, None)

    
    # Element fratraadt uses Python identifier fratraadt
    __fratraadt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'fratraadt'), 'fratraadt', '__AbsentNamespace0_CTD_ANON_18_fratraadt', False, pyxb.utils.utility.Location('hentRoller.xsd', 360, 48), )

    
    fratraadt = property(__fratraadt.value, __fratraadt.set, None, 'K,R,F = Fratr\xc3\xa5dt - N = Ikke fratr\xc3\xa5dt')

    
    # Element fratraadtTekst uses Python identifier fratraadtTekst
    __fratraadtTekst = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'fratraadtTekst'), 'fratraadtTekst', '__AbsentNamespace0_CTD_ANON_18_fratraadtTekst', False, pyxb.utils.utility.Location('hentRoller.xsd', 374, 48), )

    
    fratraadtTekst = property(__fratraadtTekst.value, __fratraadtTekst.set, None, None)

    
    # Element revisorKategori uses Python identifier revisorKategori
    __revisorKategori = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'revisorKategori'), 'revisorKategori', '__AbsentNamespace0_CTD_ANON_18_revisorKategori', False, pyxb.utils.utility.Location('hentRoller.xsd', 381, 48), )

    
    revisorKategori = property(__revisorKategori.value, __revisorKategori.set, None, None)

    
    # Element revisorRkode uses Python identifier revisorRkode
    __revisorRkode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'revisorRkode'), 'revisorRkode', '__AbsentNamespace0_CTD_ANON_18_revisorRkode', False, pyxb.utils.utility.Location('hentRoller.xsd', 382, 48), )

    
    revisorRkode = property(__revisorRkode.value, __revisorRkode.set, None, None)

    
    # Element reTekst uses Python identifier reTekst
    __reTekst = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'reTekst'), 'reTekst', '__AbsentNamespace0_CTD_ANON_18_reTekst', False, pyxb.utils.utility.Location('hentRoller.xsd', 383, 48), )

    
    reTekst = property(__reTekst.value, __reTekst.set, None, None)

    
    # Element rolleFritekst uses Python identifier rolleFritekst
    __rolleFritekst = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'rolleFritekst'), 'rolleFritekst', '__AbsentNamespace0_CTD_ANON_18_rolleFritekst', False, pyxb.utils.utility.Location('hentRoller.xsd', 384, 48), )

    
    rolleFritekst = property(__rolleFritekst.value, __rolleFritekst.set, None, None)

    
    # Attribute beskrivelse uses Python identifier beskrivelse
    __beskrivelse = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'beskrivelse'), 'beskrivelse', '__AbsentNamespace0_CTD_ANON_18_beskrivelse', pyxb.binding.datatypes.string, required=True)
    __beskrivelse._DeclarationLocation = pyxb.utils.utility.Location('hentRoller.xsd', 386, 44)
    __beskrivelse._UseLocation = pyxb.utils.utility.Location('hentRoller.xsd', 386, 44)
    
    beskrivelse = property(__beskrivelse.value, __beskrivelse.set, None, None)

    
    # Attribute statuskode uses Python identifier statuskode
    __statuskode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'statuskode'), 'statuskode', '__AbsentNamespace0_CTD_ANON_18_statuskode', pyxb.binding.datatypes.string, required=True)
    __statuskode._DeclarationLocation = pyxb.utils.utility.Location('hentRoller.xsd', 387, 44)
    __statuskode._UseLocation = pyxb.utils.utility.Location('hentRoller.xsd', 387, 44)
    
    statuskode = property(__statuskode.value, __statuskode.set, None, None)

    _ElementMap.update({
        __orgnr.name() : __orgnr,
        __navn1.name() : __navn1,
        __navn2.name() : __navn2,
        __navn3.name() : __navn3,
        __navn4.name() : __navn4,
        __navn5.name() : __navn5,
        __adresse1.name() : __adresse1,
        __adresse2.name() : __adresse2,
        __adresse3.name() : __adresse3,
        __postnr.name() : __postnr,
        __poststed.name() : __poststed,
        __land.name() : __land,
        __valgtAv.name() : __valgtAv,
        __ansvarsandel.name() : __ansvarsandel,
        __fratraadt.name() : __fratraadt,
        __fratraadtTekst.name() : __fratraadtTekst,
        __revisorKategori.name() : __revisorKategori,
        __revisorRkode.name() : __revisorRkode,
        __reTekst.name() : __reTekst,
        __rolleFritekst.name() : __rolleFritekst
    })
    _AttributeMap.update({
        __beskrivelse.name() : __beskrivelse,
        __statuskode.name() : __statuskode
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_19 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 342, 52)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute landkode4 uses Python identifier landkode4
    __landkode4 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'landkode4'), 'landkode4', '__AbsentNamespace0_CTD_ANON_19_landkode4', pyxb.binding.datatypes.string, required=True)
    __landkode4._DeclarationLocation = pyxb.utils.utility.Location('hentRoller.xsd', 345, 64)
    __landkode4._UseLocation = pyxb.utils.utility.Location('hentRoller.xsd', 345, 64)
    
    landkode4 = property(__landkode4.value, __landkode4.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __landkode4.name() : __landkode4
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_20 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 351, 52)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute kode uses Python identifier kode
    __kode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kode'), 'kode', '__AbsentNamespace0_CTD_ANON_20_kode', pyxb.binding.datatypes.string, required=True)
    __kode._DeclarationLocation = pyxb.utils.utility.Location('hentRoller.xsd', 354, 64)
    __kode._UseLocation = pyxb.utils.utility.Location('hentRoller.xsd', 354, 64)
    
    kode = property(__kode.value, __kode.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __kode.name() : __kode
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_21 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('hentRoller.xsd', 12, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element orgnr uses Python identifier orgnr
    __orgnr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'orgnr'), 'orgnr', '__AbsentNamespace0_CTD_ANON_21_orgnr', False, pyxb.utils.utility.Location('hentRoller.xsd', 14, 28), )

    
    orgnr = property(__orgnr.value, __orgnr.set, None, None)

    
    # Element hovedStatus uses Python identifier hovedStatus
    __hovedStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'hovedStatus'), 'hovedStatus', '__AbsentNamespace0_CTD_ANON_21_hovedStatus', False, pyxb.utils.utility.Location('hentRoller.xsd', 15, 28), )

    
    hovedStatus = property(__hovedStatus.value, __hovedStatus.set, None, None)

    
    # Element underStatus uses Python identifier underStatus
    __underStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'underStatus'), 'underStatus', '__AbsentNamespace0_CTD_ANON_21_underStatus', False, pyxb.utils.utility.Location('hentRoller.xsd', 16, 28), )

    
    underStatus = property(__underStatus.value, __underStatus.set, None, None)

    
    # Attribute prossessDato uses Python identifier prossessDato
    __prossessDato = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'prossessDato'), 'prossessDato', '__AbsentNamespace0_CTD_ANON_21_prossessDato', pyxb.binding.datatypes.date, required=True)
    __prossessDato._DeclarationLocation = pyxb.utils.utility.Location('hentRoller.xsd', 32, 24)
    __prossessDato._UseLocation = pyxb.utils.utility.Location('hentRoller.xsd', 32, 24)
    
    prossessDato = property(__prossessDato.value, __prossessDato.set, None, None)

    
    # Attribute tjeneste uses Python identifier tjeneste
    __tjeneste = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tjeneste'), 'tjeneste', '__AbsentNamespace0_CTD_ANON_21_tjeneste', STD_ANON, required=True)
    __tjeneste._DeclarationLocation = pyxb.utils.utility.Location('hentRoller.xsd', 33, 24)
    __tjeneste._UseLocation = pyxb.utils.utility.Location('hentRoller.xsd', 33, 24)
    
    tjeneste = property(__tjeneste.value, __tjeneste.set, None, None)

    _ElementMap.update({
        __orgnr.name() : __orgnr,
        __hovedStatus.name() : __hovedStatus,
        __underStatus.name() : __underStatus
    })
    _AttributeMap.update({
        __prossessDato.name() : __prossessDato,
        __tjeneste.name() : __tjeneste
    })



grunndata = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'grunndata'), CTD_ANON, documentation='Bekskriver tjenesten hentRoller', location=pyxb.utils.utility.Location('hentRoller.xsd', 5, 4))
Namespace.addCategoryObject('elementBinding', grunndata.name().localName(), grunndata)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'responseHeader'), CTD_ANON_21, scope=CTD_ANON, location=pyxb.utils.utility.Location('hentRoller.xsd', 11, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'melding'), CTD_ANON_3, scope=CTD_ANON, location=pyxb.utils.utility.Location('hentRoller.xsd', 43, 16)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 43, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'responseHeader')), pyxb.utils.utility.Location('hentRoller.xsd', 11, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'melding')), pyxb.utils.utility.Location('hentRoller.xsd', 43, 16))
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
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'underStatusMelding'), CTD_ANON_2, scope=CTD_ANON_, location=pyxb.utils.utility.Location('hentRoller.xsd', 19, 40)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'underStatusMelding')), pyxb.utils.utility.Location('hentRoller.xsd', 19, 40))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'organisasjonsnummer'), CTD_ANON_4, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('hentRoller.xsd', 46, 28)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'kontaktperson'), CTD_ANON_5, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('hentRoller.xsd', 55, 28)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'deltakere'), CTD_ANON_6, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('hentRoller.xsd', 60, 28)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'komplementar'), CTD_ANON_7, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('hentRoller.xsd', 65, 28)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sameiere'), CTD_ANON_8, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('hentRoller.xsd', 70, 28)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'styre'), CTD_ANON_9, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('hentRoller.xsd', 75, 28)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'revisor'), CTD_ANON_10, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('hentRoller.xsd', 80, 28)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'regnskapsfoerer'), CTD_ANON_11, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('hentRoller.xsd', 85, 28)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'eierkommune'), CTD_ANON_12, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('hentRoller.xsd', 90, 28)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 55, 28))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 60, 28))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 65, 28))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 70, 28))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 75, 28))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 80, 28))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 85, 28))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 90, 28))
    counters.add(cc_7)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'organisasjonsnummer')), pyxb.utils.utility.Location('hentRoller.xsd', 46, 28))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'kontaktperson')), pyxb.utils.utility.Location('hentRoller.xsd', 55, 28))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'deltakere')), pyxb.utils.utility.Location('hentRoller.xsd', 60, 28))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'komplementar')), pyxb.utils.utility.Location('hentRoller.xsd', 65, 28))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'sameiere')), pyxb.utils.utility.Location('hentRoller.xsd', 70, 28))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'styre')), pyxb.utils.utility.Location('hentRoller.xsd', 75, 28))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'revisor')), pyxb.utils.utility.Location('hentRoller.xsd', 80, 28))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'regnskapsfoerer')), pyxb.utils.utility.Location('hentRoller.xsd', 85, 28))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'eierkommune')), pyxb.utils.utility.Location('hentRoller.xsd', 90, 28))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_2()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'samendring'), CTD_ANON_13, scope=CTD_ANON_5, documentation='Samendring (SAMtidig ENDRING): Samling av roller som h\xc3\xb8rer naturlig sammen, og som endres samtidig.Samendring (SAMtidig ENDRING): Samling av roller som h\xc3\xb8rer naturlig sammen, og som endres samtidig.', location=pyxb.utils.utility.Location('hentRoller.xsd', 107, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, 'samendring')), pyxb.utils.utility.Location('hentRoller.xsd', 107, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_3()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'samendring'), CTD_ANON_13, scope=CTD_ANON_6, documentation='Samendring (SAMtidig ENDRING): Samling av roller som h\xc3\xb8rer naturlig sammen, og som endres samtidig.Samendring (SAMtidig ENDRING): Samling av roller som h\xc3\xb8rer naturlig sammen, og som endres samtidig.', location=pyxb.utils.utility.Location('hentRoller.xsd', 107, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(None, 'samendring')), pyxb.utils.utility.Location('hentRoller.xsd', 107, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_4()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'samendring'), CTD_ANON_13, scope=CTD_ANON_7, documentation='Samendring (SAMtidig ENDRING): Samling av roller som h\xc3\xb8rer naturlig sammen, og som endres samtidig.Samendring (SAMtidig ENDRING): Samling av roller som h\xc3\xb8rer naturlig sammen, og som endres samtidig.', location=pyxb.utils.utility.Location('hentRoller.xsd', 107, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'samendring')), pyxb.utils.utility.Location('hentRoller.xsd', 107, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_5()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'samendring'), CTD_ANON_13, scope=CTD_ANON_8, documentation='Samendring (SAMtidig ENDRING): Samling av roller som h\xc3\xb8rer naturlig sammen, og som endres samtidig.Samendring (SAMtidig ENDRING): Samling av roller som h\xc3\xb8rer naturlig sammen, og som endres samtidig.', location=pyxb.utils.utility.Location('hentRoller.xsd', 107, 12)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'samendring')), pyxb.utils.utility.Location('hentRoller.xsd', 107, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_6()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'samendring'), CTD_ANON_13, scope=CTD_ANON_9, documentation='Samendring (SAMtidig ENDRING): Samling av roller som h\xc3\xb8rer naturlig sammen, og som endres samtidig.Samendring (SAMtidig ENDRING): Samling av roller som h\xc3\xb8rer naturlig sammen, og som endres samtidig.', location=pyxb.utils.utility.Location('hentRoller.xsd', 107, 12)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'samendring')), pyxb.utils.utility.Location('hentRoller.xsd', 107, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_7()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'samendring'), CTD_ANON_13, scope=CTD_ANON_10, documentation='Samendring (SAMtidig ENDRING): Samling av roller som h\xc3\xb8rer naturlig sammen, og som endres samtidig.Samendring (SAMtidig ENDRING): Samling av roller som h\xc3\xb8rer naturlig sammen, og som endres samtidig.', location=pyxb.utils.utility.Location('hentRoller.xsd', 107, 12)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(None, 'samendring')), pyxb.utils.utility.Location('hentRoller.xsd', 107, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_8()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'samendring'), CTD_ANON_13, scope=CTD_ANON_11, documentation='Samendring (SAMtidig ENDRING): Samling av roller som h\xc3\xb8rer naturlig sammen, og som endres samtidig.Samendring (SAMtidig ENDRING): Samling av roller som h\xc3\xb8rer naturlig sammen, og som endres samtidig.', location=pyxb.utils.utility.Location('hentRoller.xsd', 107, 12)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'samendring')), pyxb.utils.utility.Location('hentRoller.xsd', 107, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_9()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'samendring'), CTD_ANON_13, scope=CTD_ANON_12, documentation='Samendring (SAMtidig ENDRING): Samling av roller som h\xc3\xb8rer naturlig sammen, og som endres samtidig.Samendring (SAMtidig ENDRING): Samling av roller som h\xc3\xb8rer naturlig sammen, og som endres samtidig.', location=pyxb.utils.utility.Location('hentRoller.xsd', 107, 12)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'samendring')), pyxb.utils.utility.Location('hentRoller.xsd', 107, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_10()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'headerTekst'), pyxb.binding.datatypes.string, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('hentRoller.xsd', 114, 24)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'rolle'), CTD_ANON_14, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('hentRoller.xsd', 115, 24)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'trailerTekst'), pyxb.binding.datatypes.string, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('hentRoller.xsd', 395, 24)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 114, 24))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 115, 24))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 395, 24))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'headerTekst')), pyxb.utils.utility.Location('hentRoller.xsd', 114, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'rolle')), pyxb.utils.utility.Location('hentRoller.xsd', 115, 24))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'trailerTekst')), pyxb.utils.utility.Location('hentRoller.xsd', 395, 24))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_11()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'person'), CTD_ANON_15, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('hentRoller.xsd', 118, 36)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'enhet'), CTD_ANON_18, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('hentRoller.xsd', 251, 36)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 118, 36))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 251, 36))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'person')), pyxb.utils.utility.Location('hentRoller.xsd', 118, 36))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'enhet')), pyxb.utils.utility.Location('hentRoller.xsd', 251, 36))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_12()




CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vergeTekst'), pyxb.binding.datatypes.string, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('hentRoller.xsd', 121, 48)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'fodselsnr'), STD_ANON_, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('hentRoller.xsd', 123, 52)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'fodselsdato'), STD_ANON_2, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('hentRoller.xsd', 130, 52)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'fornavn'), STD_ANON_3, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('hentRoller.xsd', 138, 48)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mellomnavn'), STD_ANON_4, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('hentRoller.xsd', 146, 48)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'slektsnavn'), STD_ANON_5, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('hentRoller.xsd', 154, 48)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'adresse1'), STD_ANON_6, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('hentRoller.xsd', 162, 48)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'adresse2'), STD_ANON_7, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('hentRoller.xsd', 170, 48)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'adresse3'), STD_ANON_8, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('hentRoller.xsd', 178, 48)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'postnr'), STD_ANON_9, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('hentRoller.xsd', 186, 48)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'poststed'), STD_ANON_10, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('hentRoller.xsd', 194, 48)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'land'), CTD_ANON_16, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('hentRoller.xsd', 202, 48)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'valgtAv'), CTD_ANON_17, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('hentRoller.xsd', 211, 48)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ansvarsandel'), pyxb.binding.datatypes.string, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('hentRoller.xsd', 220, 48)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'fratraadt'), STD_ANON_11, scope=CTD_ANON_15, documentation='K,R,F = Fratr\xc3\xa5dt - N = Ikke fratr\xc3\xa5dt', location=pyxb.utils.utility.Location('hentRoller.xsd', 221, 48)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'fratraadtTekst'), STD_ANON_12, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('hentRoller.xsd', 235, 48)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'revisorKategori'), pyxb.binding.datatypes.int, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('hentRoller.xsd', 242, 48)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'revisorRkode'), pyxb.binding.datatypes.int, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('hentRoller.xsd', 243, 48)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'reTekst'), pyxb.binding.datatypes.string, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('hentRoller.xsd', 244, 48)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'rolleFritekst'), pyxb.binding.datatypes.string, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('hentRoller.xsd', 245, 48)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 121, 48))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 146, 48))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 162, 48))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 170, 48))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 178, 48))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 186, 48))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 194, 48))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 202, 48))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 211, 48))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 220, 48))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 221, 48))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 235, 48))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 242, 48))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 243, 48))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 244, 48))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 245, 48))
    counters.add(cc_15)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'vergeTekst')), pyxb.utils.utility.Location('hentRoller.xsd', 121, 48))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'fodselsnr')), pyxb.utils.utility.Location('hentRoller.xsd', 123, 52))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'fodselsdato')), pyxb.utils.utility.Location('hentRoller.xsd', 130, 52))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'fornavn')), pyxb.utils.utility.Location('hentRoller.xsd', 138, 48))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'mellomnavn')), pyxb.utils.utility.Location('hentRoller.xsd', 146, 48))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'slektsnavn')), pyxb.utils.utility.Location('hentRoller.xsd', 154, 48))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'adresse1')), pyxb.utils.utility.Location('hentRoller.xsd', 162, 48))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'adresse2')), pyxb.utils.utility.Location('hentRoller.xsd', 170, 48))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'adresse3')), pyxb.utils.utility.Location('hentRoller.xsd', 178, 48))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'postnr')), pyxb.utils.utility.Location('hentRoller.xsd', 186, 48))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'poststed')), pyxb.utils.utility.Location('hentRoller.xsd', 194, 48))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'land')), pyxb.utils.utility.Location('hentRoller.xsd', 202, 48))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'valgtAv')), pyxb.utils.utility.Location('hentRoller.xsd', 211, 48))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'ansvarsandel')), pyxb.utils.utility.Location('hentRoller.xsd', 220, 48))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'fratraadt')), pyxb.utils.utility.Location('hentRoller.xsd', 221, 48))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'fratraadtTekst')), pyxb.utils.utility.Location('hentRoller.xsd', 235, 48))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'revisorKategori')), pyxb.utils.utility.Location('hentRoller.xsd', 242, 48))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'revisorRkode')), pyxb.utils.utility.Location('hentRoller.xsd', 243, 48))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'reTekst')), pyxb.utils.utility.Location('hentRoller.xsd', 244, 48))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'rolleFritekst')), pyxb.utils.utility.Location('hentRoller.xsd', 245, 48))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
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
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, True) ]))
    st_19._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_13()




CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'orgnr'), STD_ANON_13, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('hentRoller.xsd', 254, 48)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'navn1'), STD_ANON_14, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('hentRoller.xsd', 261, 48)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'navn2'), STD_ANON_15, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('hentRoller.xsd', 269, 48)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'navn3'), STD_ANON_16, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('hentRoller.xsd', 277, 48)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'navn4'), STD_ANON_17, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('hentRoller.xsd', 285, 48)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'navn5'), STD_ANON_18, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('hentRoller.xsd', 293, 48)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'adresse1'), STD_ANON_19, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('hentRoller.xsd', 301, 48)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'adresse2'), STD_ANON_20, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('hentRoller.xsd', 309, 48)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'adresse3'), STD_ANON_21, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('hentRoller.xsd', 317, 48)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'postnr'), STD_ANON_22, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('hentRoller.xsd', 325, 48)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'poststed'), STD_ANON_23, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('hentRoller.xsd', 333, 48)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'land'), CTD_ANON_19, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('hentRoller.xsd', 341, 48)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'valgtAv'), CTD_ANON_20, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('hentRoller.xsd', 350, 48)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ansvarsandel'), pyxb.binding.datatypes.string, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('hentRoller.xsd', 359, 48)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'fratraadt'), STD_ANON_24, scope=CTD_ANON_18, documentation='K,R,F = Fratr\xc3\xa5dt - N = Ikke fratr\xc3\xa5dt', location=pyxb.utils.utility.Location('hentRoller.xsd', 360, 48)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'fratraadtTekst'), STD_ANON_25, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('hentRoller.xsd', 374, 48)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'revisorKategori'), pyxb.binding.datatypes.int, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('hentRoller.xsd', 381, 48)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'revisorRkode'), pyxb.binding.datatypes.int, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('hentRoller.xsd', 382, 48)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'reTekst'), pyxb.binding.datatypes.string, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('hentRoller.xsd', 383, 48)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'rolleFritekst'), pyxb.binding.datatypes.string, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('hentRoller.xsd', 384, 48)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 269, 48))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 277, 48))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 285, 48))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 293, 48))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 301, 48))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 309, 48))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 317, 48))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 325, 48))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 333, 48))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 341, 48))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 350, 48))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 359, 48))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 360, 48))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 374, 48))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 381, 48))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 382, 48))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 383, 48))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('hentRoller.xsd', 384, 48))
    counters.add(cc_17)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'orgnr')), pyxb.utils.utility.Location('hentRoller.xsd', 254, 48))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'navn1')), pyxb.utils.utility.Location('hentRoller.xsd', 261, 48))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'navn2')), pyxb.utils.utility.Location('hentRoller.xsd', 269, 48))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'navn3')), pyxb.utils.utility.Location('hentRoller.xsd', 277, 48))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'navn4')), pyxb.utils.utility.Location('hentRoller.xsd', 285, 48))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'navn5')), pyxb.utils.utility.Location('hentRoller.xsd', 293, 48))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'adresse1')), pyxb.utils.utility.Location('hentRoller.xsd', 301, 48))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'adresse2')), pyxb.utils.utility.Location('hentRoller.xsd', 309, 48))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'adresse3')), pyxb.utils.utility.Location('hentRoller.xsd', 317, 48))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'postnr')), pyxb.utils.utility.Location('hentRoller.xsd', 325, 48))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'poststed')), pyxb.utils.utility.Location('hentRoller.xsd', 333, 48))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'land')), pyxb.utils.utility.Location('hentRoller.xsd', 341, 48))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'valgtAv')), pyxb.utils.utility.Location('hentRoller.xsd', 350, 48))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'ansvarsandel')), pyxb.utils.utility.Location('hentRoller.xsd', 359, 48))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'fratraadt')), pyxb.utils.utility.Location('hentRoller.xsd', 360, 48))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'fratraadtTekst')), pyxb.utils.utility.Location('hentRoller.xsd', 374, 48))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'revisorKategori')), pyxb.utils.utility.Location('hentRoller.xsd', 381, 48))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'revisorRkode')), pyxb.utils.utility.Location('hentRoller.xsd', 382, 48))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'reTekst')), pyxb.utils.utility.Location('hentRoller.xsd', 383, 48))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'rolleFritekst')), pyxb.utils.utility.Location('hentRoller.xsd', 384, 48))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, True) ]))
    st_19._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_18._Automaton = _BuildAutomaton_14()




CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'orgnr'), pyxb.binding.datatypes.int, scope=CTD_ANON_21, location=pyxb.utils.utility.Location('hentRoller.xsd', 14, 28)))

CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'hovedStatus'), pyxb.binding.datatypes.int, scope=CTD_ANON_21, location=pyxb.utils.utility.Location('hentRoller.xsd', 15, 28)))

CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'underStatus'), CTD_ANON_, scope=CTD_ANON_21, location=pyxb.utils.utility.Location('hentRoller.xsd', 16, 28)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(None, 'orgnr')), pyxb.utils.utility.Location('hentRoller.xsd', 14, 28))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(None, 'hovedStatus')), pyxb.utils.utility.Location('hentRoller.xsd', 15, 28))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(None, 'underStatus')), pyxb.utils.utility.Location('hentRoller.xsd', 16, 28))
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
CTD_ANON_21._Automaton = _BuildAutomaton_15()

