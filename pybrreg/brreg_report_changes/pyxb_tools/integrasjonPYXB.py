# ./pybrreg/brreg_report_changes/pyxb_tools/integrasjonERFV.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:7e5c5481fd105c4cb8c4c3874a397d043a2a3aae
# Generated 2018-01-23 12:17:41.750449 by PyXB version 1.2.4 using Python 2.7.13.final.0
# Namespace http://schema.brreg.no/intef/integrasjonERFV

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:07017fc8-002f-11e8-85e2-74d4354c2634')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://schema.brreg.no/intef/integrasjonERFV', create_if_missing=True)
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
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 19, 5)
    _Documentation = None
STD_ANON._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(4))
STD_ANON._InitializeFacetMap(STD_ANON._CF_totalDigits)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 26, 5)
    _Documentation = None
STD_ANON_._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
STD_ANON_._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_maxLength,
   STD_ANON_._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 35, 5)
    _Documentation = None
STD_ANON_2._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(9))
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_totalDigits)

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 46, 8)
    _Documentation = None
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_3, enum_prefix=None)
STD_ANON_3.N = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='N', tag='N')
STD_ANON_3.J = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='J', tag='J')
STD_ANON_3._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration,
   STD_ANON_3._CF_length)

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 55, 8)
    _Documentation = None
STD_ANON_4._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_4, enum_prefix=None)
STD_ANON_4.N = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='N', tag='N')
STD_ANON_4.J = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='J', tag='J')
STD_ANON_4._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_enumeration,
   STD_ANON_4._CF_length)

# Atomic simple type: [anonymous]
class STD_ANON_5 (pyxb.binding.datatypes.date):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 68, 4)
    _Documentation = None
STD_ANON_5._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_6 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 105, 5)
    _Documentation = None
STD_ANON_6._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_6, enum_prefix=None)
STD_ANON_6.FADR = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='FADR', tag='FADR')
STD_ANON_6.PADR = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='PADR', tag='PADR')
STD_ANON_6.IADR = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='IADR', tag='IADR')
STD_ANON_6.EPOS = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='EPOS', tag='EPOS')
STD_ANON_6.TFON = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='TFON', tag='TFON')
STD_ANON_6.TFAX = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='TFAX', tag='TFAX')
STD_ANON_6.MTLF = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='MTLF', tag='MTLF')
STD_ANON_6.KONT = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='KONT', tag='KONT')
STD_ANON_6.DAGL = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='DAGL', tag='DAGL')
STD_ANON_6.FFR = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='FF\xd8R', tag='FFR')
STD_ANON_6.STYR = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='STYR', tag='STYR')
STD_ANON_6.SIGN = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='SIGN', tag='SIGN')
STD_ANON_6.PROK = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='PROK', tag='PROK')
STD_ANON_6.KTO = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='KTO', tag='KTO')
STD_ANON_6._InitializeFacetMap(STD_ANON_6._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_7 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 126, 5)
    _Documentation = None
STD_ANON_7._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(11))
STD_ANON_7._InitializeFacetMap(STD_ANON_7._CF_length)

# Atomic simple type: [anonymous]
class STD_ANON_8 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 139, 2)
    _Documentation = None
STD_ANON_8._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(13))
STD_ANON_8._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_8._InitializeFacetMap(STD_ANON_8._CF_maxLength,
   STD_ANON_8._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_9 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 155, 6)
    _Documentation = None
STD_ANON_9._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_9, enum_prefix=None)
STD_ANON_9.LEDE = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value='LEDE', tag='LEDE')
STD_ANON_9.NEST = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value='NEST', tag='NEST')
STD_ANON_9.MEDL = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value='MEDL', tag='MEDL')
STD_ANON_9._InitializeFacetMap(STD_ANON_9._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_10 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 171, 5)
    _Documentation = None
STD_ANON_10._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(11))
STD_ANON_10._InitializeFacetMap(STD_ANON_10._CF_length)

# Atomic simple type: [anonymous]
class STD_ANON_11 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 178, 5)
    _Documentation = None
STD_ANON_11._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50))
STD_ANON_11._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_11._InitializeFacetMap(STD_ANON_11._CF_maxLength,
   STD_ANON_11._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_12 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 201, 4)
    _Documentation = None
STD_ANON_12._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_13 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 206, 4)
    _Documentation = None
STD_ANON_13._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_14 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 216, 5)
    _Documentation = None
STD_ANON_14._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_14, enum_prefix=None)
STD_ANON_14.N = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='N', tag='N')
STD_ANON_14.J = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='J', tag='J')
STD_ANON_14._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_14._InitializeFacetMap(STD_ANON_14._CF_enumeration,
   STD_ANON_14._CF_length)

# Atomic simple type: [anonymous]
class STD_ANON_15 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 226, 4)
    _Documentation = None
STD_ANON_15._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_16 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 231, 4)
    _Documentation = None
STD_ANON_16._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_17 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 241, 5)
    _Documentation = None
STD_ANON_17._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_17, enum_prefix=None)
STD_ANON_17.N = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value='N', tag='N')
STD_ANON_17.J = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value='J', tag='J')
STD_ANON_17._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_17._InitializeFacetMap(STD_ANON_17._CF_enumeration,
   STD_ANON_17._CF_length)

# Atomic simple type: [anonymous]
class STD_ANON_18 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 251, 4)
    _Documentation = None
STD_ANON_18._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_19 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 256, 4)
    _Documentation = None
STD_ANON_19._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_20 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 275, 4)
    _Documentation = None
STD_ANON_20._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_21 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 280, 4)
    _Documentation = None
STD_ANON_21._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_22 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 300, 4)
    _Documentation = None
STD_ANON_22._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_23 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 305, 4)
    _Documentation = None
STD_ANON_23._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_24 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 315, 5)
    _Documentation = None
STD_ANON_24._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(4))
STD_ANON_24._InitializeFacetMap(STD_ANON_24._CF_length)

# Atomic simple type: [anonymous]
class STD_ANON_25 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 323, 4)
    _Documentation = None
STD_ANON_25._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_26 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 328, 4)
    _Documentation = None
STD_ANON_26._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_27 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 338, 5)
    _Documentation = None
STD_ANON_27._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_27._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
STD_ANON_27._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_27, enum_prefix=None)
STD_ANON_27.FLI = STD_ANON_27._CF_enumeration.addEnumeration(unicode_value='FLI', tag='FLI')
STD_ANON_27._InitializeFacetMap(STD_ANON_27._CF_minLength,
   STD_ANON_27._CF_maxLength,
   STD_ANON_27._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_28 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 353, 5)
    _Documentation = None
STD_ANON_28._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_28._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_28._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_28, enum_prefix=None)
STD_ANON_28.S = STD_ANON_28._CF_enumeration.addEnumeration(unicode_value='S', tag='S')
STD_ANON_28.E = STD_ANON_28._CF_enumeration.addEnumeration(unicode_value='E', tag='E')
STD_ANON_28.N = STD_ANON_28._CF_enumeration.addEnumeration(unicode_value='N', tag='N')
STD_ANON_28._InitializeFacetMap(STD_ANON_28._CF_minLength,
   STD_ANON_28._CF_maxLength,
   STD_ANON_28._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_29 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 364, 5)
    _Documentation = None
STD_ANON_29._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_29._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
STD_ANON_29._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_29, enum_prefix=None)
STD_ANON_29.SL = STD_ANON_29._CF_enumeration.addEnumeration(unicode_value='SL', tag='SL')
STD_ANON_29.SLFV = STD_ANON_29._CF_enumeration.addEnumeration(unicode_value='SLFV', tag='SLFV')
STD_ANON_29.EN = STD_ANON_29._CF_enumeration.addEnumeration(unicode_value='EN', tag='EN')
STD_ANON_29.NYFV = STD_ANON_29._CF_enumeration.addEnumeration(unicode_value='NYFV', tag='NYFV')
STD_ANON_29.NY = STD_ANON_29._CF_enumeration.addEnumeration(unicode_value='NY', tag='NY')
STD_ANON_29._InitializeFacetMap(STD_ANON_29._CF_minLength,
   STD_ANON_29._CF_maxLength,
   STD_ANON_29._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_30 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 383, 5)
    _Documentation = None
STD_ANON_30._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_30, enum_prefix=None)
STD_ANON_30.J = STD_ANON_30._CF_enumeration.addEnumeration(unicode_value='J', tag='J')
STD_ANON_30._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_30._InitializeFacetMap(STD_ANON_30._CF_enumeration,
   STD_ANON_30._CF_length)

# Atomic simple type: [anonymous]
class STD_ANON_31 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 392, 4)
    _Documentation = None
STD_ANON_31._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_32 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 397, 4)
    _Documentation = None
STD_ANON_32._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_33 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 407, 5)
    _Documentation = None
STD_ANON_33._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(150))
STD_ANON_33._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_33._InitializeFacetMap(STD_ANON_33._CF_maxLength,
   STD_ANON_33._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_34 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 423, 5)
    _Documentation = None
STD_ANON_34._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_35 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 429, 4)
    _Documentation = None
STD_ANON_35._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_36 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 434, 4)
    _Documentation = None
STD_ANON_36._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_37 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 444, 5)
    _Documentation = None
STD_ANON_37._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
STD_ANON_37._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_37._InitializeFacetMap(STD_ANON_37._CF_maxLength,
   STD_ANON_37._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_38 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 452, 5)
    _Documentation = None
STD_ANON_38._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
STD_ANON_38._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_38._InitializeFacetMap(STD_ANON_38._CF_maxLength,
   STD_ANON_38._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_39 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 460, 5)
    _Documentation = None
STD_ANON_39._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
STD_ANON_39._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_39._InitializeFacetMap(STD_ANON_39._CF_maxLength,
   STD_ANON_39._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_40 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 468, 5)
    _Documentation = None
STD_ANON_40._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(4))
STD_ANON_40._InitializeFacetMap(STD_ANON_40._CF_length)

# Atomic simple type: [anonymous]
class STD_ANON_41 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 475, 5)
    _Documentation = None
STD_ANON_41._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
STD_ANON_41._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_41._InitializeFacetMap(STD_ANON_41._CF_maxLength,
   STD_ANON_41._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_42 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 483, 5)
    _Documentation = None
STD_ANON_42._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
STD_ANON_42._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_42._InitializeFacetMap(STD_ANON_42._CF_maxLength,
   STD_ANON_42._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_43 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 491, 5)
    _Documentation = None
STD_ANON_43._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(4))
STD_ANON_43._InitializeFacetMap(STD_ANON_43._CF_length)

# Atomic simple type: [anonymous]
class STD_ANON_44 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 498, 5)
    _Documentation = None
STD_ANON_44._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
STD_ANON_44._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_44._InitializeFacetMap(STD_ANON_44._CF_maxLength,
   STD_ANON_44._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_45 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 506, 5)
    _Documentation = None
STD_ANON_45._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(2))
STD_ANON_45._InitializeFacetMap(STD_ANON_45._CF_length)

# Atomic simple type: [anonymous]
class STD_ANON_46 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 513, 5)
    _Documentation = None
STD_ANON_46._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40))
STD_ANON_46._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_46._InitializeFacetMap(STD_ANON_46._CF_maxLength,
   STD_ANON_46._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_47 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 529, 5)
    _Documentation = None
STD_ANON_47._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_47, enum_prefix=None)
STD_ANON_47.N = STD_ANON_47._CF_enumeration.addEnumeration(unicode_value='N', tag='N')
STD_ANON_47.J = STD_ANON_47._CF_enumeration.addEnumeration(unicode_value='J', tag='J')
STD_ANON_47._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_47._InitializeFacetMap(STD_ANON_47._CF_enumeration,
   STD_ANON_47._CF_length)

# Atomic simple type: [anonymous]
class STD_ANON_48 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 539, 4)
    _Documentation = None
STD_ANON_48._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_49 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 544, 4)
    _Documentation = None
STD_ANON_49._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_50 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 554, 5)
    _Documentation = None
STD_ANON_50._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_50, enum_prefix=None)
STD_ANON_50.N = STD_ANON_50._CF_enumeration.addEnumeration(unicode_value='N', tag='N')
STD_ANON_50.J = STD_ANON_50._CF_enumeration.addEnumeration(unicode_value='J', tag='J')
STD_ANON_50._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_50._InitializeFacetMap(STD_ANON_50._CF_enumeration,
   STD_ANON_50._CF_length)

# Atomic simple type: [anonymous]
class STD_ANON_51 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 564, 4)
    _Documentation = None
STD_ANON_51._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_51, enum_prefix=None)
STD_ANON_51.GRDT = STD_ANON_51._CF_enumeration.addEnumeration(unicode_value='GRDT', tag='GRDT')
STD_ANON_51._InitializeFacetMap(STD_ANON_51._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_52 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 571, 4)
    _Documentation = None
STD_ANON_52._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_52, enum_prefix=None)
STD_ANON_52.FV = STD_ANON_52._CF_enumeration.addEnumeration(unicode_value='FV', tag='FV')
STD_ANON_52._InitializeFacetMap(STD_ANON_52._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_53 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 583, 5)
    _Documentation = None
