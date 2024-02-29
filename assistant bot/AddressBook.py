from collections import UserDict
import datetime
class AddressBook(UserDict):
    def __init__(self):
        self.data = {}
    

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def add_birthday(self, name, birthday):
        if name in self.data:
            self.data[name].add_birthday(birthday)
            return f'Birthday added for {name}'
        else:
            return f'Contact {name} not found'