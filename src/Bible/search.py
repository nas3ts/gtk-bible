# search.py
class BibleSearchResults:
    def __init__(self):
        self.sameBookNumber = True
        self.sameChapter = True
        self.results = []

    def __add__(self, other):
        for result in other.results:
            self.add(result)

    def add(self, result):
        self.results.append(result)
        if not result.bookNumber == self.results[0].bookNumber:
            self.sameBookNumber = False
        if not result.chapter == self.results[0].chapter:
            self.sameChapter = False
