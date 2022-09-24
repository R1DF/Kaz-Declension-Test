# Imports
import random
from .base import BaseTest

# Genitive case
class AccusativeTest(BaseTest):
    def __init__(self):
        BaseTest.__init__(self)
        self.description = "The accusative case higlights the direct object of a verb. In the sentence \"Dogs eat meat\", \"meat\" is the direct object."
        self.word = ""

    def make_special(self):
        self.word = self.json_data["pronounsAndEndings"][random.choice(list(self.json_data["pronounsAndEndings"].keys()))][3]
        if self.word in ["мені", "сені", "оны"]:
            self.word_before = self.word[:-1]
        else:
            self.word_before = self.word[:-2]
        self.sentence = [self.word]

    def make_normal(self):
        self.word = self.random_word()  # Only one word needed
        self.word_before = self.word  # Saves original self
        self.sentence = [self.word]

        # First step: Adding the specific ending
        types_list = self.json_data["caseEndings"]["accusative"]["lists"]
        endings = self.json_data["caseEndings"]["accusative"]["word"]
        last_letter = self.word[-1].upper()
        if last_letter in types_list["D"]:
            self.word += endings[0][0 if self.word_type(0) == "hard" else 1]
        elif last_letter in types_list["T"]:
            self.word += endings[1][0 if self.word_type(0) == "hard" else 1]
        else:
            self.word += endings[2][0 if self.word_type(0) == "hard" else 1]

        # Second step: Updating the sentence.
        self.sentence = [self.word]
