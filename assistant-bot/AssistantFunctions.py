import pickle
from AddressBook import AddressBook
from NoteManager import NoteManager

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

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

def load_note_book(filename):
    try:
       with open(filename, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("File not found. Creating a new note book.")
        return NoteManager()
    except Exception as e:
        print(f"An error occurred while loading the note book: {e}")
        return NoteManager()
    
def save_note_book(note, filename):
    with open(filename, 'wb') as f:
        pickle.dump(note, f)
