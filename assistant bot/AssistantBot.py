from AssistantFunctions import*
from NoteManager import*

def main():
    filename_book = "address_book.pkl"
    filename_note = "note_book.pkl"
    book = load_address_book(filename_book)
    note = load_note_book(filename_note)
    print('Welcome to the assistant bot!')
    while True:
        user_input = input('Enter a command: ')
        try:
            command, *args = parse_input(user_input)
        except ValueError:
            command = 'Invalid command'


        if command in ['close', 'exit']:
            print('Saving address book...')
            save_address_book(book, filename_book)
            print('Saving note book...')
            save_note_book(note, filename_note)
            print('Good bye!')
            break
        elif command == 'hello':
            print('How can I help you?')
        elif command == 'add-contact':
            print(add_contact(args, book))
        elif command == 'change-contact':
            print(change_contact(args, book))
        elif command == 'phone':
            print(show_phone(args, book))
        elif command == 'all-contact':
            print(show_all_contacts(book))
        elif command == 'add-birthday':
            print(add_birthday(args, book))
        elif command == 'show-birthday':
            print(name_birthday(args, book))
        elif command == 'birthday':
            print(get_birthdays_per_week(book))
        elif command == 'add-note':
            print(note.create_note())
        elif command == 'change-note':
            print(note.edit_note_by_title())
        elif command == 'delete-note':
            print(note.delete_note_by_title())
        elif command == 'add-tag':
            print(note.add_note_tag())
        elif command == 'delete-tag':
            print(note.remove_note_tag())
        elif command == 'find-note':
            print(note.find_notes())
        elif command == 'all-note':
            print(note.get_all_notes())
        elif command == 'help-note':
            print(note.help_note())
        else:
            print('Invalid command.')


if __name__ == '__main__':
    main()