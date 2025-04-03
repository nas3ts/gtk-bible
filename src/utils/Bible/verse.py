# verse.py
class Verse:
    def __init__(self, bookNumber, chapter, verse, text):
        self.bookNumber = bookNumber
        self.chapter = chapter
        self.verse = verse
        self.text = text

    def __str__(self):
        return f"Verse({self.bookNumber}, {self.chapter}, {self.verse}, {self.text})"
