# search.py
"""
Class to hold search results and provide flags for if all results are in the same book and chapter
"""
class BibleSearchResults:
    def __init__(self):
        # Initialize attributes to track if all results are from the same book and chapter
        self.sameBookNumber = True
        self.sameChapter = True
        # Store search results
        self.results = []

    def __add__(self, other):
        # Add results from another BibleSearchResults object
        for result in other.results:
            self.add(result)
        return self

    def add(self, result):
        # Add a result and update sameBookNumber and sameChapter flags
        self.results.append(result)
        if self.results:
            first_result = self.results[0]
            if result.bookNumber != first_result.bookNumber:
                self.sameBookNumber = False
            if result.chapter != first_result.chapter:
                self.sameChapter = False

