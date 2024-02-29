from Field import Field

class Phone(Field):
    
    def __init__(self,value):
        if not self.validate_phone(value):
            raise ValueError('Phone number must be 10 digits')
        super().__init__(value)

    def __str__(self):
        return str(self.value)
    
    def validate_phone(self, phone):
        return len(phone) == 10 and phone.isdigit()