STD_ANON_53._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(150))
STD_ANON_53._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_53._InitializeFacetMap(STD_ANON_53._CF_maxLength,
   STD_ANON_53._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_54 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 602, 4)
    _Documentation = None
STD_ANON_54._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_54, enum_prefix=None)
STD_ANON_54.KATG = STD_ANON_54._CF_enumeration.addEnumeration(unicode_value='KATG', tag='KATG')
STD_ANON_54._InitializeFacetMap(STD_ANON_54._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_55 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 609, 4)
    _Documentation = None
STD_ANON_55._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_55, enum_prefix=None)
STD_ANON_55.FV = STD_ANON_55._CF_enumeration.addEnumeration(unicode_value='FV', tag='FV')
STD_ANON_55._InitializeFacetMap(STD_ANON_55._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_56 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 621, 5)
    _Documentation = None
STD_ANON_56._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
STD_ANON_56._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_56._InitializeFacetMap(STD_ANON_56._CF_maxLength,
   STD_ANON_56._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_57 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 630, 4)
    _Documentation = None
STD_ANON_57._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_58 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 635, 4)
    _Documentation = None
STD_ANON_58._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_59 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 645, 5)
    _Documentation = None
STD_ANON_59._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_59, enum_prefix=None)
STD_ANON_59.N = STD_ANON_59._CF_enumeration.addEnumeration(unicode_value='N', tag='N')
STD_ANON_59.B = STD_ANON_59._CF_enumeration.addEnumeration(unicode_value='B', tag='B')
STD_ANON_59._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_59._InitializeFacetMap(STD_ANON_59._CF_enumeration,
   STD_ANON_59._CF_length)

# Atomic simple type: [anonymous]
class STD_ANON_60 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 655, 4)
    _Documentation = None
STD_ANON_60._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_61 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 660, 4)
    _Documentation = None
STD_ANON_61._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_62 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 670, 5)
    _Documentation = None
STD_ANON_62._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
STD_ANON_62._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_62._InitializeFacetMap(STD_ANON_62._CF_maxLength,
   STD_ANON_62._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_63 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 678, 5)
    _Documentation = None
STD_ANON_63._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
STD_ANON_63._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_63._InitializeFacetMap(STD_ANON_63._CF_maxLength,
   STD_ANON_63._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_64 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 686, 5)
    _Documentation = None
STD_ANON_64._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
STD_ANON_64._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_64._InitializeFacetMap(STD_ANON_64._CF_maxLength,
   STD_ANON_64._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_65 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 694, 5)
    _Documentation = None
STD_ANON_65._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
STD_ANON_65._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_65._InitializeFacetMap(STD_ANON_65._CF_maxLength,
   STD_ANON_65._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_66 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 702, 5)
    _Documentation = None
STD_ANON_66._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
STD_ANON_66._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_66._InitializeFacetMap(STD_ANON_66._CF_maxLength,
   STD_ANON_66._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_67 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 720, 4)
    _Documentation = None
STD_ANON_67._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_68 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 725, 4)
    _Documentation = None
STD_ANON_68._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_69 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 736, 6)
    _Documentation = None
STD_ANON_69._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_69, enum_prefix=None)
STD_ANON_69.NDAT = STD_ANON_69._CF_enumeration.addEnumeration(unicode_value='NDAT', tag='NDAT')
STD_ANON_69._InitializeFacetMap(STD_ANON_69._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_70 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 743, 6)
    _Documentation = None
STD_ANON_70._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_70, enum_prefix=None)
STD_ANON_70.ER = STD_ANON_70._CF_enumeration.addEnumeration(unicode_value='ER', tag='ER')
STD_ANON_70._InitializeFacetMap(STD_ANON_70._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_71 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 757, 5)
    _Documentation = None
STD_ANON_71._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
STD_ANON_71._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_71._InitializeFacetMap(STD_ANON_71._CF_maxLength,
   STD_ANON_71._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_72 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 765, 5)
    _Documentation = None
STD_ANON_72._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
STD_ANON_72._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_72._InitializeFacetMap(STD_ANON_72._CF_maxLength,
   STD_ANON_72._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_73 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 773, 5)
    _Documentation = None
STD_ANON_73._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
STD_ANON_73._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_73._InitializeFacetMap(STD_ANON_73._CF_maxLength,
   STD_ANON_73._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_74 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 781, 5)
    _Documentation = None
STD_ANON_74._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(4))
STD_ANON_74._InitializeFacetMap(STD_ANON_74._CF_length)

# Atomic simple type: [anonymous]
class STD_ANON_75 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 788, 5)
    _Documentation = None
STD_ANON_75._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
STD_ANON_75._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_75._InitializeFacetMap(STD_ANON_75._CF_maxLength,
   STD_ANON_75._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_76 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 796, 5)
    _Documentation = None
STD_ANON_76._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
STD_ANON_76._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_76._InitializeFacetMap(STD_ANON_76._CF_maxLength,
   STD_ANON_76._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_77 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 804, 5)
    _Documentation = None
STD_ANON_77._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(4))
STD_ANON_77._InitializeFacetMap(STD_ANON_77._CF_length)

# Atomic simple type: [anonymous]
class STD_ANON_78 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 811, 5)
    _Documentation = None
STD_ANON_78._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
STD_ANON_78._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_78._InitializeFacetMap(STD_ANON_78._CF_maxLength,
   STD_ANON_78._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_79 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 819, 5)
    _Documentation = None
STD_ANON_79._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(2))
STD_ANON_79._InitializeFacetMap(STD_ANON_79._CF_length)

# Atomic simple type: [anonymous]
class STD_ANON_80 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 826, 5)
    _Documentation = None
STD_ANON_80._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40))
STD_ANON_80._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_80._InitializeFacetMap(STD_ANON_80._CF_maxLength,
   STD_ANON_80._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_81 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 842, 5)
    _Documentation = None
STD_ANON_81._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_81, enum_prefix=None)
STD_ANON_81.Styrets_leder_og_nestleder_hver_for_seg = STD_ANON_81._CF_enumeration.addEnumeration(unicode_value='Styrets leder og nestleder hver for seg.', tag='Styrets_leder_og_nestleder_hver_for_seg')
STD_ANON_81.Daglig_leder_og_styrets_leder_i_fellesskap = STD_ANON_81._CF_enumeration.addEnumeration(unicode_value='Daglig leder og styrets leder i fellesskap.', tag='Daglig_leder_og_styrets_leder_i_fellesskap')
STD_ANON_81.Styrets_leder_alene = STD_ANON_81._CF_enumeration.addEnumeration(unicode_value='Styrets leder alene.', tag='Styrets_leder_alene')
STD_ANON_81.To_styremedlemmer_i_fellesskap = STD_ANON_81._CF_enumeration.addEnumeration(unicode_value='To styremedlemmer i fellesskap.', tag='To_styremedlemmer_i_fellesskap')
STD_ANON_81.Styrets_medlemmer_hver_for_seg = STD_ANON_81._CF_enumeration.addEnumeration(unicode_value='Styrets medlemmer hver for seg.', tag='Styrets_medlemmer_hver_for_seg')
STD_ANON_81.Daglig_leder_alene = STD_ANON_81._CF_enumeration.addEnumeration(unicode_value='Daglig leder alene.', tag='Daglig_leder_alene')
STD_ANON_81._InitializeFacetMap(STD_ANON_81._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_82 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 859, 7)
    _Documentation = None
STD_ANON_82._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_82, enum_prefix=None)
STD_ANON_82.PROK = STD_ANON_82._CF_enumeration.addEnumeration(unicode_value='PROK', tag='PROK')
STD_ANON_82.POHV = STD_ANON_82._CF_enumeration.addEnumeration(unicode_value='POHV', tag='POHV')
STD_ANON_82.POFE = STD_ANON_82._CF_enumeration.addEnumeration(unicode_value='POFE', tag='POFE')
STD_ANON_82._InitializeFacetMap(STD_ANON_82._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_83 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 871, 4)
    _Documentation = None
STD_ANON_83._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_84 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 876, 4)
    _Documentation = None
STD_ANON_84._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_85 (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 886, 5)
    _Documentation = None
STD_ANON_85._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(9))
STD_ANON_85._InitializeFacetMap(STD_ANON_85._CF_totalDigits)

# Atomic simple type: [anonymous]
class STD_ANON_86 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 901, 4)
    _Documentation = None
STD_ANON_86._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_86, enum_prefix=None)
STD_ANON_86.TFAX = STD_ANON_86._CF_enumeration.addEnumeration(unicode_value='TFAX', tag='TFAX')
STD_ANON_86._InitializeFacetMap(STD_ANON_86._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_87 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 908, 4)
    _Documentation = None
STD_ANON_87._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_87, enum_prefix=None)
STD_ANON_87.ER = STD_ANON_87._CF_enumeration.addEnumeration(unicode_value='ER', tag='ER')
STD_ANON_87._InitializeFacetMap(STD_ANON_87._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_88 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 922, 4)
    _Documentation = None
STD_ANON_88._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_89 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 927, 4)
    _Documentation = None
STD_ANON_89._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_90 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 937, 5)
    _Documentation = None
STD_ANON_90._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(5))
STD_ANON_90._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_90._InitializeFacetMap(STD_ANON_90._CF_maxLength,
   STD_ANON_90._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_91 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 951, 5)
    _Documentation = None
STD_ANON_91._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_91, enum_prefix=None)
STD_ANON_91.Styrets_leder_og_ett_styremedlem_i_fellesskap = STD_ANON_91._CF_enumeration.addEnumeration(unicode_value='Styrets leder og ett styremedlem i fellesskap.', tag='Styrets_leder_og_ett_styremedlem_i_fellesskap')
STD_ANON_91.Daglig_leder_alene = STD_ANON_91._CF_enumeration.addEnumeration(unicode_value='Daglig leder alene.', tag='Daglig_leder_alene')
STD_ANON_91.Styrets_leder_og_nestleder_hver_for_seg = STD_ANON_91._CF_enumeration.addEnumeration(unicode_value='Styrets leder og nestleder hver for seg.', tag='Styrets_leder_og_nestleder_hver_for_seg')
STD_ANON_91.Styrets_leder_alene = STD_ANON_91._CF_enumeration.addEnumeration(unicode_value='Styrets leder alene.', tag='Styrets_leder_alene')
STD_ANON_91.To_styremedlemmer_i_fellesskap = STD_ANON_91._CF_enumeration.addEnumeration(unicode_value='To styremedlemmer i fellesskap.', tag='To_styremedlemmer_i_fellesskap')
STD_ANON_91.Daglig_leder_og_styrets_leder_i_fellesskap = STD_ANON_91._CF_enumeration.addEnumeration(unicode_value='Daglig leder og styrets leder i fellesskap.', tag='Daglig_leder_og_styrets_leder_i_fellesskap')
STD_ANON_91.Styrets_medlemmer_hver_for_seg = STD_ANON_91._CF_enumeration.addEnumeration(unicode_value='Styrets medlemmer hver for seg.', tag='Styrets_medlemmer_hver_for_seg')
STD_ANON_91.Styret_i_fellesskap = STD_ANON_91._CF_enumeration.addEnumeration(unicode_value='Styret i fellesskap.', tag='Styret_i_fellesskap')
STD_ANON_91._InitializeFacetMap(STD_ANON_91._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_92 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 970, 7)
    _Documentation = None
STD_ANON_92._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_92, enum_prefix=None)
STD_ANON_92.SIGN = STD_ANON_92._CF_enumeration.addEnumeration(unicode_value='SIGN', tag='SIGN')
STD_ANON_92.SIHV = STD_ANON_92._CF_enumeration.addEnumeration(unicode_value='SIHV', tag='SIHV')
STD_ANON_92.SIFE = STD_ANON_92._CF_enumeration.addEnumeration(unicode_value='SIFE', tag='SIFE')
STD_ANON_92._InitializeFacetMap(STD_ANON_92._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_93 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 982, 4)
    _Documentation = None
STD_ANON_93._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_94 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 987, 4)
    _Documentation = None
STD_ANON_94._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_95 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 1007, 4)
    _Documentation = None
STD_ANON_95._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_96 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 1012, 4)
    _Documentation = None
STD_ANON_96._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_97 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 1022, 5)
    _Documentation = None
STD_ANON_97._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(150))
STD_ANON_97._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_97._InitializeFacetMap(STD_ANON_97._CF_maxLength,
   STD_ANON_97._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_98 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 1033, 8)
    _Documentation = None
STD_ANON_98._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(8))
STD_ANON_98._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_98._InitializeFacetMap(STD_ANON_98._CF_maxLength,
   STD_ANON_98._CF_minLength)

# Atomic simple type: [anonymous]
class STD_ANON_99 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 1041, 8)
    _Documentation = None
