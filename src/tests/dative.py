# Imports
import random
from .base import BaseTest

# Dative case
class DativeTest(BaseTest):
    def __init__(self):
        BaseTest.__init__(self)
        self.description = "The dative case higlights the recipient/beneficiary of a specific action: \"Who is receiving what?\". In the sentence \"John gave Hannah flowers\", Hannah is the recipient."
        self.word = ""
        self.types_lists = {}
        self.endings = []

        # Types lists and endings
        self.get_types_lists("dative")
        self.get_endings("dative")

    def make_special(self):
        # Getting word
        self.word = self.json_data["pronounsAndEndings"][random.choice(list(self.json_data["pronounsAndEndings"].keys()))][2]

        # Getting original is a bit more complicated due to special grammar rules for pronouns
        if self.word in ["маған", "саған", "оған"]: # Special cases
            match self.word:
                case "маған":
                    self.word_before = "мен"
                case "саған":
                    self.word_before = "сен"
                case "оған":
                    self.word_before = "оған"
        else:
            self.word_before = self.word[:-2]

        # Updating
        self.sentence = [self.word]

    def make_normal(self):
        # Initialization
        self.make_word_normal()

        # Adding ending
        last_letter = self.word[-1].upper()
        if last_letter in self.types_lists["G"]:
            self.word += self.endings[0][0 if self.word_type(0) == "hard" else 1]
        else:
            self.word += self.endings[1][0 if self.word_type(0) == "hard" else 1]

        # Updating
        self.sentence = [self.word]

