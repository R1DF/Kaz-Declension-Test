# Imports
import random
from .base import BaseTest

# Genitive case
class DativeTest(BaseTest):
    def __init__(self):
        BaseTest.__init__(self)
        self.description = "The dative case higlights the recipient/beneficiary of a specific action: \"Who is receiving what?\". In the sentence \"John gave Hannah flowers\", Hannah is the recipient."
        self.word = ""

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
        self.word = self.random_word()
        self.word_before = self.word
        self.sentence = [self.word]

        # Adding ending
        types_list = self.json_data["caseEndings"]["dative"]["lists"]
        endings = self.json_data["caseEndings"]["dative"]["word"]
        last_letter = self.word[-1].upper()
        if last_letter in types_list["G"]:
            self.word += endings[0][0 if self.word_type(0) == "hard" else 1]
        else:
            self.word += endings[1][0 if self.word_type(0) == "hard" else 1]

        # Updating
        self.sentence = [self.word]

