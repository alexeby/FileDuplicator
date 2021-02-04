from .person import Person
from .contact import Contact
import json
from types import SimpleNamespace
from ..common.dict_translator import *


class ObjectMapper:

    json_data_obj = None

    def __init__(self, json_data: dict):
        json_data_str = json.dumps(json_data)
        self.json_data_obj = json.loads(json_data_str, object_hook=lambda d: SimpleNamespace(**d))

    def map_contact(self):
        contact = Contact()
        jdo = self.json_data_obj

        contact.set_street1(str(jdo.location.street.number) + ' ' + jdo.location.street.name)
        contact.set_city(jdo.location.city)
        contact.set_state(state_abbreviation[jdo.location.state])
        contact.set_postal_code_prefix(jdo.location.postcode)
        contact.set_country(jdo.location.country)
        contact.set_home_phone(jdo.phone)
        contact.set_mobile_phone(jdo.cell)
        contact.set_email(jdo.email)
        # contact.set_county()
        contact.set_latitude(jdo.location.coordinates.latitude)
        contact.set_longitude(jdo.location.coordinates.longitude)
        return contact

    def map_person(self):
        person = Person()
        jdo = self.json_data_obj

        person.set_first_name(jdo.name.first)
        person.set_middle_name(jdo.name.first+jdo.name.last)
        person.set_last_name(jdo.name.last)
        person.set_full_name(jdo.name.first + ' ' + jdo.name.last)
        person.set_title(jdo.name.title)
        person.set_tax_id(jdo.id.value)
        person.set_birth_date(jdo.dob.date)
        person.set_gender(sex[jdo.gender])
        person.set_contact(self.map_contact())
        return person


