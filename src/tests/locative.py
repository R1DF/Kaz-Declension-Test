# Imports
import random
from .base import BaseTest

# Genitive case
class LocativeTest(BaseTest):
    def __init__(self):
        BaseTest.__init__(self)
        self.description = "The locative case highlights a location. In English, prepositions such as \"in\" and \"at\" replace it instead of having a case."
        self.word = ""

    def make_special(self):
        # Getting word
        self.word = self.json_data["pronounsAndEndings"][random.choice(list(self.json_data["pronounsAndEndings"].keys()))][4]
        self.word_before = self.word[:-2] # Getting original is VERY easy for the locative (just cut off the last 2)

        # Updating
        self.sentence = [self.word]

    def make_normal(self):
        # Getting word
        self.word = self.random_word()  # Only one word needed
        self.word_before = self.word  # Saves original self
        self.sentence = [self.word]

        # Adding ending
        types_list = self.json_data["caseEndings"]["locative"]["lists"]
        endings = self.json_data["caseEndings"]["locative"]["word"]
        last_letter = self.word[-1].upper()
        if last_letter in types_list["D"]:
            self.word += endings[0][0 if self.word_type(0) == "hard" else 1]
        else:
            self.word += endings[1][0 if self.word_type(0) == "hard" else 1]

        # Updating sentence
        self.sentence = [self.word]