STD_ANON_99._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(13))
STD_ANON_99._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_99._InitializeFacetMap(STD_ANON_99._CF_maxLength,
   STD_ANON_99._CF_minLength)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Beskriver tjenesten integrasjon mot frivillighetsregisteret"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 8, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}header uses Python identifier header
    __header = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'header'), 'header', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_httpschema_brreg_nointefintegrasjonERFVheader', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 15, 1), )


    header = property(__header.value, __header.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}melding uses Python identifier melding
    __melding = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'melding'), 'melding', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_httpschema_brreg_nointefintegrasjonERFVmelding', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 74, 1), )


    melding = property(__melding.value, __melding.set, None, None)

    _ElementMap.update({
        __header.name() : __header,
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
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 43, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}ERstatus uses Python identifier ERstatus
    __ERstatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ERstatus'), 'ERstatus', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON__httpschema_brreg_nointefintegrasjonERFVERstatus', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 45, 7), )


    ERstatus = property(__ERstatus.value, __ERstatus.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}FVstatus uses Python identifier FVstatus
    __FVstatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FVstatus'), 'FVstatus', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON__httpschema_brreg_nointefintegrasjonERFVFVstatus', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 54, 7), )


    FVstatus = property(__FVstatus.value, __FVstatus.set, None, None)

    _ElementMap.update({
        __ERstatus.name() : __ERstatus,
        __FVstatus.name() : __FVstatus
    })
    _AttributeMap.update({

    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 75, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}opplysningUtgaar uses Python identifier opplysningUtgaar
    __opplysningUtgaar = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'opplysningUtgaar'), 'opplysningUtgaar', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_2_httpschema_brreg_nointefintegrasjonERFVopplysningUtgaar', True, pyxb.utils.utility.Location('integrasjonERFV.xsd', 104, 4), )


    opplysningUtgaar = property(__opplysningUtgaar.value, __opplysningUtgaar.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}signerer uses Python identifier signerer
    __signerer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'signerer'), 'signerer', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_2_httpschema_brreg_nointefintegrasjonERFVsignerer', True, pyxb.utils.utility.Location('integrasjonERFV.xsd', 125, 4), )


    signerer = property(__signerer.value, __signerer.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}kontaktperson uses Python identifier kontaktperson
    __kontaktperson = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'kontaktperson'), 'kontaktperson', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_2_httpschema_brreg_nointefintegrasjonERFVkontaktperson', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 188, 1), )


    kontaktperson = property(__kontaktperson.value, __kontaktperson.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}aarsregnskapLeveres uses Python identifier aarsregnskapLeveres
    __aarsregnskapLeveres = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'aarsregnskapLeveres'), 'aarsregnskapLeveres', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_2_httpschema_brreg_nointefintegrasjonERFVaarsregnskapLeveres', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 212, 1), )


    aarsregnskapLeveres = property(__aarsregnskapLeveres.value, __aarsregnskapLeveres.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}ansatte uses Python identifier ansatte
    __ansatte = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ansatte'), 'ansatte', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_2_httpschema_brreg_nointefintegrasjonERFVansatte', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 237, 1), )


    ansatte = property(__ansatte.value, __ansatte.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}dagligLeder uses Python identifier dagligLeder
    __dagligLeder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dagligLeder'), 'dagligLeder', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_2_httpschema_brreg_nointefintegrasjonERFVdagligLeder', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 262, 1), )


    dagligLeder = property(__dagligLeder.value, __dagligLeder.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}forretningsforer uses Python identifier forretningsforer
    __forretningsforer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'forretningsforer'), 'forretningsforer', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_2_httpschema_brreg_nointefintegrasjonERFVforretningsforer', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 286, 1), )


    forretningsforer = property(__forretningsforer.value, __forretningsforer.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}regnskapsperiode uses Python identifier regnskapsperiode
    __regnskapsperiode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'regnskapsperiode'), 'regnskapsperiode', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_2_httpschema_brreg_nointefintegrasjonERFVregnskapsperiode', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 311, 1), )


    regnskapsperiode = property(__regnskapsperiode.value, __regnskapsperiode.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}endringAvVedtekter uses Python identifier endringAvVedtekter
    __endringAvVedtekter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'endringAvVedtekter'), 'endringAvVedtekter', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_2_httpschema_brreg_nointefintegrasjonERFVendringAvVedtekter', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 379, 1), )


    endringAvVedtekter = property(__endringAvVedtekter.value, __endringAvVedtekter.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}epost uses Python identifier epost
    __epost = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'epost'), 'epost', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_2_httpschema_brreg_nointefintegrasjonERFVepost', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 403, 1), )


    epost = property(__epost.value, __epost.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}formaal uses Python identifier formaal
    __formaal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'formaal'), 'formaal', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_2_httpschema_brreg_nointefintegrasjonERFVformaal', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 419, 1), )


    formaal = property(__formaal.value, __formaal.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}forretningsAdresse uses Python identifier forretningsAdresse
    __forretningsAdresse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'forretningsAdresse'), 'forretningsAdresse', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_2_httpschema_brreg_nointefintegrasjonERFVforretningsAdresse', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 440, 1), )


    forretningsAdresse = property(__forretningsAdresse.value, __forretningsAdresse.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}meldepliktVedtekter uses Python identifier meldepliktVedtekter
    __meldepliktVedtekter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'meldepliktVedtekter'), 'meldepliktVedtekter', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_2_httpschema_brreg_nointefintegrasjonERFVmeldepliktVedtekter', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 525, 1), )


    meldepliktVedtekter = property(__meldepliktVedtekter.value, __meldepliktVedtekter.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}grasrotandel uses Python identifier grasrotandel
    __grasrotandel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'grasrotandel'), 'grasrotandel', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_2_httpschema_brreg_nointefintegrasjonERFVgrasrotandel', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 550, 1), )


    grasrotandel = property(__grasrotandel.value, __grasrotandel.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}hjemmeside uses Python identifier hjemmeside
    __hjemmeside = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hjemmeside'), 'hjemmeside', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_2_httpschema_brreg_nointefintegrasjonERFVhjemmeside', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 579, 1), )


    hjemmeside = property(__hjemmeside.value, __hjemmeside.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}kategori uses Python identifier kategori
    __kategori = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'kategori'), 'kategori', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_2_httpschema_brreg_nointefintegrasjonERFVkategori', True, pyxb.utils.utility.Location('integrasjonERFV.xsd', 595, 1), )


    kategori = property(__kategori.value, __kategori.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}kontonummer uses Python identifier kontonummer
    __kontonummer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'kontonummer'), 'kontonummer', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_2_httpschema_brreg_nointefintegrasjonERFVkontonummer', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 617, 1), )


    kontonummer = property(__kontonummer.value, __kontonummer.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}maalform uses Python identifier maalform
    __maalform = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'maalform'), 'maalform', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_2_httpschema_brreg_nointefintegrasjonERFVmaalform', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 641, 1), )


    maalform = property(__maalform.value, __maalform.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}navn uses Python identifier navn
    __navn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'navn'), 'navn', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_2_httpschema_brreg_nointefintegrasjonERFVnavn', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 666, 1), )


    navn = property(__navn.value, __navn.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}mobil uses Python identifier mobil
    __mobil = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mobil'), 'mobil', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_2_httpschema_brreg_nointefintegrasjonERFVmobil', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 714, 1), )


    mobil = property(__mobil.value, __mobil.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}nedleggelsesdato uses Python identifier nedleggelsesdato
    __nedleggelsesdato = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nedleggelsesdato'), 'nedleggelsesdato', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_2_httpschema_brreg_nointefintegrasjonERFVnedleggelsesdato', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 731, 1), )


    nedleggelsesdato = property(__nedleggelsesdato.value, __nedleggelsesdato.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}postAdresse uses Python identifier postAdresse
    __postAdresse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'postAdresse'), 'postAdresse', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_2_httpschema_brreg_nointefintegrasjonERFVpostAdresse', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 753, 1), )


    postAdresse = property(__postAdresse.value, __postAdresse.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}prokura uses Python identifier prokura
    __prokura = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'prokura'), 'prokura', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_2_httpschema_brreg_nointefintegrasjonERFVprokura', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 838, 1), )


    prokura = property(__prokura.value, __prokura.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}telefaks uses Python identifier telefaks
    __telefaks = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'telefaks'), 'telefaks', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_2_httpschema_brreg_nointefintegrasjonERFVtelefaks', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 895, 1), )


    telefaks = property(__telefaks.value, __telefaks.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}telefon uses Python identifier telefon
    __telefon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'telefon'), 'telefon', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_2_httpschema_brreg_nointefintegrasjonERFVtelefon', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 916, 1), )


    telefon = property(__telefon.value, __telefon.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}vedlegg uses Python identifier vedlegg
    __vedlegg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vedlegg'), 'vedlegg', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_2_httpschema_brreg_nointefintegrasjonERFVvedlegg', True, pyxb.utils.utility.Location('integrasjonERFV.xsd', 933, 1), )


    vedlegg = property(__vedlegg.value, __vedlegg.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}signatur uses Python identifier signatur
    __signatur = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'signatur'), 'signatur', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_2_httpschema_brreg_nointefintegrasjonERFVsignatur', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 947, 1), )


    signatur = property(__signatur.value, __signatur.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}stiftelsesdato uses Python identifier stiftelsesdato
    __stiftelsesdato = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'stiftelsesdato'), 'stiftelsesdato', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_2_httpschema_brreg_nointefintegrasjonERFVstiftelsesdato', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 993, 1), )


    stiftelsesdato = property(__stiftelsesdato.value, __stiftelsesdato.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}styre uses Python identifier styre
    __styre = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'styre'), 'styre', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_2_httpschema_brreg_nointefintegrasjonERFVstyre', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 1003, 1), )


    styre = property(__styre.value, __styre.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}elektroniskVarslingsadresse uses Python identifier elektroniskVarslingsadresse
    __elektroniskVarslingsadresse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'elektroniskVarslingsadresse'), 'elektroniskVarslingsadresse', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_2_httpschema_brreg_nointefintegrasjonERFVelektroniskVarslingsadresse', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 1018, 1), )


    elektroniskVarslingsadresse = property(__elektroniskVarslingsadresse.value, __elektroniskVarslingsadresse.set, None, None)

    _ElementMap.update({
        __opplysningUtgaar.name() : __opplysningUtgaar,
        __signerer.name() : __signerer,
        __kontaktperson.name() : __kontaktperson,
        __aarsregnskapLeveres.name() : __aarsregnskapLeveres,
        __ansatte.name() : __ansatte,
        __dagligLeder.name() : __dagligLeder,
        __forretningsforer.name() : __forretningsforer,
        __regnskapsperiode.name() : __regnskapsperiode,
        __endringAvVedtekter.name() : __endringAvVedtekter,
        __epost.name() : __epost,
        __formaal.name() : __formaal,
        __forretningsAdresse.name() : __forretningsAdresse,
        __meldepliktVedtekter.name() : __meldepliktVedtekter,
        __grasrotandel.name() : __grasrotandel,
        __hjemmeside.name() : __hjemmeside,
        __kategori.name() : __kategori,
        __kontonummer.name() : __kontonummer,
        __maalform.name() : __maalform,
        __navn.name() : __navn,
        __mobil.name() : __mobil,
        __nedleggelsesdato.name() : __nedleggelsesdato,
        __postAdresse.name() : __postAdresse,
        __prokura.name() : __prokura,
        __telefaks.name() : __telefaks,
        __telefon.name() : __telefon,
        __vedlegg.name() : __vedlegg,
        __signatur.name() : __signatur,
        __stiftelsesdato.name() : __stiftelsesdato,
        __styre.name() : __styre,
        __elektroniskVarslingsadresse.name() : __elektroniskVarslingsadresse
    })
    _AttributeMap.update({

    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 168, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}fodselsnr uses Python identifier fodselsnr
    __fodselsnr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fodselsnr'), 'fodselsnr', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_3_httpschema_brreg_nointefintegrasjonERFVfodselsnr', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 170, 4), )


    fodselsnr = property(__fodselsnr.value, __fodselsnr.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}slektsnavn uses Python identifier slektsnavn
    __slektsnavn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'slektsnavn'), 'slektsnavn', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_3_httpschema_brreg_nointefintegrasjonERFVslektsnavn', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 177, 4), )


    slektsnavn = property(__slektsnavn.value, __slektsnavn.set, None, None)

    _ElementMap.update({
        __fodselsnr.name() : __fodselsnr,
        __slektsnavn.name() : __slektsnavn
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
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 192, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}person uses Python identifier person
    __person = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'person'), 'person', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_4_httpschema_brreg_nointefintegrasjonERFVperson', True, pyxb.utils.utility.Location('integrasjonERFV.xsd', 167, 1), )


    person = property(__person.value, __person.set, None, None)


    # Attribute rolletype uses Python identifier rolletype
    __rolletype = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rolletype'), 'rolletype', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_4_rolletype', pyxb.binding.datatypes.string, fixed=True, unicode_default='KONT', required=True)
    __rolletype._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 196, 6)
    __rolletype._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 196, 6)

    rolletype = property(__rolletype.value, __rolletype.set, None, None)

    _ElementMap.update({
        __person.name() : __person
    })
    _AttributeMap.update({
        __rolletype.name() : __rolletype
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 266, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}person uses Python identifier person
    __person = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'person'), 'person', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_5_httpschema_brreg_nointefintegrasjonERFVperson', True, pyxb.utils.utility.Location('integrasjonERFV.xsd', 167, 1), )


    person = property(__person.value, __person.set, None, None)


    # Attribute rolletype uses Python identifier rolletype
    __rolletype = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rolletype'), 'rolletype', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_5_rolletype', pyxb.binding.datatypes.string, fixed=True, unicode_default='DAGL', required=True)
    __rolletype._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 270, 6)
    __rolletype._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 270, 6)

    rolletype = property(__rolletype.value, __rolletype.set, None, None)

    _ElementMap.update({
        __person.name() : __person
    })
    _AttributeMap.update({
        __rolletype.name() : __rolletype
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 290, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}person uses Python identifier person
    __person = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'person'), 'person', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_6_httpschema_brreg_nointefintegrasjonERFVperson', True, pyxb.utils.utility.Location('integrasjonERFV.xsd', 167, 1), )


    person = property(__person.value, __person.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}enhet uses Python identifier enhet
    __enhet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'enhet'), 'enhet', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_6_httpschema_brreg_nointefintegrasjonERFVenhet', True, pyxb.utils.utility.Location('integrasjonERFV.xsd', 882, 1), )


    enhet = property(__enhet.value, __enhet.set, None, None)


    # Attribute rolletype uses Python identifier rolletype
    __rolletype = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rolletype'), 'rolletype', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_6_rolletype', pyxb.binding.datatypes.string, fixed=True, unicode_default='FF\xd8R', required=True)
    __rolletype._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 295, 6)
    __rolletype._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 295, 6)

    rolletype = property(__rolletype.value, __rolletype.set, None, None)

    _ElementMap.update({
        __person.name() : __person,
        __enhet.name() : __enhet
    })
    _AttributeMap.update({
        __rolletype.name() : __rolletype
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 335, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}orgform uses Python identifier orgform
    __orgform = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orgform'), 'orgform', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_7_httpschema_brreg_nointefintegrasjonERFVorgform', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 337, 4), )


    orgform = property(__orgform.value, __orgform.set, None, None)

    _ElementMap.update({
        __orgform.name() : __orgform
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
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 350, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}hovedsakstype uses Python identifier hovedsakstype
    __hovedsakstype = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hovedsakstype'), 'hovedsakstype', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_8_httpschema_brreg_nointefintegrasjonERFVhovedsakstype', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 352, 4), )


    hovedsakstype = property(__hovedsakstype.value, __hovedsakstype.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}undersakstype uses Python identifier undersakstype
    __undersakstype = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'undersakstype'), 'undersakstype', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_8_httpschema_brreg_nointefintegrasjonERFVundersakstype', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 363, 4), )


    undersakstype = property(__undersakstype.value, __undersakstype.set, None, None)

    _ElementMap.update({
        __hovedsakstype.name() : __hovedsakstype,
        __undersakstype.name() : __undersakstype
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
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 404, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}epostAdresse uses Python identifier epostAdresse
    __epostAdresse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'epostAdresse'), 'epostAdresse', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_9_httpschema_brreg_nointefintegrasjonERFVepostAdresse', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 406, 4), )


    epostAdresse = property(__epostAdresse.value, __epostAdresse.set, None, None)


    # Attribute infoType uses Python identifier infoType
    __infoType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'infoType'), 'infoType', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_9_infoType', pyxb.binding.datatypes.string, fixed=True, unicode_default='EPOS', required=True)
    __infoType._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 415, 3)
    __infoType._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 415, 3)

    infoType = property(__infoType.value, __infoType.set, None, None)


    # Attribute register uses Python identifier register
    __register = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'register'), 'register', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_9_register', pyxb.binding.datatypes.string, fixed=True, unicode_default='ER', required=True)
    __register._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 416, 3)
    __register._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 416, 3)

    register = property(__register.value, __register.set, None, None)

    _ElementMap.update({
        __epostAdresse.name() : __epostAdresse
    })
    _AttributeMap.update({
        __infoType.name() : __infoType,
        __register.name() : __register
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 441, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}adresse1 uses Python identifier adresse1
    __adresse1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'adresse1'), 'adresse1', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_10_httpschema_brreg_nointefintegrasjonERFVadresse1', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 443, 4), )


    adresse1 = property(__adresse1.value, __adresse1.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}adresse2 uses Python identifier adresse2
    __adresse2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'adresse2'), 'adresse2', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_10_httpschema_brreg_nointefintegrasjonERFVadresse2', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 451, 4), )


    adresse2 = property(__adresse2.value, __adresse2.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}adresse3 uses Python identifier adresse3
    __adresse3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'adresse3'), 'adresse3', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_10_httpschema_brreg_nointefintegrasjonERFVadresse3', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 459, 4), )


    adresse3 = property(__adresse3.value, __adresse3.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}postnr uses Python identifier postnr
    __postnr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'postnr'), 'postnr', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_10_httpschema_brreg_nointefintegrasjonERFVpostnr', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 467, 4), )


    postnr = property(__postnr.value, __postnr.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}poststed uses Python identifier poststed
    __poststed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'poststed'), 'poststed', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_10_httpschema_brreg_nointefintegrasjonERFVpoststed', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 474, 4), )


    poststed = property(__poststed.value, __poststed.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}utenlandskPoststed uses Python identifier utenlandskPoststed
    __utenlandskPoststed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'utenlandskPoststed'), 'utenlandskPoststed', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_10_httpschema_brreg_nointefintegrasjonERFVutenlandskPoststed', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 482, 4), )


    utenlandskPoststed = property(__utenlandskPoststed.value, __utenlandskPoststed.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}kommunenummer uses Python identifier kommunenummer
    __kommunenummer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'kommunenummer'), 'kommunenummer', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_10_httpschema_brreg_nointefintegrasjonERFVkommunenummer', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 490, 4), )


    kommunenummer = property(__kommunenummer.value, __kommunenummer.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}kommune uses Python identifier kommune
    __kommune = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'kommune'), 'kommune', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_10_httpschema_brreg_nointefintegrasjonERFVkommune', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 497, 4), )


    kommune = property(__kommune.value, __kommune.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}landkode uses Python identifier landkode
    __landkode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'landkode'), 'landkode', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_10_httpschema_brreg_nointefintegrasjonERFVlandkode', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 505, 4), )


    landkode = property(__landkode.value, __landkode.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}land uses Python identifier land
    __land = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'land'), 'land', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_10_httpschema_brreg_nointefintegrasjonERFVland', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 512, 4), )


    land = property(__land.value, __land.set, None, None)


    # Attribute infoType uses Python identifier infoType
    __infoType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'infoType'), 'infoType', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_10_infoType', pyxb.binding.datatypes.string, fixed=True, unicode_default='FADR', required=True)
    __infoType._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 521, 3)
    __infoType._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 521, 3)

    infoType = property(__infoType.value, __infoType.set, None, None)


    # Attribute register uses Python identifier register
    __register = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'register'), 'register', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_10_register', pyxb.binding.datatypes.string, fixed=True, unicode_default='ER', required=True)
    __register._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 522, 3)
    __register._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 522, 3)

    register = property(__register.value, __register.set, None, None)

    _ElementMap.update({
        __adresse1.name() : __adresse1,
        __adresse2.name() : __adresse2,
        __adresse3.name() : __adresse3,
        __postnr.name() : __postnr,
        __poststed.name() : __poststed,
        __utenlandskPoststed.name() : __utenlandskPoststed,
        __kommunenummer.name() : __kommunenummer,
        __kommune.name() : __kommune,
        __landkode.name() : __landkode,
        __land.name() : __land
    })
    _AttributeMap.update({
        __infoType.name() : __infoType,
        __register.name() : __register
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 580, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}url uses Python identifier url
    __url = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'url'), 'url', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_11_httpschema_brreg_nointefintegrasjonERFVurl', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 582, 4), )


    url = property(__url.value, __url.set, None, None)


    # Attribute infoType uses Python identifier infoType
    __infoType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'infoType'), 'infoType', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_11_infoType', pyxb.binding.datatypes.string, fixed=True, unicode_default='IADR', required=True)
    __infoType._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 591, 3)
    __infoType._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 591, 3)

    infoType = property(__infoType.value, __infoType.set, None, None)


    # Attribute register uses Python identifier register
    __register = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'register'), 'register', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_11_register', pyxb.binding.datatypes.string, fixed=True, unicode_default='ER', required=True)
    __register._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 592, 3)
    __register._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 592, 3)

    register = property(__register.value, __register.set, None, None)

    _ElementMap.update({
        __url.name() : __url
    })
    _AttributeMap.update({
        __infoType.name() : __infoType,
        __register.name() : __register
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 667, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}navn1 uses Python identifier navn1
    __navn1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'navn1'), 'navn1', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_12_httpschema_brreg_nointefintegrasjonERFVnavn1', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 669, 4), )


    navn1 = property(__navn1.value, __navn1.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}navn2 uses Python identifier navn2
    __navn2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'navn2'), 'navn2', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_12_httpschema_brreg_nointefintegrasjonERFVnavn2', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 677, 4), )


    navn2 = property(__navn2.value, __navn2.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}navn3 uses Python identifier navn3
    __navn3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'navn3'), 'navn3', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_12_httpschema_brreg_nointefintegrasjonERFVnavn3', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 685, 4), )


    navn3 = property(__navn3.value, __navn3.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}navn4 uses Python identifier navn4
    __navn4 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'navn4'), 'navn4', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_12_httpschema_brreg_nointefintegrasjonERFVnavn4', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 693, 4), )


    navn4 = property(__navn4.value, __navn4.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}navn5 uses Python identifier navn5
    __navn5 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'navn5'), 'navn5', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_12_httpschema_brreg_nointefintegrasjonERFVnavn5', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 701, 4), )


    navn5 = property(__navn5.value, __navn5.set, None, None)


    # Attribute infoType uses Python identifier infoType
    __infoType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'infoType'), 'infoType', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_12_infoType', pyxb.binding.datatypes.string, fixed=True, unicode_default='NAVN', required=True)
    __infoType._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 710, 3)
    __infoType._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 710, 3)

    infoType = property(__infoType.value, __infoType.set, None, None)


    # Attribute register uses Python identifier register
    __register = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'register'), 'register', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_12_register', pyxb.binding.datatypes.string, fixed=True, unicode_default='ER', required=True)
    __register._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 711, 3)
    __register._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 711, 3)

    register = property(__register.value, __register.set, None, None)

    _ElementMap.update({
        __navn1.name() : __navn1,
        __navn2.name() : __navn2,
        __navn3.name() : __navn3,
        __navn4.name() : __navn4,
        __navn5.name() : __navn5
    })
    _AttributeMap.update({
        __infoType.name() : __infoType,
        __register.name() : __register
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 754, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}adresse1 uses Python identifier adresse1
    __adresse1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'adresse1'), 'adresse1', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_13_httpschema_brreg_nointefintegrasjonERFVadresse1', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 756, 4), )


    adresse1 = property(__adresse1.value, __adresse1.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}adresse2 uses Python identifier adresse2
    __adresse2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'adresse2'), 'adresse2', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_13_httpschema_brreg_nointefintegrasjonERFVadresse2', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 764, 4), )


    adresse2 = property(__adresse2.value, __adresse2.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}adresse3 uses Python identifier adresse3
    __adresse3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'adresse3'), 'adresse3', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_13_httpschema_brreg_nointefintegrasjonERFVadresse3', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 772, 4), )


    adresse3 = property(__adresse3.value, __adresse3.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}postnr uses Python identifier postnr
    __postnr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'postnr'), 'postnr', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_13_httpschema_brreg_nointefintegrasjonERFVpostnr', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 780, 4), )


    postnr = property(__postnr.value, __postnr.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}poststed uses Python identifier poststed
    __poststed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'poststed'), 'poststed', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_13_httpschema_brreg_nointefintegrasjonERFVpoststed', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 787, 4), )


    poststed = property(__poststed.value, __poststed.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}utenlandskPoststed uses Python identifier utenlandskPoststed
    __utenlandskPoststed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'utenlandskPoststed'), 'utenlandskPoststed', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_13_httpschema_brreg_nointefintegrasjonERFVutenlandskPoststed', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 795, 4), )


    utenlandskPoststed = property(__utenlandskPoststed.value, __utenlandskPoststed.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}kommunenummer uses Python identifier kommunenummer
    __kommunenummer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'kommunenummer'), 'kommunenummer', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_13_httpschema_brreg_nointefintegrasjonERFVkommunenummer', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 803, 4), )


    kommunenummer = property(__kommunenummer.value, __kommunenummer.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}kommune uses Python identifier kommune
    __kommune = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'kommune'), 'kommune', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_13_httpschema_brreg_nointefintegrasjonERFVkommune', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 810, 4), )


    kommune = property(__kommune.value, __kommune.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}landkode uses Python identifier landkode
    __landkode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'landkode'), 'landkode', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_13_httpschema_brreg_nointefintegrasjonERFVlandkode', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 818, 4), )


    landkode = property(__landkode.value, __landkode.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}land uses Python identifier land
    __land = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'land'), 'land', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_13_httpschema_brreg_nointefintegrasjonERFVland', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 825, 4), )


    land = property(__land.value, __land.set, None, None)


    # Attribute infoType uses Python identifier infoType
    __infoType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'infoType'), 'infoType', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_13_infoType', pyxb.binding.datatypes.string, fixed=True, unicode_default='PADR', required=True)
    __infoType._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 834, 3)
    __infoType._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 834, 3)

    infoType = property(__infoType.value, __infoType.set, None, None)


    # Attribute register uses Python identifier register
    __register = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'register'), 'register', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_13_register', pyxb.binding.datatypes.string, fixed=True, unicode_default='ER', required=True)
    __register._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 835, 3)
    __register._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 835, 3)

    register = property(__register.value, __register.set, None, None)

    _ElementMap.update({
        __adresse1.name() : __adresse1,
        __adresse2.name() : __adresse2,
        __adresse3.name() : __adresse3,
        __postnr.name() : __postnr,
        __poststed.name() : __poststed,
        __utenlandskPoststed.name() : __utenlandskPoststed,
        __kommunenummer.name() : __kommunenummer,
        __kommune.name() : __kommune,
        __landkode.name() : __landkode,
        __land.name() : __land
    })
    _AttributeMap.update({
        __infoType.name() : __infoType,
        __register.name() : __register
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 883, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}orgnr uses Python identifier orgnr
    __orgnr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orgnr'), 'orgnr', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_14_httpschema_brreg_nointefintegrasjonERFVorgnr', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 885, 4), )


    orgnr = property(__orgnr.value, __orgnr.set, None, None)

    _ElementMap.update({
        __orgnr.name() : __orgnr
    })
    _AttributeMap.update({

    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 934, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}vedleggsType uses Python identifier vedleggsType
    __vedleggsType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vedleggsType'), 'vedleggsType', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_15_httpschema_brreg_nointefintegrasjonERFVvedleggsType', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 936, 4), )


    vedleggsType = property(__vedleggsType.value, __vedleggsType.set, None, None)

    _ElementMap.update({
        __vedleggsType.name() : __vedleggsType
    })
    _AttributeMap.update({

    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.date
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 994, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.date

    # Attribute infoType uses Python identifier infoType
    __infoType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'infoType'), 'infoType', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_16_infoType', pyxb.binding.datatypes.string, fixed=True, unicode_default='STID', required=True)
    __infoType._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 997, 5)
    __infoType._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 997, 5)

    infoType = property(__infoType.value, __infoType.set, None, None)


    # Attribute register uses Python identifier register
    __register = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'register'), 'register', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_16_register', pyxb.binding.datatypes.string, fixed=True, unicode_default='ER', required=True)
    __register._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 998, 5)
    __register._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 998, 5)

    register = property(__register.value, __register.set, None, None)

    _ElementMap.update({

    })
    _AttributeMap.update({
        __infoType.name() : __infoType,
        __register.name() : __register
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_17 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 1019, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}epostadresse uses Python identifier epostadresse
    __epostadresse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'epostadresse'), 'epostadresse', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_17_httpschema_brreg_nointefintegrasjonERFVepostadresse', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 1021, 4), )


    epostadresse = property(__epostadresse.value, __epostadresse.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}mobil uses Python identifier mobil
    __mobil = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mobil'), 'mobil', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_17_httpschema_brreg_nointefintegrasjonERFVmobil', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 1029, 4), )


    mobil = property(__mobil.value, __mobil.set, None, None)

    _ElementMap.update({
        __epostadresse.name() : __epostadresse,
        __mobil.name() : __mobil
    })
    _AttributeMap.update({

    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_18 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 1030, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}prefiks uses Python identifier prefiks
    __prefiks = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'prefiks'), 'prefiks', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_18_httpschema_brreg_nointefintegrasjonERFVprefiks', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 1032, 7), )


    prefiks = property(__prefiks.value, __prefiks.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}mobilnummer uses Python identifier mobilnummer
    __mobilnummer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mobilnummer'), 'mobilnummer', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_18_httpschema_brreg_nointefintegrasjonERFVmobilnummer', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 1040, 7), )


    mobilnummer = property(__mobilnummer.value, __mobilnummer.set, None, None)

    _ElementMap.update({
        __prefiks.name() : __prefiks,
        __mobilnummer.name() : __mobilnummer
    })
    _AttributeMap.update({

    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_19 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 16, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}SLsysId uses Python identifier SLsysId
    __SLsysId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SLsysId'), 'SLsysId', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_19_httpschema_brreg_nointefintegrasjonERFVSLsysId', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 18, 4), )


    SLsysId = property(__SLsysId.value, __SLsysId.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}SLsysMeldingsId uses Python identifier SLsysMeldingsId
    __SLsysMeldingsId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SLsysMeldingsId'), 'SLsysMeldingsId', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_19_httpschema_brreg_nointefintegrasjonERFVSLsysMeldingsId', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 25, 4), )


    SLsysMeldingsId = property(__SLsysMeldingsId.value, __SLsysMeldingsId.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}organisasjonsnummer uses Python identifier organisasjonsnummer
    __organisasjonsnummer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'organisasjonsnummer'), 'organisasjonsnummer', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_19_httpschema_brreg_nointefintegrasjonERFVorganisasjonsnummer', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 34, 4), )


    organisasjonsnummer = property(__organisasjonsnummer.value, __organisasjonsnummer.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}status uses Python identifier status
    __status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'status'), 'status', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_19_httpschema_brreg_nointefintegrasjonERFVstatus', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 42, 4), )


    status = property(__status.value, __status.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}organisasjonsform uses Python identifier organisasjonsform
    __organisasjonsform = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'organisasjonsform'), 'organisasjonsform', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_19_httpschema_brreg_nointefintegrasjonERFVorganisasjonsform', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 334, 1), )


    organisasjonsform = property(__organisasjonsform.value, __organisasjonsform.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}sakstype uses Python identifier sakstype
    __sakstype = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sakstype'), 'sakstype', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_19_httpschema_brreg_nointefintegrasjonERFVsakstype', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 349, 1), )


    sakstype = property(__sakstype.value, __sakstype.set, None, None)


    # Attribute MeldingsDato uses Python identifier MeldingsDato
    __MeldingsDato = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'MeldingsDato'), 'MeldingsDato', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_19_MeldingsDato', STD_ANON_5, required=True)
    __MeldingsDato._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 67, 3)
    __MeldingsDato._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 67, 3)

    MeldingsDato = property(__MeldingsDato.value, __MeldingsDato.set, None, None)

    _ElementMap.update({
        __SLsysId.name() : __SLsysId,
        __SLsysMeldingsId.name() : __SLsysMeldingsId,
        __organisasjonsnummer.name() : __organisasjonsnummer,
        __status.name() : __status,
        __organisasjonsform.name() : __organisasjonsform,
        __sakstype.name() : __sakstype
    })
    _AttributeMap.update({
        __MeldingsDato.name() : __MeldingsDato
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_20 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 149, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}person uses Python identifier person
    __person = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'person'), 'person', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_20_httpschema_brreg_nointefintegrasjonERFVperson', True, pyxb.utils.utility.Location('integrasjonERFV.xsd', 167, 1), )


    person = property(__person.value, __person.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}enhet uses Python identifier enhet
    __enhet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'enhet'), 'enhet', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_20_httpschema_brreg_nointefintegrasjonERFVenhet', True, pyxb.utils.utility.Location('integrasjonERFV.xsd', 882, 1), )


    enhet = property(__enhet.value, __enhet.set, None, None)


    # Attribute rolle uses Python identifier rolle
    __rolle = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rolle'), 'rolle', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_20_rolle', STD_ANON_9, required=True)
    __rolle._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 154, 5)
    __rolle._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 154, 5)

    rolle = property(__rolle.value, __rolle.set, None, None)

    _ElementMap.update({
        __person.name() : __person,
        __enhet.name() : __enhet
    })
    _AttributeMap.update({
        __rolle.name() : __rolle
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_21 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 189, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}rolle uses Python identifier rolle
    __rolle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rolle'), 'rolle', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_21_httpschema_brreg_nointefintegrasjonERFVrolle', True, pyxb.utils.utility.Location('integrasjonERFV.xsd', 191, 4), )


    rolle = property(__rolle.value, __rolle.set, None, None)


    # Attribute infoType uses Python identifier infoType
    __infoType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'infoType'), 'infoType', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_21_infoType', STD_ANON_12, fixed=True, unicode_default='KONT', required=True)
    __infoType._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 200, 3)
    __infoType._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 200, 3)

    infoType = property(__infoType.value, __infoType.set, None, None)


    # Attribute register uses Python identifier register
    __register = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'register'), 'register', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_21_register', STD_ANON_13, fixed=True, unicode_default='ER', required=True)
    __register._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 205, 3)
    __register._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 205, 3)

    register = property(__register.value, __register.set, None, None)

    _ElementMap.update({
        __rolle.name() : __rolle
    })
    _AttributeMap.update({
        __infoType.name() : __infoType,
        __register.name() : __register
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_22 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 213, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}skalLevere uses Python identifier skalLevere
    __skalLevere = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'skalLevere'), 'skalLevere', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_22_httpschema_brreg_nointefintegrasjonERFVskalLevere', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 215, 4), )


    skalLevere = property(__skalLevere.value, __skalLevere.set, None, None)


    # Attribute infoType uses Python identifier infoType
    __infoType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'infoType'), 'infoType', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_22_infoType', STD_ANON_15, fixed=True, unicode_default='FVRR', required=True)
    __infoType._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 225, 3)
    __infoType._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 225, 3)

    infoType = property(__infoType.value, __infoType.set, None, None)


    # Attribute register uses Python identifier register
    __register = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'register'), 'register', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_22_register', STD_ANON_16, fixed=True, unicode_default='FV', required=True)
    __register._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 230, 3)
    __register._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 230, 3)

    register = property(__register.value, __register.set, None, None)

    _ElementMap.update({
        __skalLevere.name() : __skalLevere
    })
    _AttributeMap.update({
        __infoType.name() : __infoType,
        __register.name() : __register
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_23 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 238, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}harAnsatte uses Python identifier harAnsatte
    __harAnsatte = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'harAnsatte'), 'harAnsatte', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_23_httpschema_brreg_nointefintegrasjonERFVharAnsatte', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 240, 4), )


    harAnsatte = property(__harAnsatte.value, __harAnsatte.set, None, None)


    # Attribute infoType uses Python identifier infoType
    __infoType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'infoType'), 'infoType', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_23_infoType', STD_ANON_18, fixed=True, unicode_default='ARBG', required=True)
    __infoType._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 250, 3)
    __infoType._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 250, 3)

    infoType = property(__infoType.value, __infoType.set, None, None)


    # Attribute register uses Python identifier register
    __register = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'register'), 'register', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_23_register', STD_ANON_19, fixed=True, unicode_default='ER', required=True)
    __register._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 255, 3)
    __register._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 255, 3)

    register = property(__register.value, __register.set, None, None)

    _ElementMap.update({
        __harAnsatte.name() : __harAnsatte
    })
    _AttributeMap.update({
        __infoType.name() : __infoType,
        __register.name() : __register
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_24 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 263, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}rolle uses Python identifier rolle
    __rolle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rolle'), 'rolle', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_24_httpschema_brreg_nointefintegrasjonERFVrolle', True, pyxb.utils.utility.Location('integrasjonERFV.xsd', 265, 4), )


    rolle = property(__rolle.value, __rolle.set, None, None)


    # Attribute infoType uses Python identifier infoType
    __infoType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'infoType'), 'infoType', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_24_infoType', STD_ANON_20, fixed=True, unicode_default='DAGL', required=True)
    __infoType._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 274, 3)
    __infoType._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 274, 3)

    infoType = property(__infoType.value, __infoType.set, None, None)


    # Attribute register uses Python identifier register
    __register = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'register'), 'register', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_24_register', STD_ANON_21, fixed=True, unicode_default='ER', required=True)
    __register._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 279, 3)
    __register._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 279, 3)

    register = property(__register.value, __register.set, None, None)

    _ElementMap.update({
        __rolle.name() : __rolle
    })
    _AttributeMap.update({
        __infoType.name() : __infoType,
        __register.name() : __register
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_25 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 287, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}rolle uses Python identifier rolle
    __rolle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rolle'), 'rolle', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_25_httpschema_brreg_nointefintegrasjonERFVrolle', True, pyxb.utils.utility.Location('integrasjonERFV.xsd', 289, 4), )


    rolle = property(__rolle.value, __rolle.set, None, None)


    # Attribute infoType uses Python identifier infoType
    __infoType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'infoType'), 'infoType', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_25_infoType', STD_ANON_22, fixed=True, unicode_default='FF\xd8R', required=True)
    __infoType._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 299, 3)
    __infoType._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 299, 3)

    infoType = property(__infoType.value, __infoType.set, None, None)


    # Attribute register uses Python identifier register
    __register = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'register'), 'register', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_25_register', STD_ANON_23, fixed=True, unicode_default='ER', required=True)
    __register._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 304, 3)
    __register._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 304, 3)

    register = property(__register.value, __register.set, None, None)

    _ElementMap.update({
        __rolle.name() : __rolle
    })
    _AttributeMap.update({
        __infoType.name() : __infoType,
        __register.name() : __register
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_26 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 312, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}datoMaaned uses Python identifier datoMaaned
    __datoMaaned = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'datoMaaned'), 'datoMaaned', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_26_httpschema_brreg_nointefintegrasjonERFVdatoMaaned', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 314, 4), )


    datoMaaned = property(__datoMaaned.value, __datoMaaned.set, None, None)


    # Attribute infoType uses Python identifier infoType
    __infoType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'infoType'), 'infoType', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_26_infoType', STD_ANON_25, fixed=True, unicode_default='FVRP', required=True)
    __infoType._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 322, 3)
    __infoType._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 322, 3)

    infoType = property(__infoType.value, __infoType.set, None, None)


    # Attribute register uses Python identifier register
    __register = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'register'), 'register', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_26_register', STD_ANON_26, fixed=True, unicode_default='FV', required=True)
    __register._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 327, 3)
    __register._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 327, 3)

    register = property(__register.value, __register.set, None, None)

    _ElementMap.update({
        __datoMaaned.name() : __datoMaaned
    })
    _AttributeMap.update({
        __infoType.name() : __infoType,
        __register.name() : __register
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_27 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 380, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}endringMeldt uses Python identifier endringMeldt
    __endringMeldt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'endringMeldt'), 'endringMeldt', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_27_httpschema_brreg_nointefintegrasjonERFVendringMeldt', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 382, 4), )


    endringMeldt = property(__endringMeldt.value, __endringMeldt.set, None, None)


    # Attribute infoType uses Python identifier infoType
    __infoType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'infoType'), 'infoType', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_27_infoType', STD_ANON_31, fixed=True, unicode_default='EVDT', required=True)
    __infoType._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 391, 3)
    __infoType._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 391, 3)

    infoType = property(__infoType.value, __infoType.set, None, None)


    # Attribute register uses Python identifier register
    __register = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'register'), 'register', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_27_register', STD_ANON_32, fixed=True, unicode_default='FV', required=True)
    __register._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 396, 3)
    __register._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 396, 3)

    register = property(__register.value, __register.set, None, None)

    _ElementMap.update({
        __endringMeldt.name() : __endringMeldt
    })
    _AttributeMap.update({
        __infoType.name() : __infoType,
        __register.name() : __register
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_28 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 420, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}formaalTekst uses Python identifier formaalTekst
    __formaalTekst = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'formaalTekst'), 'formaalTekst', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_28_httpschema_brreg_nointefintegrasjonERFVformaalTekst', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 422, 4), )


    formaalTekst = property(__formaalTekst.value, __formaalTekst.set, None, None)


    # Attribute infoType uses Python identifier infoType
    __infoType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'infoType'), 'infoType', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_28_infoType', STD_ANON_35, fixed=True, unicode_default='FORM', required=True)
    __infoType._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 428, 3)
    __infoType._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 428, 3)

    infoType = property(__infoType.value, __infoType.set, None, None)


    # Attribute register uses Python identifier register
    __register = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'register'), 'register', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_28_register', STD_ANON_36, fixed=True, unicode_default='ER', required=True)
    __register._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 433, 3)
    __register._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 433, 3)

    register = property(__register.value, __register.set, None, None)

    _ElementMap.update({
        __formaalTekst.name() : __formaalTekst
    })
    _AttributeMap.update({
        __infoType.name() : __infoType,
        __register.name() : __register
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_29 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 526, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}skalRegistreres uses Python identifier skalRegistreres
    __skalRegistreres = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'skalRegistreres'), 'skalRegistreres', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_29_httpschema_brreg_nointefintegrasjonERFVskalRegistreres', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 528, 4), )


    skalRegistreres = property(__skalRegistreres.value, __skalRegistreres.set, None, None)


    # Attribute infoType uses Python identifier infoType
    __infoType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'infoType'), 'infoType', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_29_infoType', STD_ANON_48, fixed=True, unicode_default='MPVT', required=True)
    __infoType._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 538, 3)
    __infoType._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 538, 3)

    infoType = property(__infoType.value, __infoType.set, None, None)


    # Attribute register uses Python identifier register
    __register = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'register'), 'register', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_29_register', STD_ANON_49, fixed=True, unicode_default='FV', required=True)
    __register._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 543, 3)
    __register._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 543, 3)

    register = property(__register.value, __register.set, None, None)

    _ElementMap.update({
        __skalRegistreres.name() : __skalRegistreres
    })
    _AttributeMap.update({
        __infoType.name() : __infoType,
        __register.name() : __register
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_30 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 551, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}skalDelta uses Python identifier skalDelta
    __skalDelta = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'skalDelta'), 'skalDelta', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_30_httpschema_brreg_nointefintegrasjonERFVskalDelta', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 553, 4), )


    skalDelta = property(__skalDelta.value, __skalDelta.set, None, None)


    # Attribute infotype uses Python identifier infotype
    __infotype = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'infotype'), 'infotype', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_30_infotype', STD_ANON_51, fixed=True, unicode_default='GRDT', required=True)
    __infotype._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 563, 3)
    __infotype._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 563, 3)

    infotype = property(__infotype.value, __infotype.set, None, None)


    # Attribute register uses Python identifier register
    __register = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'register'), 'register', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_30_register', STD_ANON_52, fixed=True, unicode_default='FV', required=True)
    __register._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 570, 3)
    __register._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 570, 3)

    register = property(__register.value, __register.set, None, None)

    _ElementMap.update({
        __skalDelta.name() : __skalDelta
    })
    _AttributeMap.update({
        __infotype.name() : __infotype,
        __register.name() : __register
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_31 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 596, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}kode uses Python identifier kode
    __kode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'kode'), 'kode', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_31_httpschema_brreg_nointefintegrasjonERFVkode', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 598, 4), )


    kode = property(__kode.value, __kode.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}rangering uses Python identifier rangering
    __rangering = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rangering'), 'rangering', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_31_httpschema_brreg_nointefintegrasjonERFVrangering', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 599, 4), )


    rangering = property(__rangering.value, __rangering.set, None, None)


    # Attribute infoType uses Python identifier infoType
    __infoType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'infoType'), 'infoType', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_31_infoType', STD_ANON_54, fixed=True, unicode_default='KATG', required=True)
    __infoType._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 601, 3)
    __infoType._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 601, 3)

    infoType = property(__infoType.value, __infoType.set, None, None)


    # Attribute register uses Python identifier register
    __register = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'register'), 'register', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_31_register', STD_ANON_55, fixed=True, unicode_default='FV', required=True)
    __register._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 608, 3)
    __register._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 608, 3)

    register = property(__register.value, __register.set, None, None)

    _ElementMap.update({
        __kode.name() : __kode,
        __rangering.name() : __rangering
    })
    _AttributeMap.update({
        __infoType.name() : __infoType,
        __register.name() : __register
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_32 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 618, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}nummer uses Python identifier nummer
    __nummer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nummer'), 'nummer', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_32_httpschema_brreg_nointefintegrasjonERFVnummer', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 620, 4), )


    nummer = property(__nummer.value, __nummer.set, None, None)


    # Attribute infoType uses Python identifier infoType
    __infoType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'infoType'), 'infoType', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_32_infoType', STD_ANON_57, fixed=True, unicode_default='KTO', required=True)
    __infoType._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 629, 3)
    __infoType._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 629, 3)

    infoType = property(__infoType.value, __infoType.set, None, None)


    # Attribute register uses Python identifier register
    __register = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'register'), 'register', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_32_register', STD_ANON_58, fixed=True, unicode_default='FV', required=True)
    __register._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 634, 3)
    __register._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 634, 3)

    register = property(__register.value, __register.set, None, None)

    _ElementMap.update({
        __nummer.name() : __nummer
    })
    _AttributeMap.update({
        __infoType.name() : __infoType,
        __register.name() : __register
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_33 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 642, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}maalformKode uses Python identifier maalformKode
    __maalformKode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'maalformKode'), 'maalformKode', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_33_httpschema_brreg_nointefintegrasjonERFVmaalformKode', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 644, 4), )


    maalformKode = property(__maalformKode.value, __maalformKode.set, None, None)


    # Attribute infoType uses Python identifier infoType
    __infoType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'infoType'), 'infoType', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_33_infoType', STD_ANON_60, fixed=True, unicode_default='M\xc5L', required=True)
    __infoType._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 654, 3)
    __infoType._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 654, 3)

    infoType = property(__infoType.value, __infoType.set, None, None)


    # Attribute register uses Python identifier register
    __register = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'register'), 'register', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_33_register', STD_ANON_61, fixed=True, unicode_default='ER', required=True)
    __register._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 659, 3)
    __register._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 659, 3)

    register = property(__register.value, __register.set, None, None)

    _ElementMap.update({
        __maalformKode.name() : __maalformKode
    })
    _AttributeMap.update({
        __infoType.name() : __infoType,
        __register.name() : __register
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_34 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 715, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}nummer uses Python identifier nummer
    __nummer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nummer'), 'nummer', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_34_httpschema_brreg_nointefintegrasjonERFVnummer', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 135, 1), )


    nummer = property(__nummer.value, __nummer.set, None, 'felleselement for nummer som har like egenskaper')


    # Attribute infoType uses Python identifier infoType
    __infoType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'infoType'), 'infoType', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_34_infoType', STD_ANON_67, fixed=True, unicode_default='MTLF', required=True)
    __infoType._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 719, 3)
    __infoType._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 719, 3)

    infoType = property(__infoType.value, __infoType.set, None, None)


    # Attribute register uses Python identifier register
    __register = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'register'), 'register', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_34_register', STD_ANON_68, fixed=True, unicode_default='ER', required=True)
    __register._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 724, 3)
    __register._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 724, 3)

    register = property(__register.value, __register.set, None, None)

    _ElementMap.update({
        __nummer.name() : __nummer
    })
    _AttributeMap.update({
        __infoType.name() : __infoType,
        __register.name() : __register
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_35 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.date
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 732, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.date

    # Attribute infoType uses Python identifier infoType
    __infoType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'infoType'), 'infoType', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_35_infoType', STD_ANON_69, fixed=True, unicode_default='NDAT', required=True)
    __infoType._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 735, 5)
    __infoType._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 735, 5)

    infoType = property(__infoType.value, __infoType.set, None, None)


    # Attribute register uses Python identifier register
    __register = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'register'), 'register', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_35_register', STD_ANON_70, fixed=True, unicode_default='ER', required=True)
    __register._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 742, 5)
    __register._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 742, 5)

    register = property(__register.value, __register.set, None, None)

    _ElementMap.update({

    })
    _AttributeMap.update({
        __infoType.name() : __infoType,
        __register.name() : __register
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_36 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 839, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}prokuraTekst uses Python identifier prokuraTekst
    __prokuraTekst = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'prokuraTekst'), 'prokuraTekst', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_36_httpschema_brreg_nointefintegrasjonERFVprokuraTekst', True, pyxb.utils.utility.Location('integrasjonERFV.xsd', 841, 4), )


    prokuraTekst = property(__prokuraTekst.value, __prokuraTekst.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}rolle uses Python identifier rolle
    __rolle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rolle'), 'rolle', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_36_httpschema_brreg_nointefintegrasjonERFVrolle', True, pyxb.utils.utility.Location('integrasjonERFV.xsd', 853, 4), )


    rolle = property(__rolle.value, __rolle.set, None, None)


    # Attribute infoType uses Python identifier infoType
    __infoType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'infoType'), 'infoType', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_36_infoType', STD_ANON_83, fixed=True, unicode_default='PROK', required=True)
    __infoType._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 870, 3)
    __infoType._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 870, 3)

    infoType = property(__infoType.value, __infoType.set, None, None)


    # Attribute register uses Python identifier register
    __register = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'register'), 'register', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_36_register', STD_ANON_84, fixed=True, unicode_default='ER', required=True)
    __register._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 875, 3)
    __register._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 875, 3)

    register = property(__register.value, __register.set, None, None)

    _ElementMap.update({
        __prokuraTekst.name() : __prokuraTekst,
        __rolle.name() : __rolle
    })
    _AttributeMap.update({
        __infoType.name() : __infoType,
        __register.name() : __register
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_37 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 854, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}person uses Python identifier person
    __person = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'person'), 'person', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_37_httpschema_brreg_nointefintegrasjonERFVperson', True, pyxb.utils.utility.Location('integrasjonERFV.xsd', 167, 1), )


    person = property(__person.value, __person.set, None, None)


    # Attribute rolletype uses Python identifier rolletype
    __rolletype = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rolletype'), 'rolletype', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_37_rolletype', STD_ANON_82, required=True)
    __rolletype._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 858, 6)
    __rolletype._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 858, 6)

    rolletype = property(__rolletype.value, __rolletype.set, None, None)

    _ElementMap.update({
        __person.name() : __person
    })
    _AttributeMap.update({
        __rolletype.name() : __rolletype
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_38 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 896, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}nummer uses Python identifier nummer
    __nummer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nummer'), 'nummer', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_38_httpschema_brreg_nointefintegrasjonERFVnummer', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 135, 1), )


    nummer = property(__nummer.value, __nummer.set, None, 'felleselement for nummer som har like egenskaper')


    # Attribute infoType uses Python identifier infoType
    __infoType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'infoType'), 'infoType', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_38_infoType', STD_ANON_86, fixed=True, unicode_default='TFAX', required=True)
    __infoType._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 900, 3)
    __infoType._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 900, 3)

    infoType = property(__infoType.value, __infoType.set, None, None)


    # Attribute register uses Python identifier register
    __register = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'register'), 'register', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_38_register', STD_ANON_87, fixed=True, unicode_default='ER', required=True)
    __register._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 907, 3)
    __register._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 907, 3)

    register = property(__register.value, __register.set, None, None)

    _ElementMap.update({
        __nummer.name() : __nummer
    })
    _AttributeMap.update({
        __infoType.name() : __infoType,
        __register.name() : __register
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_39 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 917, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}nummer uses Python identifier nummer
    __nummer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nummer'), 'nummer', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_39_httpschema_brreg_nointefintegrasjonERFVnummer', False, pyxb.utils.utility.Location('integrasjonERFV.xsd', 135, 1), )


    nummer = property(__nummer.value, __nummer.set, None, 'felleselement for nummer som har like egenskaper')


    # Attribute infoType uses Python identifier infoType
    __infoType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'infoType'), 'infoType', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_39_infoType', STD_ANON_88, fixed=True, unicode_default='TFON', required=True)
    __infoType._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 921, 3)
    __infoType._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 921, 3)

    infoType = property(__infoType.value, __infoType.set, None, None)


    # Attribute register uses Python identifier register
    __register = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'register'), 'register', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_39_register', STD_ANON_89, fixed=True, unicode_default='ER', required=True)
    __register._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 926, 3)
    __register._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 926, 3)

    register = property(__register.value, __register.set, None, None)

    _ElementMap.update({
        __nummer.name() : __nummer
    })
    _AttributeMap.update({
        __infoType.name() : __infoType,
        __register.name() : __register
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_40 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 948, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}signaturTekst uses Python identifier signaturTekst
    __signaturTekst = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'signaturTekst'), 'signaturTekst', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_40_httpschema_brreg_nointefintegrasjonERFVsignaturTekst', True, pyxb.utils.utility.Location('integrasjonERFV.xsd', 950, 4), )


    signaturTekst = property(__signaturTekst.value, __signaturTekst.set, None, None)


    # Element {http://schema.brreg.no/intef/integrasjonERFV}rolle uses Python identifier rolle
    __rolle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rolle'), 'rolle', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_40_httpschema_brreg_nointefintegrasjonERFVrolle', True, pyxb.utils.utility.Location('integrasjonERFV.xsd', 964, 4), )


    rolle = property(__rolle.value, __rolle.set, None, None)


    # Attribute infoType uses Python identifier infoType
    __infoType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'infoType'), 'infoType', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_40_infoType', STD_ANON_93, fixed=True, unicode_default='SIGN', required=True)
    __infoType._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 981, 3)
    __infoType._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 981, 3)

    infoType = property(__infoType.value, __infoType.set, None, None)


    # Attribute register uses Python identifier register
    __register = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'register'), 'register', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_40_register', STD_ANON_94, fixed=True, unicode_default='ER', required=True)
    __register._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 986, 3)
    __register._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 986, 3)

    register = property(__register.value, __register.set, None, None)

    _ElementMap.update({
        __signaturTekst.name() : __signaturTekst,
        __rolle.name() : __rolle
    })
    _AttributeMap.update({
        __infoType.name() : __infoType,
        __register.name() : __register
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_41 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 965, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}person uses Python identifier person
    __person = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'person'), 'person', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_41_httpschema_brreg_nointefintegrasjonERFVperson', True, pyxb.utils.utility.Location('integrasjonERFV.xsd', 167, 1), )


    person = property(__person.value, __person.set, None, None)


    # Attribute rolletype uses Python identifier rolletype
    __rolletype = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rolletype'), 'rolletype', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_41_rolletype', STD_ANON_92, required=True)
    __rolletype._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 969, 6)
    __rolletype._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 969, 6)

    rolletype = property(__rolletype.value, __rolletype.set, None, None)

    _ElementMap.update({
        __person.name() : __person
    })
    _AttributeMap.update({
        __rolletype.name() : __rolletype
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_42 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 1004, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://schema.brreg.no/intef/integrasjonERFV}rolle uses Python identifier rolle
    __rolle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rolle'), 'rolle', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_42_httpschema_brreg_nointefintegrasjonERFVrolle', True, pyxb.utils.utility.Location('integrasjonERFV.xsd', 148, 3), )


    rolle = property(__rolle.value, __rolle.set, None, None)


    # Attribute infoType uses Python identifier infoType
    __infoType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'infoType'), 'infoType', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_42_infoType', STD_ANON_95, fixed=True, unicode_default='STYR', required=True)
    __infoType._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 1006, 3)
    __infoType._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 1006, 3)

    infoType = property(__infoType.value, __infoType.set, None, None)


    # Attribute register uses Python identifier register
    __register = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'register'), 'register', '__httpschema_brreg_nointefintegrasjonERFV_CTD_ANON_42_register', STD_ANON_96, fixed=True, unicode_default='ER', required=True)
    __register._DeclarationLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 1011, 3)
    __register._UseLocation = pyxb.utils.utility.Location('integrasjonERFV.xsd', 1011, 3)

    register = property(__register.value, __register.set, None, None)

    _ElementMap.update({
        __rolle.name() : __rolle
    })
    _AttributeMap.update({
        __infoType.name() : __infoType,
        __register.name() : __register
    })



