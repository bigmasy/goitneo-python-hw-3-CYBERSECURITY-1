class Note:
    def __init__(self, title, text, tags=None):
        self.title = title
        self.text = text
        self.tags = [tags] if tags else []

    def change_text(self, new_text):
        self.text = new_text

    def add_tag(self, new_tag):
        self.tags.append(new_tag)

    def remove_tag(self, new_tag):
        if new_tag not in self.tags:
            raise KeyError("Tag not found.")
        self.tags.remove(new_tag)

    def has_tag(self, search_tag):
        return search_tag in self.tags

    def show(self):
        tags = 'No tags' if not self.tags else f"Tags: {', '.join(self.tags)}"
        text = 'No text' if not self.text else f"Text:\n{self.text}"
        return f"Title: {self.title}\n{tags}\n{text}"
