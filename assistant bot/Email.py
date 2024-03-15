import re


class Email() :

    def validate_email(self, email) :
        if not email :
            return False
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(pattern, email):
            return True
        else :
            return False

    def edit_email(self, email) :
        if self.validate_email(email) :
            return email
        else :
            raise ValueError('Invalid email.')

    def init(self, value) :
        if not self.validate_email(value):
            raise ValueError('Invalid email.')