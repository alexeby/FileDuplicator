from .formatter import *
import math
import random
from .constants import Constants as c
from ..setup.mappings import Mappings as m


def get_key(val, dictionary: dict):
    for key, v in dictionary.items():
        if val in v:
            return key
    return ''


def get_person_value(tok, person):
    switcher = {
        person.first_name: m.first_name,
        person.middle_name: m.middle_name,
        person.last_name: m.last_name,
        person.full_name: m.full_name,
        person.title: m.title,
        person.tax_id: m.tax_id,
        person.birth_date: m.birth_date,
        person.age: m.age,
        person.gender: m.gender,
        person.nat: m.nat,
        person.username: m.username,
        person.password: m.password
    }
    return get_key(tok, switcher)


def get_contact_value(tok, person):
    contact = person.contact
    switcher = {
        contact.street: m.street,
        contact.city: m.city,
        contact.state: m.state,
        contact.postal_code: m.postal_code,
        contact.country: m.country,
        contact.home_phone: m.home_phone,
        contact.mobile_phone: m.mobile_phone,
        contact.email: m.email,
        contact.latitude: m.latitude,
        contact.longitude: m.longitude
    }
    return get_key(tok, switcher)


def process(token: str, person):
    token_upper = token.upper()
    if token_upper.startswith(c.person):
        return get_person_value(token_upper.split('.')[1], person)
    elif token_upper.startswith(c.address):
        return get_contact_value(token_upper.split('.')[1], person)
    else:
        return str(eval(token))
    pass