integrasjonERFV = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'integrasjonERFV'), CTD_ANON, documentation='Beskriver tjenesten integrasjon mot frivillighetsregisteret', location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 4, 1))
Namespace.addCategoryObject('elementBinding', integrasjonERFV.name().localName(), integrasjonERFV)

melding = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'melding'), CTD_ANON_2, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 74, 1))
Namespace.addCategoryObject('elementBinding', melding.name().localName(), melding)

nummer = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nummer'), STD_ANON_8, documentation='felleselement for nummer som har like egenskaper', location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 135, 1))
Namespace.addCategoryObject('elementBinding', nummer.name().localName(), nummer)

person = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'person'), CTD_ANON_3, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 167, 1))
Namespace.addCategoryObject('elementBinding', person.name().localName(), person)

organisasjonsform = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'organisasjonsform'), CTD_ANON_7, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 334, 1))
Namespace.addCategoryObject('elementBinding', organisasjonsform.name().localName(), organisasjonsform)

sakstype = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sakstype'), CTD_ANON_8, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 349, 1))
Namespace.addCategoryObject('elementBinding', sakstype.name().localName(), sakstype)

epost = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'epost'), CTD_ANON_9, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 403, 1))
Namespace.addCategoryObject('elementBinding', epost.name().localName(), epost)

