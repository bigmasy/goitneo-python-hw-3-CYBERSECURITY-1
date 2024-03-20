import re


class Email:
    def __init__(self, value):
        if not self.validate_email(value):
            raise ValueError("Invalid email format!")
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not self.validate_email(new_value):
            raise ValueError("Invalid email format!")
        self._value = new_value

    def validate_email(self, email) :
        if not email :
            return False
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(pattern, email):
            return True
        else :
            return False


    def __str__(self):
        return self._value