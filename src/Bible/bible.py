# bible.py
from book import Book
from search import BibleSearchResults

class Bible:
    def __init__(self):
        self.translationName = ""
        self.translationAbbreviation = ""
        self.translationInformation = ""
        self.books = []
        self.language = ""
        self.right_to_left = False

    def __str__(self):
        ret = ""
        ret += "translation name: " + self.translationName + '\n'
        ret += "translation abbreviation: " + self.translationAbbreviation + '\n'
        ret += "translation information: " + self.translationInformation + '\n'
        for book in self.books:
            ret += str(book) + '\n'
        return ret

    def append(self, book):
        self.books.append(book)

    def addVerse(self, verse):
        for book in self.books:
            if book.number == verse.bookNumber:
                book.addVerse(verse)
                break

    def getBookNames(self):
        return [book.bookName for book in self.books]

    def getBookByNum(self, num):
        for book in self.books:
            if book.number == num:
                return book
        return None

    def search(self, string):
        results = BibleSearchResults()
        string = string.lower()
        for book in self.books:
            results += book.search(string)
        return results

    def sort(self):
        self.books.sort(key=lambda x: x.number)
        for book in self.books:
            book.sort()