forretningsAdresse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'forretningsAdresse'), CTD_ANON_10, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 440, 1))
Namespace.addCategoryObject('elementBinding', forretningsAdresse.name().localName(), forretningsAdresse)

hjemmeside = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hjemmeside'), CTD_ANON_11, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 579, 1))
Namespace.addCategoryObject('elementBinding', hjemmeside.name().localName(), hjemmeside)

navn = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'navn'), CTD_ANON_12, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 666, 1))
Namespace.addCategoryObject('elementBinding', navn.name().localName(), navn)

postAdresse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'postAdresse'), CTD_ANON_13, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 753, 1))
Namespace.addCategoryObject('elementBinding', postAdresse.name().localName(), postAdresse)

enhet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'enhet'), CTD_ANON_14, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 882, 1))
Namespace.addCategoryObject('elementBinding', enhet.name().localName(), enhet)

vedlegg = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vedlegg'), CTD_ANON_15, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 933, 1))
Namespace.addCategoryObject('elementBinding', vedlegg.name().localName(), vedlegg)

stiftelsesdato = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stiftelsesdato'), CTD_ANON_16, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 993, 1))
Namespace.addCategoryObject('elementBinding', stiftelsesdato.name().localName(), stiftelsesdato)

elektroniskVarslingsadresse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'elektroniskVarslingsadresse'), CTD_ANON_17, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 1018, 1))
Namespace.addCategoryObject('elementBinding', elektroniskVarslingsadresse.name().localName(), elektroniskVarslingsadresse)

header = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'header'), CTD_ANON_19, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 15, 1))
Namespace.addCategoryObject('elementBinding', header.name().localName(), header)

kontaktperson = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'kontaktperson'), CTD_ANON_21, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 188, 1))
Namespace.addCategoryObject('elementBinding', kontaktperson.name().localName(), kontaktperson)

aarsregnskapLeveres = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'aarsregnskapLeveres'), CTD_ANON_22, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 212, 1))
Namespace.addCategoryObject('elementBinding', aarsregnskapLeveres.name().localName(), aarsregnskapLeveres)

ansatte = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ansatte'), CTD_ANON_23, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 237, 1))
Namespace.addCategoryObject('elementBinding', ansatte.name().localName(), ansatte)

dagligLeder = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dagligLeder'), CTD_ANON_24, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 262, 1))
Namespace.addCategoryObject('elementBinding', dagligLeder.name().localName(), dagligLeder)

forretningsforer = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'forretningsforer'), CTD_ANON_25, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 286, 1))
Namespace.addCategoryObject('elementBinding', forretningsforer.name().localName(), forretningsforer)

regnskapsperiode = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'regnskapsperiode'), CTD_ANON_26, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 311, 1))
Namespace.addCategoryObject('elementBinding', regnskapsperiode.name().localName(), regnskapsperiode)

