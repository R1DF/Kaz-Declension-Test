# Imports
import random
from .base import BaseTest

# Ablative case
class AblativeTest(BaseTest):
    def __init__(self):
        BaseTest.__init__(self)
        self.description = "The ablative case is often used to express motion away from something and other uses. In English, the preposition \"from\" is an equivalent."
        self.word = ""

    def make_special(self):
        # Getting word
        self.word = self.json_data["pronounsAndEndings"][random.choice(list(self.json_data["pronounsAndEndings"].keys()))][5]

        # Getting original pronoun
        match self.word:
            case "одан":
                self.word_before = "ол"
            case "менен" | "сенен":
                self.word_before = self.word[:-2]
            case _:
                self.word_before = self.word[:-3]

        # Updating
        self.sentence = [self.word]

    def make_normal(self):
        # Getting word
        self.word = self.random_word()  # Only one word needed
        self.word_before = self.word  # Saves original self
        self.sentence = [self.word]

        # Adding ending
        types_list = self.json_data["caseEndings"]["ablative"]["lists"]
        endings = self.json_data["caseEndings"]["ablative"]["word"]
        last_letter = self.word[-1].upper()
        if last_letter in types_list["D"]:
            self.word += endings[0][0 if self.word_type(0) == "hard" else 1]
        elif last_letter in types_list["T"]:
            self.word += endings[1][0 if self.word_type(0) == "hard" else 1]
        else:
            self.word += endings[2][0 if self.word_type(0) == "hard" else 1]

        # Updating sentence
        self.sentence = [self.word]

