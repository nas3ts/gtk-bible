# bible.py
from book import Book
from search import BibleSearchResults

class Bible:
    def __init__(self):
        # Initialize the Bible class with translation details and an empty list of books
        self.translation_name = ""           # Full name of the translation
        self.translation_abbreviation = ""   # Abbreviation of the translation
        self.translation_information = ""    # Additional information about the translation
        self.books = []                     # List to store Book objects
        self.language = ""                  # Language of the translation
        self.right_to_left = False          # Boolean for text direction

    def __str__(self):
        # Return a string representation of the Bible object
        lines = [
            f"translation name: {self.translation_name}",
            f"translation abbreviation: {self.translation_abbreviation}",
            f"translation information: {self.translation_information}",
        ]
        lines.extend(str(book) for book in self.books)
        return "\n".join(lines)

    def append(self, book):
        # Add a Book object to the list of books
        self.books.append(book)

    def add_verse(self, verse):
        # Add a Verse to the correct Book based on book number
        for book in self.books:
            if book.number == verse.book_number:
                book.add_verse(verse)
                break

    def get_book_names(self):
        # Return a list of book names in the Bible
        return [book.book_name for book in self.books]

    def get_book_by_num(self, num):
        # Return a Book object that matches the given book number
        for book in self.books:
            if book.number == num:
                return book
        return None

    def search(self, string):
        # Search for a string in all books and return the results
        results = BibleSearchResults()
        string = string.lower()
        for book in self.books:
            results += book.search(string)
        return results

    def sort(self):
        # Sort the books by their number and sort chapters and verses within each book
        self.books.sort(key=lambda x: x.number)
        for book in self.books:
            book.sort()