endringAvVedtekter = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'endringAvVedtekter'), CTD_ANON_27, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 379, 1))
Namespace.addCategoryObject('elementBinding', endringAvVedtekter.name().localName(), endringAvVedtekter)

formaal = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'formaal'), CTD_ANON_28, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 419, 1))
Namespace.addCategoryObject('elementBinding', formaal.name().localName(), formaal)

meldepliktVedtekter = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'meldepliktVedtekter'), CTD_ANON_29, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 525, 1))
Namespace.addCategoryObject('elementBinding', meldepliktVedtekter.name().localName(), meldepliktVedtekter)

grasrotandel = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'grasrotandel'), CTD_ANON_30, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 550, 1))
Namespace.addCategoryObject('elementBinding', grasrotandel.name().localName(), grasrotandel)

kategori = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'kategori'), CTD_ANON_31, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 595, 1))
Namespace.addCategoryObject('elementBinding', kategori.name().localName(), kategori)

kontonummer = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'kontonummer'), CTD_ANON_32, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 617, 1))
Namespace.addCategoryObject('elementBinding', kontonummer.name().localName(), kontonummer)

maalform = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'maalform'), CTD_ANON_33, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 641, 1))
Namespace.addCategoryObject('elementBinding', maalform.name().localName(), maalform)

mobil = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mobil'), CTD_ANON_34, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 714, 1))
Namespace.addCategoryObject('elementBinding', mobil.name().localName(), mobil)

nedleggelsesdato = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nedleggelsesdato'), CTD_ANON_35, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 731, 1))
Namespace.addCategoryObject('elementBinding', nedleggelsesdato.name().localName(), nedleggelsesdato)

prokura = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'prokura'), CTD_ANON_36, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 838, 1))
Namespace.addCategoryObject('elementBinding', prokura.name().localName(), prokura)

telefaks = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'telefaks'), CTD_ANON_38, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 895, 1))
Namespace.addCategoryObject('elementBinding', telefaks.name().localName(), telefaks)

telefon = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'telefon'), CTD_ANON_39, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 916, 1))
Namespace.addCategoryObject('elementBinding', telefon.name().localName(), telefon)

signatur = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'signatur'), CTD_ANON_40, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 947, 1))
Namespace.addCategoryObject('elementBinding', signatur.name().localName(), signatur)

