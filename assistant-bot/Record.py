from Name import Name
from Phone import Phone
from Email import Email
from Address import Address
from Birthday import Birthday

class Record:
    def __init__(self, name, phone, email=None, address=None, birthday=None):
        self.name = Name(name)
        self.phone = Phone(phone)
        self.email = Email(email) if email else None
        self.address = Address(address) if address else None
        self.birthday = Birthday(birthday) if birthday else None

    def update_name(self, new_name):
        self.name = Name(new_name)

    def update_phone(self, new_phone):
        self.phone = Phone(new_phone)

    def update_address(self, new_address):
        self.address = Address(new_address)

    def update_email(self, new_email):
        self.email = Email(new_email)

    def update_birthday(self, new_birthday):
        self.birthday = Birthday(new_birthday)

    def __str__(self):
        return (
            f"Name: {self.name}, Phone: {self.phone}, "
            f"Address: {self.address}, Email: {self.email}, Birthday: {self.birthday}"
        )