from .formatter import *
from .constants import Constants as c


def get_person_value(tok, person):
    switcher = {
        c.first_name: person.get_first_name(),
        c.middle_name: person.get_middle_name(),
        c.last_name: person.get_last_name(),
        c.full_name: person.get_full_name(),
        c.title: person.get_title(),
        c.tax_id: person.get_tax_id(),
        c.birth_date: person.get_birth_date(),
        c.gender: person.get_gender()
    }
    return switcher.get(tok)


def get_contact_value(tok, person):
    contact = person.get_contact()
    switcher = {
        c.street1: contact.get_street1(),
        c.city: contact.get_city(),
        c.state: contact.get_state(),
        c.postal_code_prefix: contact.get_postal_code_prefix(),
        c.country: contact.get_country(),
        c.home_phone: contact.get_home_phone(),
        c.mobile_phone: contact.get_mobile_phone(),
        c.email: contact.get_email(),
        c.latitude: contact.get_latitude(),
        c.longitude: contact.get_longitude()
    }
    return switcher.get(tok)


def process(token: str, person):
    token_upper = token.upper()
    if token_upper.startswith(c.person or c.party):
        return get_person_value(token_upper.split('.')[1], person)
    elif token_upper.startswith('Contact.'):
        return get_contact_value(token_upper.split('.')[1], person)
    else:
        return eval(token)
    pass
