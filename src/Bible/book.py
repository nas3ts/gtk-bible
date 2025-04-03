# book.py
from chapter import Chapter

class Book:
    def __init__(self, name, number=-1, shortName=""):
        self.bookName = name
        self.number = number
        self.shortName = shortName
        self.chapters = []

    def addChapter(self, chapter):
        self.chapters.append(chapter)

    def __str__(self):
        return self.bookName

    def addVerse(self, verse):
        found = False
        for chapter in self.chapters:
            if chapter.number == verse.chapter:
                chapter.addVerse(verse)
                found = True
                break
        if not found:
            c = Chapter(verse.chapter)
            c.addVerse(verse)
            self.chapters.append(c)

    def search(self, string):
        results = []
        string = string.lower()
        for chapter in self.chapters:
            results.extend(chapter.search(string))
        return results

    def sort(self):
        self.chapters.sort(key=lambda x: x.number)
        for chapter in self.chapters:
            chapter.sort()

