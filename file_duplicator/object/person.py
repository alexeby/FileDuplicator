class Person:
    def __init__(self, first_name=None, middle_name=None, last_name=None, full_name=None, alias=None, maiden_name=None,
                 mothers_maiden_name=None, title=None, suffix=None, tax_id=None, birth_date=None, death_date=None,
                 gender=None, contact=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.full_name = full_name
        self.alias = alias
        self.maiden_name = maiden_name
        self.mothers_maiden_name = mothers_maiden_name
        self.title = title
        self.suffix = suffix
        self.tax_id = tax_id
        self.birth_date = birth_date
        self.death_date = death_date
        self.gender = gender
        self.contact = contact

    def get_first_name(self):
        return self.first_name

    def get_middle_name(self):
        return self.middle_name

    def get_last_name(self):
        return self.last_name

    def get_full_name(self):
        return self.full_name

    def get_alias(self):
        return self.alias

    def get_maiden_name(self):
        return self.maiden_name

    def get_mothers_maiden_name(self):
        return self.mothers_maiden_name

    def get_title(self):
        return self.title

    def get_suffix(self):
        return self.suffix

    def get_tax_id(self):
        return self.tax_id

    def get_birth_date(self):
        return self.birth_date

    def get_death_date(self):
        return self.death_date

    def get_gender(self):
        return self.gender

    def get_contact(self):
        return self.contact

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_middle_name(self, middle_name):
        self.middle_name = middle_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_full_name(self, full_name):
        self.full_name = full_name

    def set_alias(self, alias):
        self.alias = alias

    def set_maiden_name(self, maiden_name):
        self.maiden_name = maiden_name

    def set_mothers_maiden_name(self, mothers_maiden_name):
        self.mothers_maiden_name = mothers_maiden_name

    def set_title(self, title):
        self.title = title

    def set_suffix(self, suffix):
        self.suffix = suffix

    def set_tax_id(self, tax_id):
        self.tax_id = tax_id

    def set_birth_date(self, birth_date):
        self.birth_date = birth_date

    def set_death_date(self, death_date):
        self.death_date = death_date

    def set_gender(self, gender):
        self.gender = gender

    def set_contact(self, contact):
        self.contact = contact


