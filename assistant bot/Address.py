class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.addresses = []  
        self.birthday = None

    def add_address(self, address):
        self.addresses.append(Address(address))

    def remove_address(self, address):
        for a in self.addresses:
            if a.value == address:
                self.addresses.remove(a)
                break

    def edit_address(self, old_address, new_address):
        for a in self.addresses:
            if a.value == old_address:
                a.value = new_address
                break

    def find_address(self, address):
        for a in self.addresses:
            if a.value == address:
                return a
        return None

    def __str__(self):
        return f'Contact name: {self.name.value}, phones: {"; ".join(p.value for p in self.phones)}, addresses: {"; ".join(a.value for a in self.addresses)}'