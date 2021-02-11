from .formatter import *
import math
import random
from .constants import Constants as c


def get_person_value(tok, person):
    switcher = {
        c.first_name: person.first_name,
        c.middle_name: person.middle_name,
        c.last_name: person.last_name,
        c.full_name: person.full_name,
        c.title: person.title,
        c.tax_id: person.tax_id,
        c.birth_date: person.birth_date,
        c.gender: person.gender
    }
    return switcher.get(tok)


def get_contact_value(tok, person):
    contact = person.contact
    switcher = {
        c.street: contact.street,
        c.city: contact.city,
        c.state: contact.state,
        c.postal_code: contact.postal_code,
        c.country: contact.country,
        c.home_phone: contact.home_phone,
        c.mobile_phone: contact.mobile_phone,
        c.email: contact.email,
        c.latitude: contact.latitude,
        c.longitude: contact.longitude
    }
    return switcher.get(tok)


def process(token: str, person):
    token_upper = token.upper()
    if token_upper.startswith(c.person):
        return get_person_value(token_upper.split('.')[1], person)
    elif token_upper.startswith(c.address):
        return get_contact_value(token_upper.split('.')[1], person)
    else:
        return str(eval(token))
    pass
