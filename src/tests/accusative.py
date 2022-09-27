# Imports
import random
from .base import BaseTest

# Accusative case
class AccusativeTest(BaseTest):
    def __init__(self):
        BaseTest.__init__(self)
        self.description = "The accusative case higlights the direct object of a verb. In the sentence \"Dogs eat meat\", \"meat\" is the direct object."
        self.word = ""
        self.types_lists = {}
        self.endings = []

        # Types lists and endings
        self.get_types_lists("accusative")
        self.get_endings("accusative")

    def make_special(self):
        self.word = self.json_data["pronounsAndEndings"][random.choice(list(self.json_data["pronounsAndEndings"].keys()))][3]
        if self.word in ["мені", "сені", "оны"]:
            self.word_before = self.word[:-1]
        else:
            self.word_before = self.word[:-2]
        self.sentence = [self.word]

    def make_normal(self):
        # Getting word
        self.make_word_normal()

        # Adding the specific ending
        last_letter = self.word[-1].upper()
        if last_letter in self.types_lists["D"]:
            self.word += self.endings[0][0 if self.word_type(0) == "hard" else 1]
        elif last_letter in self.types_lists["T"]:
            self.word += self.endings[1][0 if self.word_type(0) == "hard" else 1]
        else:
            self.word += self.endings[2][0 if self.word_type(0) == "hard" else 1]

        # Updating the sentence.
        self.sentence = [self.word]
