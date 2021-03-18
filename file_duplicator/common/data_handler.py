from .formatter import *
import math
import random
from .constants import Constants as c
from ..setup.mappings import Mappings as m
from .file_utils import get_key


def get_person_value(tok, person):
    contact = person.contact
    switcher = {
        c.FIRST_NAME: person.first_name,
        c.MIDDLE_NAME: person.middle_name,
        c.LAST_NAME: person.last_name,
        c.FULL_NAME: person.full_name,
        c.TITLE: person.title,
        c.TAX_ID: person.tax_id,
        c.BIRTH_DATE: person.birth_date,
        c.AGE: person.age,
        c.GENDER: person.gender,
        c.NAT: person.nat,
        c.USERNAME: person.username,
        c.PASSWORD: person.password,

        c.STREET: contact.street,
        c.CITY: contact.city,
        c.STATE: contact.state,
        c.POSTAL_CODE: contact.postal_code,
        c.COUNTRY: contact.country,
        c.HOME_PHONE: contact.home_phone,
        c.MOBILE_PHONE: contact.mobile_phone,
        c.EMAIL: contact.email,
        c.LATITUDE: contact.latitude,
        c.LONGITUDE: contact.longitude
    }
    return switcher[tok]


def process(token: str, person):
    if token.upper().startswith(c.PERSON) or token.upper().startswith(c.ADDRESS):
        token_value = get_key(token.upper().split('.')[1], m.mapping_dictionary)
        return get_person_value(token_value, person)
    else:
        return str(eval(token))
    pass
