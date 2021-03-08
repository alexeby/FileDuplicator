from .contact import Contact


class Person:
    def __init__(self, first_name='', middle_name='', last_name='', full_name='',
                 title='', tax_id='', birth_date='', gender='', contact=Contact()):
        self.first_name: str = first_name
        self.middle_name: str = middle_name
        self.last_name: str = last_name
        self.full_name: str = full_name
        self.title: str = title
        self.tax_id: str = tax_id
        self.birth_date: str = birth_date
        self.gender: str = gender
        self.contact: Contact = contact
