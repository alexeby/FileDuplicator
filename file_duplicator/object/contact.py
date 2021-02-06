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

