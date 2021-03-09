import configparser
import logging

# Init config parser
parser = configparser.ConfigParser()
parser.read('./setup/mappings.ini')

logger = logging.getLogger(__name__)


class Mappings:

    config_section = 'Mappings'
    MAPPINGS = []

    first_name = parser.get(config_section, 'first_name').upper().split('|')
    MAPPINGS.extend(first_name)
    
    middle_name = parser.get(config_section, 'middle_name').upper().split('|')
    MAPPINGS.extend(middle_name)
    
    last_name = parser.get(config_section, 'last_name').upper().split('|')
    MAPPINGS.extend(last_name)
    
    full_name = parser.get(config_section, 'full_name').upper().split('|')
    MAPPINGS.extend(full_name)
    
    title = parser.get(config_section, 'title').upper().split('|')
    MAPPINGS.extend(title)
    
    tax_id = parser.get(config_section, 'tax_id').upper().split('|')
    MAPPINGS.extend(tax_id)
    
    birth_date = parser.get(config_section, 'birth_date').upper().split('|')
    MAPPINGS.extend(birth_date)

    age = parser.get(config_section, 'age').upper().split('|')
    MAPPINGS.extend(age)

    gender = parser.get(config_section, 'gender').upper().split('|')
    MAPPINGS.extend(gender)

    nat = parser.get(config_section, 'nat').upper().split('|')
    MAPPINGS.extend(nat)

    username = parser.get(config_section, 'username').upper().split('|')
    MAPPINGS.extend(username)

    password = parser.get(config_section, 'password').upper().split('|')
    MAPPINGS.extend(password)

    street = parser.get(config_section, 'street').upper().split('|')
    MAPPINGS.extend(street)
    
    city = parser.get(config_section, 'city').upper().split('|')
    MAPPINGS.extend(city)
    
    state = parser.get(config_section, 'state').upper().split('|')
    MAPPINGS.extend(state)
    
    postal_code = parser.get(config_section, 'postal_code').upper().split('|')
    MAPPINGS.extend(postal_code)
    
    country = parser.get(config_section, 'country').upper().split('|')
    MAPPINGS.extend(country)
    
    home_phone = parser.get(config_section, 'home_phone').upper().split('|')
    MAPPINGS.extend(home_phone)
    
    mobile_phone = parser.get(config_section, 'mobile_phone').upper().split('|')
    MAPPINGS.extend(mobile_phone)
    
    email = parser.get(config_section, 'email').upper().split('|')
    MAPPINGS.extend(email)
    
    latitude = parser.get(config_section, 'latitude').upper().split('|')
    MAPPINGS.extend(latitude)
    
    longitude = parser.get(config_section, 'longitude').upper().split('|')
    MAPPINGS.extend(longitude)
