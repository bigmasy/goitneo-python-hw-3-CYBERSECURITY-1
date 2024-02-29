import datetime
from Record import Record
import pickle
from AddressBook import AddressBook

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            if str(e) == 'Phone number must be 10 digits':
                return str(e)
            elif str(e) == 'Give me name and date in format DD.MM.YYY':
                return str(e)
            elif str(e) == 'Birthday must be in the format DD.MM.YYYY':
                return str(e)
            else:
                return 'Give me name and phone please.' 
        except KeyError:
            return 'Enter correct name please.'
        except IndexError:
            return 'Enter user name please.'
        
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, book):
    name, phone = args
    if book.find(name):
        book.find(name).add_phone(phone)
        return f'To contact {name} added new number'
    else:
        rec = Record(name)
        rec.add_phone(phone)
        book.add_record(rec)
        return 'Contact added'

@input_error
def change_contact(args, book):
    name, new_phone = args
    rec = book.find(name)
    if not len(new_phone) == 10 or not new_phone.isdigit():
            raise ValueError('Phone number must be 10 digits')
    if rec is not None:
        old_phone = rec.select_phone()
        rec.edit_phone(old_phone, new_phone)
        return 'Contact changed'
    else:
        return 'Contact not found'



    
@input_error
def show_phone(args, book):
    name = args[0]
    record = book.find(name)
    if record:
        return record
    else:
        return f"Contact '{name}' not found."


def show_all_contacts(book):
    contacts_list = []
    max_name_length = max(len(name) for name in book.keys())
    
    for name, record in book.items():
        phones = ", ".join(str(phone) for phone in record.phones)
        if record.birthday is not None:
            birthday = record.birthday.strftime('%d.%m.%Y')
        else:
            birthday = "N/A"
        contact_info = f"Contact name: {name.ljust(max_name_length)}, phones: {phones}, birthday: {birthday}"
        contacts_list.append(contact_info)
    
    return '\n'.join(contacts_list)


def get_birthdays_per_week(book):
    list_name = {}
    today = datetime.datetime.today().date()

    for name, record in book.items():
        if record.birthday is None:
            continue
        birthday = record.birthday.strftime('%d.%m.%Y')
        birthday_date = datetime.datetime.strptime(birthday, '%d.%m.%Y').date()
        birthday_this_year = birthday_date.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            day_name = birthday_this_year.strftime("%A")
            if day_name in ['Saturday', 'Sunday']:
                day_name = 'Monday'
            if day_name in list_name:
                list_name[day_name].append(name)
            else:
                list_name[day_name] = [name]  
    if list_name:
        return '\n'.join([f"{day}: {', '.join(names)}" for day, names in list_name.items()])
    else:
        return 'No birthdays this week'

@input_error
def add_birthday(args, book):
    try:
        name, birthday = args
    except ValueError:
        raise ValueError('Give me name and date in format DD.MM.YYY') 
    contact = book.find(name)
    if contact:
        contact.add_birthday(birthday)
        return f'Birthday added for {name}'
    else:
        return f'Contact {name} not found'
    
@input_error
def name_birthday(args, book):
    name = args[0]
    contact = book.find(name)
    if contact:
        return contact.birthday.strftime('%d.%m.%Y') if hasattr(contact, 'birthday') else "N/A"
    else:
        return f"Contact '{name}' not found."
    
def load_address_book(filename):
    try:
        with open(filename, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("File not found. Creating a new address book.")
        return AddressBook()
    except Exception as e:
        print(f"An error occurred while loading the address book: {e}")
        return AddressBook()
    
def save_address_book(book, filename):
    with open(filename, 'wb') as f:
        pickle.dump(book, f)
