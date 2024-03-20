from collections import UserDict
from Record import Record
from Email import Email
from Phone import Phone
from datetime import datetime, timedelta
from Error import input_error
import re

class AddressBook(UserDict):
    def __init__(self):
        self.data = []
    

    def add(self):
        name = input('Enter name: ')
        while True:
            phone = input('Enter phone. It should be in "+380991234567" or "0991234567" format: ')
            if Phone.validate_phone(phone):
                break
            else:
                print("Invalid phone number. Please try again.")
        
        email = input('Enter email: ')
        if email:
            while True:
                try:
                    Email(email)
                    break
                except ValueError as e:
                    print(f"{e}. Please try again.")
                    email = input('Enter email: ') 

        address = input('Enter address: ')
        birthday = input('Enter birthday date. It should be in format DD.MM.YYYY: ')
        if birthday:
            while True:
                if re.fullmatch(r"\d{2}\.\d{2}\.\d{4}", birthday):
                    break
                else:
                    print("Invalid birthday format. Please try again.")
                    birthday = input('Enter birthday date. It should be in format DD.MM.YYYY: ')

        user = Record(name, phone, email, address, birthday)
        self.data.append(user)
        return f"User {name} added successfully!"
    
    @input_error
    def change(self):
        name_to_change = input("Enter the name of the user you want to change: ")

        user_to_change = next((user for user in self.data if user.name.__str__() == name_to_change), None)
        if user_to_change is None:
            return f"User {name_to_change} not found!"

        field_to_change = input("Enter the field you want to change (name, phone, email, address, birthday): ")
        if field_to_change not in ['name', 'phone', 'email', 'address', 'birthday']:
            return f"Invalid field: {field_to_change}!"

        new_value = input(f"Enter the new value for {field_to_change}: ")

        if field_to_change == 'name':
            user_to_change.update_name(new_value)
        elif field_to_change == 'phone':
            user_to_change.update_phone(new_value)
        elif field_to_change == 'email':
            user_to_change.update_email(new_value)
        elif field_to_change == 'address':
            user_to_change.update_address(new_value)
        elif field_to_change == 'birthday':
            user_to_change.update_birthday(new_value)

        return f"{field_to_change.capitalize()} for user {name_to_change} changed successfully!"
    
    def delete(self):
        name_to_delete = input("Enter the name of the user you want to delete: ")

        user_to_delete = next((user for user in self.data if user.name.value == name_to_delete), None)

        if user_to_delete is None:
            return f"User {name_to_delete} not found!"

        self.data.remove(user_to_delete)
        return f"User {name_to_delete} deleted successfully!"
    
    def find(self):
        search_field = input("Enter the field to search (name, phone, email, address, birthday): ")
        if search_field not in ['name', 'phone', 'email', 'address', 'birthday']:
            return f"Invalid field: {search_field}!"
        search_value = input("Enter the value to search: ").lower()


        found_users = [user for user in self.data if getattr(user, search_field, '').__str__().lower().find(search_value) != -1]

        if not found_users:
            return f"No users found with {search_field} like {search_value}."

        return "\n".join([str(user) for user in found_users])
    
    def get_all(self):
        if not self.data:
            return "No contacts found."

        return "\n".join([str(user) for user in self.data])
        
    def get_birthday(self):
        try:
            days = int(input("Enter the number of days to search for upcoming birthdays: "))
        except ValueError:
            return "Invalid input. Please enter a valid number of days."

        if days < 0:
            return "Number of days cannot be negative."

        today = datetime.today().date()
        end_date = today + timedelta(days=days)

        found_users = []

        for user in self.data:
            if user.birthday:
                b_day, b_month = map(int, user.birthday.value.split('.')[:2])

                # Handle leap year case
                if b_month == 2 and b_day == 29 and not today.year % 4 == 0:
                    b_day = 28

                birthday_this_year = datetime(today.year, b_month, b_day).date()

                if today <= birthday_this_year <= end_date:
                    found_users.append(user)

        if not found_users:
            return f"No users found with birthdays within the next {days} days."

        return "\n".join([f"{user.name.value} - {user.birthday.value}" for user in found_users])
    
    def help_contact(self):
        help_text = """
        Available contact commands:
        - add-contact: Add a new contact.
        - change-contact: Change a field for an existing contact.
        - delete-contact: Delete a contact by name.
        - find-contact: Find and display a contact by any field.
        - all-contact: Display all contacts.
        - birthdays: Display contacts who have birthdays within a specified number of days.
        - help: Display this help message.
        """
        return help_text