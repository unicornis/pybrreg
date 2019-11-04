from pyxb_tools.converters import make_xml
from pyxb.exceptions_ import IncompleteElementContentError


def make_change_report_xml(data_dict):
    try:
        return make_xml(data_dict)
    except IncompleteElementContentError, e:
        raise Exception('Pyxb-error:\n {}'.format(e))
