# verse.py
class Verse:
    """Represents a verse in the Bible

    Attributes:
        bookNumber (int): The number of the book in the Bible
        chapter (int): The chapter number
        verse (int): The verse number
        text (str): The actual text of the verse
    """

    def __init__(self, bookNumber, chapter, verse, text):
        # Store the book number
        self.bookNumber = bookNumber
        # Store the chapter number
        self.chapter = chapter
        # Store the verse number
        self.verse = verse
        # Store the text of the verse
        self.text = text

    def __str__(self):
        # Return a string representation of the verse
        return (f"Verse({self.bookNumber}, {self.chapter}, "
                f"{self.verse}, {self.text!r})")

