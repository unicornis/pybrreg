"""PyBrreg fields.

The functions in this module determine the structure of the fields that compose the processed output.
"""


def plain_string(string):
    return string


def coded_name(code, name):
    return {
        'code': code,
        'name': name,
    }


def coded_description(code, description):
    return {
        'code': code,
        'description': description,
    }


def entity_with_role(name, resigned, organisation_number):
    return {
        'name': name,
        'resigned': resigned,
        'organisation_number': organisation_number,
    }


def person_with_role(name, resigned, birth_date):
    return {
        'name': name,
        'resigned': resigned,
        'birth_date': birth_date,
    }


def address(street_address, zip_code, city, municipality_number, country_code, country):
    return {
        'address': street_address,
        'zip_code': zip_code,
        'city': city,
        'municipality_number': municipality_number,
        'country_code': country_code,
        'country': country,
    }
