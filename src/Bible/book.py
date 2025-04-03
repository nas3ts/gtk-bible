# book.py
from chapter import Chapter

class Book:
    """Represents a book in the Bible.

    Attributes:
        bookName (str): The name of the book.
        number (int): The number of the book in the Bible.
        shortName (str): The short name of the book.
        chapters (list of Chapter): A list of Chapter objects in the book.
    """

    # Constructor
    def __init__(self, name, number=-1, shortName=""):
        """Initialize a Book object.

        Args:
            name (str): The name of the book.
            number (int): The number of the book in the Bible.
            shortName (str): The short name of the book.
        """
        self.bookName = name
        self.number = number
        self.shortName = shortName
        self.chapters = []

    # Add a chapter to the book
    def addChapter(self, chapter):
        """Add a chapter to the book.

        Args:
            chapter (Chapter): The Chapter object to add.
        """
        self.chapters.append(chapter)

    # String representation of the book
    def __str__(self):
        """Return a string representation of the book."""
        return self.bookName

    # Add a verse to the book
    def addVerse(self, verse):
        """Add a verse to the book.

        Args:
            verse (Verse): The Verse object to add.
        """
        # Check if the chapter already exists
        found = False
        for chapter in self.chapters:
            if chapter.number == verse.chapter:
                # Add the verse to the chapter
                chapter.addVerse(verse)
                found = True
                break
        if not found:
            # Create a new chapter
            c = Chapter(verse.chapter)
            c.addVerse(verse)
            self.chapters.append(c)

    # Search the book for a string
    def search(self, string):
        """Search the book for a string.

        Args:
            string (str): The string to search for.

        Returns:
            list of Verse: A list of Verse objects that match the search string.
        """
        # Initialize the results list
        results = []
        # Convert the string to lowercase
        string = string.lower()
        # Iterate over the chapters
        for chapter in self.chapters:
            # Add the search results from the chapter
            results.extend(chapter.search(string))
        # Return the results
        return results

    # Sort the chapters and verses in the book
    def sort(self):
        """Sort the chapters and verses in the book."""
        # Sort the chapters
        self.chapters.sort(key=lambda x: x.number)
        # Iterate over the chapters
        for chapter in self.chapters:
            # Sort the verses in the chapter
            chapter.sort()

