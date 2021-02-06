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

        contact.street1 = str(jdo.location.street.number) + ' ' + jdo.location.street.name
        contact.city = jdo.location.city
        contact.state = state_abbreviation[jdo.location.state]
        contact.postal_code_prefix = jdo.location.postcode
        contact.country = jdo.location.country
        contact.home_phone = jdo.phone
        contact.mobile_phone = jdo.cell
        contact.email = jdo.email
        # contact.county
        contact.latitude = jdo.location.coordinates.latitude
        contact.longitude = jdo.location.coordinates.longitude
        return contact

    def map_person(self):
        person = Person()
        jdo = self.json_data_obj

        person.first_name = jdo.name.first
        person.middle_name = jdo.name.first + jdo.name.last
        person.last_name = jdo.name.last
        person.full_name = jdo.name.first + ' ' + jdo.name.last
        person.title = jdo.name.title
        person.tax_id = jdo.id.value
        person.birth_date = jdo.dob.date
        person.gender = sex[jdo.gender]
        person.contact = self.map_contact()
        return person