styre = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'styre'), CTD_ANON_42, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 1003, 1))
Namespace.addCategoryObject('elementBinding', styre.name().localName(), styre)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'header'), CTD_ANON_19, scope=CTD_ANON, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 15, 1)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'melding'), CTD_ANON_2, scope=CTD_ANON, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 74, 1)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 11, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 10, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'melding')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 11, 4))
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




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ERstatus'), STD_ANON_3, scope=CTD_ANON_, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 45, 7)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FVstatus'), STD_ANON_4, scope=CTD_ANON_, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 54, 7)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ERstatus')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 45, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FVstatus')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 54, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'opplysningUtgaar'), STD_ANON_6, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 104, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'signerer'), STD_ANON_7, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 125, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'kontaktperson'), CTD_ANON_21, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 188, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'aarsregnskapLeveres'), CTD_ANON_22, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 212, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ansatte'), CTD_ANON_23, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 237, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dagligLeder'), CTD_ANON_24, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 262, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'forretningsforer'), CTD_ANON_25, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 286, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'regnskapsperiode'), CTD_ANON_26, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 311, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'endringAvVedtekter'), CTD_ANON_27, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 379, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'epost'), CTD_ANON_9, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 403, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'formaal'), CTD_ANON_28, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 419, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'forretningsAdresse'), CTD_ANON_10, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 440, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'meldepliktVedtekter'), CTD_ANON_29, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 525, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'grasrotandel'), CTD_ANON_30, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 550, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hjemmeside'), CTD_ANON_11, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 579, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'kategori'), CTD_ANON_31, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 595, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'kontonummer'), CTD_ANON_32, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 617, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'maalform'), CTD_ANON_33, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 641, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'navn'), CTD_ANON_12, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 666, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mobil'), CTD_ANON_34, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 714, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nedleggelsesdato'), CTD_ANON_35, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 731, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'postAdresse'), CTD_ANON_13, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 753, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'prokura'), CTD_ANON_36, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 838, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'telefaks'), CTD_ANON_38, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 895, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'telefon'), CTD_ANON_39, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 916, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vedlegg'), CTD_ANON_15, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 933, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'signatur'), CTD_ANON_40, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 947, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stiftelsesdato'), CTD_ANON_16, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 993, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'styre'), CTD_ANON_42, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 1003, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'elektroniskVarslingsadresse'), CTD_ANON_17, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 1018, 1)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 77, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 78, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 79, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 80, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 81, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 82, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 83, 4))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 84, 4))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 85, 4))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 86, 4))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 87, 4))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 88, 4))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 89, 4))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 90, 4))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 91, 4))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 92, 4))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 93, 4))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 94, 4))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 95, 4))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 96, 4))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 97, 4))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=3, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 98, 4))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 99, 4))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 100, 4))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 101, 4))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 102, 4))
    counters.add(cc_25)
    cc_26 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 103, 4))
    counters.add(cc_26)
    cc_27 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 104, 4))
    counters.add(cc_27)
    cc_28 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 124, 4))
    counters.add(cc_28)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'navn')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 77, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'stiftelsesdato')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 78, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'forretningsAdresse')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 79, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'postAdresse')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 80, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hjemmeside')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 81, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'epost')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 82, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'telefon')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 83, 4))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mobil')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 84, 4))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'telefaks')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 85, 4))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'formaal')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 86, 4))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'kontaktperson')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 87, 4))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dagligLeder')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 88, 4))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'forretningsforer')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 89, 4))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'styre')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 90, 4))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'elektroniskVarslingsadresse')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 91, 4))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'signatur')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 92, 4))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'prokura')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 93, 4))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'maalform')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 94, 4))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ansatte')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 95, 4))
    st_18 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nedleggelsesdato')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 96, 4))
    st_19 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'grasrotandel')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 97, 4))
    st_20 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'kategori')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 98, 4))
    st_21 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'kontonummer')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 99, 4))
    st_22 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'meldepliktVedtekter')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 100, 4))
    st_23 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'endringAvVedtekter')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 101, 4))
    st_24 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'aarsregnskapLeveres')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 102, 4))
    st_25 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'regnskapsperiode')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 103, 4))
    st_26 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'opplysningUtgaar')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 104, 4))
    st_27 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vedlegg')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 124, 4))
    st_28 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'signerer')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 125, 4))
    st_29 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_29)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
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
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
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
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
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
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
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
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
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
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
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
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
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
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
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
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
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
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
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
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
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
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
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
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
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
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_21, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_21, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_22, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_22, False) ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_23, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_23, False) ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_24, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_24, False) ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_25, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_25, False) ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_26, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_26, False) ]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_27, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_27, False) ]))
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_28, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_28, False) ]))
    st_28._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_29, [
         ]))
    st_29._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fodselsnr'), STD_ANON_10, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 170, 4)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'slektsnavn'), STD_ANON_11, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 177, 4)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fodselsnr')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 170, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'slektsnavn')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 177, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_3()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'person'), CTD_ANON_3, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 167, 1)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'person')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 194, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_4()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'person'), CTD_ANON_3, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 167, 1)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'person')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 268, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_5()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'person'), CTD_ANON_3, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 167, 1)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'enhet'), CTD_ANON_14, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 882, 1)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 292, 7))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 293, 7))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'person')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 292, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'enhet')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 293, 7))
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
CTD_ANON_6._Automaton = _BuildAutomaton_6()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orgform'), STD_ANON_27, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 337, 4), fixed=True, unicode_default='FLI'))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orgform')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 337, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_7()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hovedsakstype'), STD_ANON_28, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 352, 4)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'undersakstype'), STD_ANON_29, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 363, 4)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hovedsakstype')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 352, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'undersakstype')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 363, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_8()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'epostAdresse'), STD_ANON_33, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 406, 4)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'epostAdresse')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 406, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_9()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'adresse1'), STD_ANON_37, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 443, 4)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'adresse2'), STD_ANON_38, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 451, 4)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'adresse3'), STD_ANON_39, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 459, 4)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'postnr'), STD_ANON_40, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 467, 4)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'poststed'), STD_ANON_41, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 474, 4)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'utenlandskPoststed'), STD_ANON_42, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 482, 4)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'kommunenummer'), STD_ANON_43, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 490, 4)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'kommune'), STD_ANON_44, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 497, 4)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'landkode'), STD_ANON_45, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 505, 4)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'land'), STD_ANON_46, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 512, 4)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 443, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 451, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 459, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 467, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 474, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 482, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 490, 4))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 497, 4))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'adresse1')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 443, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'adresse2')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 451, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'adresse3')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 459, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'postnr')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 467, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'poststed')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 474, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'utenlandskPoststed')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 482, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'kommunenummer')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 490, 4))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'kommune')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 497, 4))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'landkode')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 505, 4))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'land')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 512, 4))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
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
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
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
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_10()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'url'), STD_ANON_53, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 582, 4)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'url')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 582, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_11()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'navn1'), STD_ANON_62, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 669, 4)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'navn2'), STD_ANON_63, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 677, 4)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'navn3'), STD_ANON_64, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 685, 4)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'navn4'), STD_ANON_65, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 693, 4)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'navn5'), STD_ANON_66, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 701, 4)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 677, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 685, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 693, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 701, 4))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'navn1')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 669, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'navn2')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 677, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'navn3')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 685, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'navn4')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 693, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'navn5')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 701, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_12()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'adresse1'), STD_ANON_71, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 756, 4)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'adresse2'), STD_ANON_72, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 764, 4)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'adresse3'), STD_ANON_73, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 772, 4)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'postnr'), STD_ANON_74, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 780, 4)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'poststed'), STD_ANON_75, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 787, 4)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'utenlandskPoststed'), STD_ANON_76, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 795, 4)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'kommunenummer'), STD_ANON_77, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 803, 4)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'kommune'), STD_ANON_78, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 810, 4)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'landkode'), STD_ANON_79, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 818, 4)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'land'), STD_ANON_80, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 825, 4)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 756, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 764, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 772, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 780, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 787, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 795, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 803, 4))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 810, 4))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'adresse1')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 756, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'adresse2')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 764, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'adresse3')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 772, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'postnr')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 780, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'poststed')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 787, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'utenlandskPoststed')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 795, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'kommunenummer')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 803, 4))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'kommune')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 810, 4))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'landkode')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 818, 4))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'land')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 825, 4))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
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
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
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
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_13()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orgnr'), STD_ANON_85, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 885, 4)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orgnr')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 885, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_14()




CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vedleggsType'), STD_ANON_90, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 936, 4)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vedleggsType')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 936, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_15()




CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'epostadresse'), STD_ANON_97, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 1021, 4)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mobil'), CTD_ANON_18, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 1029, 4)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 1021, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 1029, 4))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'epostadresse')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 1021, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mobil')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 1029, 4))
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
CTD_ANON_17._Automaton = _BuildAutomaton_16()




CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'prefiks'), STD_ANON_98, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 1032, 7)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mobilnummer'), STD_ANON_99, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 1040, 7)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 1032, 7))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 1040, 7))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'prefiks')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 1032, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mobilnummer')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 1040, 7))
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
CTD_ANON_18._Automaton = _BuildAutomaton_17()




CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SLsysId'), STD_ANON, scope=CTD_ANON_19, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 18, 4)))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SLsysMeldingsId'), STD_ANON_, scope=CTD_ANON_19, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 25, 4)))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'organisasjonsnummer'), STD_ANON_2, scope=CTD_ANON_19, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 34, 4)))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'status'), CTD_ANON_, scope=CTD_ANON_19, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 42, 4)))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'organisasjonsform'), CTD_ANON_7, scope=CTD_ANON_19, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 334, 1)))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sakstype'), CTD_ANON_8, scope=CTD_ANON_19, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 349, 1)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 34, 4))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SLsysId')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 18, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SLsysMeldingsId')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 25, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sakstype')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 33, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'organisasjonsnummer')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 34, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'organisasjonsform')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 41, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'status')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 42, 4))
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
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_19._Automaton = _BuildAutomaton_18()




CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'person'), CTD_ANON_3, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 167, 1)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'enhet'), CTD_ANON_14, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 882, 1)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 151, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 152, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'person')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 151, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'enhet')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 152, 6))
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
CTD_ANON_20._Automaton = _BuildAutomaton_19()




CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rolle'), CTD_ANON_4, scope=CTD_ANON_21, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 191, 4)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 191, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rolle')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 191, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_21._Automaton = _BuildAutomaton_20()




CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'skalLevere'), STD_ANON_14, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 215, 4)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'skalLevere')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 215, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_22._Automaton = _BuildAutomaton_21()




CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'harAnsatte'), STD_ANON_17, scope=CTD_ANON_23, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 240, 4)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'harAnsatte')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 240, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_23._Automaton = _BuildAutomaton_22()




CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rolle'), CTD_ANON_5, scope=CTD_ANON_24, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 265, 4)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 265, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rolle')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 265, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_24._Automaton = _BuildAutomaton_23()




CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rolle'), CTD_ANON_6, scope=CTD_ANON_25, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 289, 4)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 289, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rolle')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 289, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_25._Automaton = _BuildAutomaton_24()




CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'datoMaaned'), STD_ANON_24, scope=CTD_ANON_26, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 314, 4)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'datoMaaned')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 314, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_26._Automaton = _BuildAutomaton_25()




CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'endringMeldt'), STD_ANON_30, scope=CTD_ANON_27, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 382, 4)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'endringMeldt')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 382, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_27._Automaton = _BuildAutomaton_26()




CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'formaalTekst'), STD_ANON_34, scope=CTD_ANON_28, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 422, 4)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 422, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'formaalTekst')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 422, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_28._Automaton = _BuildAutomaton_27()




CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'skalRegistreres'), STD_ANON_47, scope=CTD_ANON_29, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 528, 4)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'skalRegistreres')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 528, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_29._Automaton = _BuildAutomaton_28()




CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'skalDelta'), STD_ANON_50, scope=CTD_ANON_30, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 553, 4)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'skalDelta')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 553, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_30._Automaton = _BuildAutomaton_29()




CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'kode'), pyxb.binding.datatypes.int, scope=CTD_ANON_31, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 598, 4)))

CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rangering'), pyxb.binding.datatypes.short, scope=CTD_ANON_31, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 599, 4), unicode_default='1'))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'kode')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 598, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rangering')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 599, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_31._Automaton = _BuildAutomaton_30()




CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nummer'), STD_ANON_56, scope=CTD_ANON_32, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 620, 4)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nummer')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 620, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_32._Automaton = _BuildAutomaton_31()




CTD_ANON_33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'maalformKode'), STD_ANON_59, scope=CTD_ANON_33, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 644, 4)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'maalformKode')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 644, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_33._Automaton = _BuildAutomaton_32()




CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nummer'), STD_ANON_8, scope=CTD_ANON_34, documentation='felleselement for nummer som har like egenskaper', location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 135, 1)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nummer')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 717, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_34._Automaton = _BuildAutomaton_33()




CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'prokuraTekst'), STD_ANON_81, scope=CTD_ANON_36, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 841, 4)))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rolle'), CTD_ANON_37, scope=CTD_ANON_36, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 853, 4)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 841, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 853, 4))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'prokuraTekst')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 841, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rolle')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 853, 4))
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
CTD_ANON_36._Automaton = _BuildAutomaton_34()




CTD_ANON_37._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'person'), CTD_ANON_3, scope=CTD_ANON_37, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 167, 1)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'person')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 856, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_37._Automaton = _BuildAutomaton_35()




CTD_ANON_38._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nummer'), STD_ANON_8, scope=CTD_ANON_38, documentation='felleselement for nummer som har like egenskaper', location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 135, 1)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nummer')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 898, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_38._Automaton = _BuildAutomaton_36()




CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nummer'), STD_ANON_8, scope=CTD_ANON_39, documentation='felleselement for nummer som har like egenskaper', location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 135, 1)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nummer')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 919, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_39._Automaton = _BuildAutomaton_37()




CTD_ANON_40._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'signaturTekst'), STD_ANON_91, scope=CTD_ANON_40, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 950, 4)))

CTD_ANON_40._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rolle'), CTD_ANON_41, scope=CTD_ANON_40, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 964, 4)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 950, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('integrasjonERFV.xsd', 964, 4))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_40._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'signaturTekst')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 950, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_40._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rolle')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 964, 4))
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
CTD_ANON_40._Automaton = _BuildAutomaton_38()




CTD_ANON_41._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'person'), CTD_ANON_3, scope=CTD_ANON_41, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 167, 1)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_41._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'person')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 967, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_41._Automaton = _BuildAutomaton_39()




CTD_ANON_42._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rolle'), CTD_ANON_20, scope=CTD_ANON_42, location=pyxb.utils.utility.Location('integrasjonERFV.xsd', 148, 3)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_42._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rolle')), pyxb.utils.utility.Location('integrasjonERFV.xsd', 148, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_42._Automaton = _BuildAutomaton_40()
