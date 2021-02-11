class Contact:
    def __init__(self, street=None, city=None, state=None, postal_code=None, country=None, home_phone=None,
                 mobile_phone=None, email=None, latitude=None, longitude=None):
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

