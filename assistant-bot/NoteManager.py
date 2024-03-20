from Note import Note


class NoteManager:
    def __init__(self):
        self.notes = []

    def create_note(self):
        title = input("Enter note title: ")
        note_text = input("Enter note text: ")
        tags = input("Enter note tag: ")
        self.notes.append(Note(title, note_text, tags))
        return f"Note '{title}' added successfully!"

    def edit_note_by_title(self):
        title = input("Enter note title to edit: ")
        for note in self.notes:
            if note.title == title:
                new_text = input("Enter new text: ")
                note.change_text(new_text)
                return f"Note '{title}' updated successfully!"
        return f"Note with title '{title}' not found."

    def delete_note_by_title(self):
        title = input("Enter note title to delete: ")
        deleted = False
        for i, note in enumerate(self.notes):
            if note.title == title:
                del self.notes[i]
                deleted = True
                break
        if deleted:
            return f"Note '{title}' deleted successfully!"
        else:
            return f"Note with title '{title}' not found."

    def add_note_tag(self):
        title = input("Enter note title to add a tag: ")
        for note in self.notes:
            if note.title == title:
                tag = input("Enter tag: ")
                note.add_tag(tag)
                return f"Tag '{tag}' added to note '{title}'."
        return f"Note with title '{title}' not found."
    
    def find_notes(self):
        query = input("Enter tag or title to search: ").lower()
        found_notes = [
            note for note in self.notes
            if any(query in tag.lower() for tag in note.tags) or query in note.title.lower()
        ]
        if not found_notes:
            return f"No notes found with tag or title containing '{query}'."
        return "\n".join([note.show() for note in found_notes])
    
    def get_all_notes(self):
        if len(self.notes) == 0:
            return "No notes available."
        return "\n".join([note.show() for note in self.notes])
    
    def remove_note_tag(self) -> str:
        title = input("Enter note title to remove a tag: ")
        for note in self.notes:
            if note.title == title:
                tag = input("Enter tag to remove: ")
                try:
                    note.remove_tag(tag)
                    return f"Tag '{tag}' removed from note '{title}'."
                except KeyError:
                    return f"Tag '{tag}' not found in note '{title}'."
        return f"Note with title '{title}' not found."
    
    def help_note(self):
        help_text = """
        Available note commands:
        - add-note: Add a new note (title and text).
        - change-note: Change the text of a note.
        - delete-note: Delete a note by title.
        - add-tag: Add a tag to a note.
        - delete-tag: Remove a tag from a note.
        - find-note: Search and display a note by tag or title.
        - all-note: Display all notes.
        - help-note: Display this help message.
        """
        return help_text
    
