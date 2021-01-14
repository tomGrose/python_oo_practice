"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    """Class to pull random words from a dictionary"""
    def __init__(self, path):
        self.file = open(path, "r")
        self.file_list = self.word_list()
        self.print_words_read()

    def word_list(self):
        """ Populate the list from the words in the file. Exclude the /n"""
        return [w.strip() for w in self.file]

    def print_words_read(self):
        """Print how many words were read in the file"""
        print(f"{len(self.file_list)} words read")

    def random(self):
        """Pull a random word from the list to return"""
        return random.choice(self.file_list)


class SpecialWordFinder(WordFinder):
    """WordFinder that will exclude blank lines and comment lines from the file"""
    def __init__(self, path):
        super().__init__(path)

    def word_list(self):
        """Return a list without blank spaces or comment lines"""
        return [w.strip() for w in self.file if w.strip() and not w.startswith("#")]

