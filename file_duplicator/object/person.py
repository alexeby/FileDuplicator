class Person:
    def __init__(self, first_name=None, middle_name=None, last_name=None, full_name=None,
                 title=None, tax_id=None, birth_date=None, gender=None, contact=None):
        self.first_name: str = first_name
        self.middle_name: str = middle_name
        self.last_name: str = last_name
        self.full_name: str = full_name
        self.title: str = title
        self.tax_id: str = tax_id
        self.birth_date: str = birth_date
        self.gender: str = gender
        self.contact: str = contact


