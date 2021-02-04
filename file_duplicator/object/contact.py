class Contact:
    def __init__(self, street1=None, street2=None, city=None, state=None, postal_code_prefix=None,
                 postal_code_suffix=None, country=None, home_phone=None, work_phone=None, mobile_phone=None, pager=None,
                 fax=None, email=None, secondary_email=None, county=None, latitude=None, longitude=None):
        self.street1 = street1
        self.street2 = street2
        self.city = city
        self.state = state
        self.postal_code_prefix = postal_code_prefix
        self.postal_code_suffix = postal_code_suffix
        self.country = country
        self.home_phone = home_phone
        self.work_phone = work_phone
        self.mobile_phone = mobile_phone
        self.pager = pager
        self.fax = fax
        self.email = email
        self.secondary_email = secondary_email
        self.county = county
        self.latitude = latitude
        self.longitude = longitude

    def get_street1(self):
        return self.street1

    def get_street2(self):
        return self.street2

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_postal_code_prefix(self):
        return self.postal_code_prefix

    def get_postal_code_suffix(self):
        return self.postal_code_suffix

    def get_country(self):
        return self.country

    def get_home_phone(self):
        return self.home_phone

    def get_work_phone(self):
        return self.work_phone

    def get_mobile_phone(self):
        return self.mobile_phone

    def get_pager(self):
        return self.pager

    def get_fax(self):
        return self.fax

    def get_email(self):
        return self.email

    def get_secondary_email(self):
        return self.secondary_email

    def get_county(self):
        return self.county

    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longitude

    def set_street1(self, street1):
        self.street1 = street1

    def set_street2(self, street2):
        self.street2 = street2

    def set_city(self, city):
        self.city = city

    def set_state(self, state):
        self.state = state

    def set_postal_code_prefix(self, postal_code_prefix):
        self.postal_code_prefix = postal_code_prefix

    def set_postal_code_suffix(self, postal_code_suffix):
        self.postal_code_suffix = postal_code_suffix

    def set_country(self, country):
        self.country = country

    def set_home_phone(self, home_phone):
        self.home_phone = home_phone

    def set_work_phone(self, work_phone):
        self.work_phone = work_phone

    def set_mobile_phone(self, mobile_phone):
        self.mobile_phone = mobile_phone

    def set_pager(self, pager):
        self.pager = pager

    def set_fax(self, fax):
        self.fax = fax

    def set_email(self, email):
        self.email = email

    def set_secondary_email(self, secondary_email):
        self.secondary_email = secondary_email

    def set_county(self, county):
        self.county = county

    def set_latitude(self, latitude):
        self.latitude = latitude

    def set_longitude(self, longitude):
        self.longitude = longitude
