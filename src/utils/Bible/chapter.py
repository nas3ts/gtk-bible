# chapter.py
from verse import Verse

class Chapter:
    def __init__(self, number=-1):
        self.number = number
        self.verses = []

    def __str__(self):
        return str(self.number)

    def addVerse(self, verse):
        self.verses.append(verse)

    def search(self, string):
        results = []
        string = string.lower()
        for verse in self.verses:
            if string in verse.text.lower():
                results.append(verse)
        return results

    def sort(self):
        self.verses.sort(key=lambda x: x.order)

