class Contact:
    def __init__(self, street='', city='', state='', postal_code='', country='', home_phone='',
                 mobile_phone='', email='', latitude='', longitude=''):
        self.street: str = street
        self.city: str = city
        self.state: str = state
        self.postal_code: str = postal_code
        self.country: str = country
        self.home_phone: str = home_phone
        self.mobile_phone: str = mobile_phone
        self.email: str = email
        self.latitude: str = latitude
        self.longitude: str = longitude

