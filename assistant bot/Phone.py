
from Field import Field

class Phone(Field):
    
    def __init__(self, value):
        

        if not self.validate_phone(value):
            raise ValueError('Invalid phone number.')

        self.value = self.normalize_phone(value)

    def __str__(self):
        
        return str(self.value)

    @staticmethod
    def validate_phone(phone):
        
        if not phone:
            return False  

        if phone[0] == '+':
            return phone[1:].isdigit()
        else:
            return phone.isdigit()

    @staticmethod
    def normalize_phone(phone):
        
        digits_only = ''.join(c for c in phone if c.isdigit())
        if digits_only and digits_only[0] == '0':  
            digits_only = digits_only[1:]
        if len(digits_only) > 10:  
            digits_only = digits_only[:10]

        if digits_only:
            return '+' + digits_only if len(digits_only) > 9 else digits_only
        else:
            return ''
        
    def save_to_disk(self, filename):

        try:
            with open(filename, "w") as file:
                file.write(self.value)
        except IOError as e:
            raise IOError(f"Error saving phone number to file: {e}")