# Imports
import random
from .base import BaseTest

# Instruental case
class InstrumentalTest(BaseTest):
    def __init__(self):
        BaseTest.__init__(self)
        self.description = "The instrumental case indicates that a noun is used by the subject to achieve an action or exists with the subject."
        self.word = ""
        self.types_lists = {}
        self.endings = []

        # Types lists and endings
        self.get_types_lists("instrumental")
        self.get_endings("instrumental")

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
        self.make_word_normal()

        # Adding ending
        last_letter = self.word[-1].upper()
        if last_letter in self.types_lists["B"]:
            self.word += self.endings[0]
        elif last_letter in self.types_lists["P"]:
            self.word += self.endings[1]
        else:
            self.word += self.endings[2]

        # Updating
        self.sentence = [self.word]

