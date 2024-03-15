from AssistantFunctions import parse_input, load_address_book, save_address_book, load_note_book, save_note_book

def main():
    filename_book = "address_book.pkl"
    filename_note = "note_book.pkl"
    book = load_address_book(filename_book)
    note = load_note_book(filename_note)
    print('Welcome to the assistant bot!')
    print('Available contact commands')
    print(note.help_note())
    print(book.help_contact())
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
            print(book.add())
        elif command == 'change-contact':
            print(book.change())
        elif command == 'all-contact':
            print(book.get_all())
        elif command == 'birthday':
            print(book.get_birthday())
        elif command == 'find-contact':
            print(book.find())
        elif command == 'delete-contact':
            print(book.delete())

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
        elif command == 'help':
            print(note.help_note())
            print(book.help_contact())
        else:
            print('Invalid command. Type "help" for a list of available commands.')


if __name__ == '__main__':
    main()