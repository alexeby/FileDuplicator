import configparser
from ..common.constants import Constants as c
import logging

# Init config parser
parser = configparser.ConfigParser()
parser.read('./setup/mappings.ini')

logger = logging.getLogger(__name__)


class Mappings:

    config_section = 'Mappings'
    MAPPINGS = []
    mapping_dictionary = {}

    first_name = parser.get(config_section, c.FIRST_NAME).upper().split('|')
    mapping_dictionary[c.FIRST_NAME] = first_name
    MAPPINGS.extend(first_name)
    
    middle_name = parser.get(config_section, c.MIDDLE_NAME).upper().split('|')
    mapping_dictionary[c.MIDDLE_NAME] = middle_name
    MAPPINGS.extend(middle_name)
    
    last_name = parser.get(config_section, c.LAST_NAME).upper().split('|')
    mapping_dictionary[c.LAST_NAME] = last_name
    MAPPINGS.extend(last_name)
    
    full_name = parser.get(config_section, c.FULL_NAME).upper().split('|')
    mapping_dictionary[c.FULL_NAME] = full_name
    MAPPINGS.extend(full_name)
    
    title = parser.get(config_section, c.TITLE).upper().split('|')
    mapping_dictionary[c.TITLE] = title
    MAPPINGS.extend(title)
    
    tax_id = parser.get(config_section, c.TAX_ID).upper().split('|')
    mapping_dictionary[c.TAX_ID] = tax_id
    MAPPINGS.extend(tax_id)
    
    birth_date = parser.get(config_section, c.BIRTH_DATE).upper().split('|')
    mapping_dictionary[c.BIRTH_DATE] = birth_date
    MAPPINGS.extend(birth_date)

    age = parser.get(config_section, c.AGE).upper().split('|')
    mapping_dictionary[c.AGE] = age
    MAPPINGS.extend(age)

    gender = parser.get(config_section, c.GENDER).upper().split('|')
    mapping_dictionary[c.GENDER] = gender
    MAPPINGS.extend(gender)

    nat = parser.get(config_section, c.NAT).upper().split('|')
    mapping_dictionary[c.NAT] = nat
    MAPPINGS.extend(nat)

    username = parser.get(config_section, c.USERNAME).upper().split('|')
    mapping_dictionary[c.USERNAME] = username
    MAPPINGS.extend(username)

    password = parser.get(config_section, c.PASSWORD).upper().split('|')
    mapping_dictionary[c.PASSWORD] = password
    MAPPINGS.extend(password)

    street = parser.get(config_section, c.STREET).upper().split('|')
    mapping_dictionary[c.STREET] = street
    MAPPINGS.extend(street)
    
    city = parser.get(config_section, c.CITY).upper().split('|')
    mapping_dictionary[c.CITY] = city
    MAPPINGS.extend(city)
    
    state = parser.get(config_section, c.STATE).upper().split('|')
    mapping_dictionary[c.STATE] = state
    MAPPINGS.extend(state)
    
    postal_code = parser.get(config_section, c.POSTAL_CODE).upper().split('|')
    mapping_dictionary[c.POSTAL_CODE] = postal_code
    MAPPINGS.extend(postal_code)
    
    country = parser.get(config_section, c.COUNTRY).upper().split('|')
    mapping_dictionary[c.COUNTRY] = country
    MAPPINGS.extend(country)
    
    home_phone = parser.get(config_section, c.HOME_PHONE).upper().split('|')
    mapping_dictionary[c.HOME_PHONE] = home_phone
    MAPPINGS.extend(home_phone)
    
    mobile_phone = parser.get(config_section, c.MOBILE_PHONE).upper().split('|')
    mapping_dictionary[c.MOBILE_PHONE] = mobile_phone
    MAPPINGS.extend(mobile_phone)
    
    email = parser.get(config_section, c.EMAIL).upper().split('|')
    mapping_dictionary[c.EMAIL] = email
    MAPPINGS.extend(email)
    
    latitude = parser.get(config_section, c.LATITUDE).upper().split('|')
    mapping_dictionary[c.LATITUDE] = latitude
    MAPPINGS.extend(latitude)
    
    longitude = parser.get(config_section, c.LONGITUDE).upper().split('|')
    mapping_dictionary[c.LONGITUDE] = longitude
    MAPPINGS.extend(longitude)
