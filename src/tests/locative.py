# Imports
import random
from .base import BaseTest

# Genitive case
class LocativeTest(BaseTest):
    def __init__(self):
        BaseTest.__init__(self)
        self.description = "The locative case highlights a location. In English, prepositions such as \"in\" and \"at\" replace it instead of having a case."
        self.word = ""
        self.types_lists = {}
        self.endings = []

        # Types lists and endings
        self.get_types_lists("locative")
        self.get_endings("locative")

    def make_special(self):
        # Getting word
        self.word = self.json_data["pronounsAndEndings"][random.choice(list(self.json_data["pronounsAndEndings"].keys()))][4]
        self.word_before = self.word[:-2] # Getting original is VERY easy for the locative (just cut off the last 2)

        # Updating
        self.sentence = [self.word]

    def make_normal(self):
        # Getting word
        self.make_word_normal()

        # Adding ending
        last_letter = self.word[-1].upper()
        if last_letter in self.types_lists["D"]:
            self.word += self.endings[0][0 if self.word_type(0) == "hard" else 1]
        else:
            self.word += self.endings[1][0 if self.word_type(0) == "hard" else 1]

        # Updating sentence
        self.sentence = [self.word]

