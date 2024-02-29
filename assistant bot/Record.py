from Name import Name
from Phone import Phone
from Birthday import Birthday
import datetime

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self,phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                break

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                break

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None
    
    def add_birthday(self, birthday):
        try:
            self.birthday = datetime.datetime.strptime(birthday, '%d.%m.%Y').date()
        except ValueError:
            raise ValueError('Birthday must be in the format DD.MM.YYYY')
        
    def select_phone(self):
        if len(self.phones) == 1:
            return self.phones[0].value
        else:
            print('Which number you want to change?')
            count = 1
            for idx, p in enumerate(self.phones):
                print(f'{count}. {p.value}')
                count += 1
            selection = int(input('Enter the number of the phone you want to change: '))
            return self.phones[selection - 1].value

        
    def __str__(self):
        return f'Contact name: {self.name.value}, phones: {"; ".join(p.value for p in self.phones)}'