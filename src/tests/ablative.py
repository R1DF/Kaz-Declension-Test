# Imports
import random
from .base import BaseTest

# Ablative case
class AblativeTest(BaseTest):
    def __init__(self):
        BaseTest.__init__(self)
        self.description = "The ablative case is often used to express motion away from something and other uses. In English, the preposition \"from\" is an equivalent."
        self.word = ""
        self.types_lists = {}
        self.endings = []

        # Types lists and endings
        self.get_types_lists("ablative")
        self.get_endings("ablative")

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
        self.make_word_normal()

        # Adding ending
        last_letter = self.word[-1].upper()
        if last_letter in self.types_lists["D"]:
            self.word += self.endings[0][0 if self.word_type(0) == "hard" else 1]
        elif last_letter in self.types_lists["T"]:
            self.word += self.endings[1][0 if self.word_type(0) == "hard" else 1]
        else:
            self.word += self.endings[2][0 if self.word_type(0) == "hard" else 1]

        # Updating sentence
        self.sentence = [self.word]

