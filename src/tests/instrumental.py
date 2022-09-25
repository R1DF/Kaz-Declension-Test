# Imports
import random
from .base import BaseTest

# Instruental case
class InstrumentalTest(BaseTest):
    def __init__(self):
        BaseTest.__init__(self)
        self.description = "The instrumental case indicates that a noun is used by the subject to achieve an action or exists with the subject."
        self.word = ""

    def make_special(self):
        # Getting word
        self.word = self.json_data["pronounsAndEndings"][random.choice(list(self.json_data["pronounsAndEndings"].keys()))][6]

        # Getting original pronoun
        match self.word:
            case "онымен":
                self.word_before = "ол"
            case "менімен" | "сенімен":
                self.word_before = self.word[:-4]
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
        types_list = self.json_data["caseEndings"]["instrumental"]["lists"]
        endings = self.json_data["caseEndings"]["instrumental"]["word"]
        last_letter = self.word[-1].upper()
        if last_letter in types_list["B"]:
            self.word += endings[0]
        elif last_letter in types_list["P"]:
            self.word += endings[1]
        else:
            self.word += endings[2]

        # Updating
        self.sentence = [self.word]

