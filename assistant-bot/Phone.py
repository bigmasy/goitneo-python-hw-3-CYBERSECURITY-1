class Phone:
    def __init__(self, value):
        if not self.validate_phone(value):
            raise ValueError('Invalid phone number.')
        self.value = value

    def __str__(self):
        return str(self.value)

    @staticmethod
    def validate_phone(phone):
        if not phone:
            return False
        if phone[0] == '+':
            return phone[1:].isdigit() and len(phone) == 13
        else:
            return phone.isdigit() and len(phone) == 10
