# chapter.py
from verse import Verse

class Chapter:
    """Represents a chapter in the Bible.

    Attributes:
        number (int): The chapter number.
        verses (list of Verse): A list of Verse objects in the chapter.
    """

    # Constructor
    def __init__(self, number=-1):
        """Initialize a Chapter object.

        Args:
            number (int): The chapter number. Defaults to -1.
        """
        # Chapter number
        self.number = number
        # List of verses
        self.verses = []

    # Return a string representation of the chapter
    def __str__(self):
        """Return a string representation of the chapter."""
        return str(self.number)

    # Add a verse to the chapter
    def addVerse(self, verse):
        """Add a verse to the chapter.

        Args:
            verse (Verse): The Verse object to add.
        """
        self.verses.append(verse)

    # Search for a string in the verses of the chapter
    def search(self, string):
        """Search for a string in the verses of the chapter.

        Args:
            string (str): The string to search for.

        Returns:
            list of Verse: A list of Verse objects that match the search string.
        """
        results = []
        # Convert the string to lowercase
        string = string.lower()
        # Iterate over the verses
        for verse in self.verses:
            # Check if the string is in the verse text
            if string in verse.text.lower():
                # Add the verse to the results list
                results.append(verse)
        # Return the results list
        return results

    # Sort the verses in the chapter
    def sort(self):
        """Sort the verses in the chapter by their order."""
        # Sort the verses by their order
        self.verses.sort(key=lambda x: x.order)

