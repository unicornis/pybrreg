from . import output_fields


def concat_string_fields(data, keys, separator=" "):
    values = [data.get(key) for key in keys if data.get(key)]
    return separator.join(values)


class BrregField(object):

    def __init__(self, path):
        self.path = path

    def transformer(self, data):
        raise NotImplementedError

    def transform(self, data):
        return self.transformer(data)


class LimitMixin(object):

    def __init__(self, *args, **kwargs):
        self.where = kwargs.pop('where')
        super(LimitMixin, self).__init__(*args, **kwargs)

    def limit(self, data):
        return [element for element in data if element.get(self.where[0]) == self.where[1]]

    def transform(self, data):
        if self.where:
            data = self.limit(data)
        return super(LimitMixin, self).transform(data) if data else None


class Text(BrregField):

    def transformer(self, data):
        return output_fields.plain_string(data['#text'])


class OrganisationName(BrregField):

    def transformer(self, data):
        return output_fields.plain_string(concat_string_fields(data, ['navn1', 'navn2', 'navn3', 'navn4', 'navn5']))


class Address(BrregField):

    def transformer(self, data):
        return output_fields.address(
            street_address=concat_string_fields(
                data,
                ['adresse1', 'adresse2', 'adresse3'],
                separator=";"
            ),
            zip_code=data.get('postnr'),
            city=data.get('poststed'),
            municipality_number=data.get('kommunenummer'),
            country_code=data.get('landkode'),
            country=data.get('land')
        )


class Language(BrregField):

    def transformer(self, data):
        return output_fields.coded_name(data.get('maalformKode'), data.get('maalformTekst'))


class OrganisationType(BrregField):

    def transformer(self, data):
        return output_fields.coded_description(data.get('orgform'), data.get('orgformBeskrivelse'))


def _person_adaptor(person_data):
    return output_fields.person_with_role(
        name=concat_string_fields(person_data, ['fornavn', 'mellomnavn', 'slektsnavn']),
        resigned=person_data.get('fratraadt') != 'N',
        birth_date=person_data.get('fodselsdato'),
    )


class Person(BrregField):

    def transformer(self, data):
        return _person_adaptor(data)


class PersonOrPersons(LimitMixin, BrregField):

    def transformer(self, data):
        person_or_persons = data[0].get('person')
        if isinstance(person_or_persons, list):
            return [_person_adaptor(person) for person in person_or_persons]
        else:
            return [_person_adaptor(person_or_persons)]


def _entity_adaptor(entity_data):
    return output_fields.entity_with_role(
        name=concat_string_fields(entity_data, ['navn1', 'navn2', 'navn3']),
        resigned=entity_data.get('fratraadt') != 'N',
        organisation_number=entity_data.get('orgnr'),
    )


class EntityOrEntities(BrregField):

    def transformer(self, data):
        entity_or_entities = data.get('enhet')
        if isinstance(entity_or_entities, list):
            return [_entity_adaptor(entity) for entity in entity_or_entities]
        else:
            return [_entity_adaptor(entity_or_entities)]


class RegistrationDate(BrregField):

    def transformer(self, data):
        return output_fields.plain_string(data.get('@registreringsDato'))


class RankedCategories(BrregField):

    def _category(self, brreg_dict):
        return {
            'code': brreg_dict['kode'],
            'description': brreg_dict['beskrivelse']
        }

    def transformer(self, data):
        if isinstance(data, dict):
            return [self._category(data)]

        sorted_categories = sorted([
            [int(category['rangering']), self._category(category)]
            for category in data
        ],  key=lambda l: l[0])
        return [category[1] for category in sorted_categories]
