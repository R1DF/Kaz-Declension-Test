# Imports
import random
from .base import BaseTest

# Genitive case
class GenitiveTest(BaseTest):
    def __init__(self):
        BaseTest.__init__(self)
        self.description = "The genitive case represents possession, such as an item belonging to someone."
        self.child = ""

    def verify_child(self):
        # First step: Checking for exceptional letters at the ends.
        match self.child[-1]:
            case "к":
                self.child = self.child[:-1] + "г"
            case "қ":
                self.child = self.child[:-1] + "ғ"
            case "п":
                self.child = self.child[:-1] + "б"

    def add_child_ending(self, ending):
        child_endings = self.json_data["caseEndings"]["genitive"]["child"][ending]
        if self.is_consonant(1, len(self.child) - 1):
            self.child += child_endings[0][0 if self.word_type(1) == "hard" else 1]
        else:
            self.child += child_endings[1][0 if self.word_type(1) == "hard" else 1]

    def make_special(self):
        # Getting words
        self.pronoun = self.json_data["pronounsAndEndings"][random.choice(list(self.json_data["pronounsAndEndings"].keys()))][1]
        self.child = random.choice(self.json_data["words"])
        self.parent_before = self.pronoun  # Immune to modification
        self.child_before = self.child  # Immune to modification
        self.sentence = [self.pronoun, self.child]

        # First step: Checking for exceptional letters at the ends.
        self.verify_child()

        # Second step: Getting child ending.
        match self.pronoun:
            case "менің":
                ending = "firstSing"
            case "сенің":
                ending = "secondInfSing"
            case "сіздің":
                ending = "secondFormSing"
            case "біздің":
                ending = "firstPlu"
            case "сендердің":
                ending = "secondInfPlu"
            case "сіздердің":
                ending = "secondFormPlu"
            case _:
                ending = "third"

        self.add_child_ending(ending)

        # Third step: Making sentence.
        self.sentence = [self.pronoun, self.child]

    def make_normal(self):
        # Getting words is different since this test uses 2
        self.parent = random.choice(self.json_data["words"])
        self.child = random.choice(self.json_data["words"])
        self.parent_before = self.parent  # Immune to modification
        self.child_before = self.child  # Immune to modification
        self.sentence = [self.parent, self.child]

        # First step: Checking for exceptional letters at the ends.
        self.verify_child()

        # Second step: Adding ending to parent word.
        parent_endings = self.json_data["caseEndings"]["genitive"]["parent"]
        match self.get_correct_ending(self.parent):
            case "D":
                self.parent += parent_endings[0][0 if self.word_type(0) == "hard" else 1]
            case "T":
                self.parent += parent_endings[1][0 if self.word_type(0) == "hard" else 1]
            case "N":
                self.parent += parent_endings[2][0 if self.word_type(0) == "hard" else 1]

        # Second step: Adding ending to child word.
        self.add_child_ending("third")

        # Third step: Updating the sentence.
        self.sentence = [self.parent, self.child]

    def get_correct_ending(self, word):
        word = word.upper()
        if word[-1] in self.json_data["caseEndings"]["genitive"]["lists"]["D"]:
            return "D"
        elif word[-1] in self.json_data["caseEndings"]["genitive"]["lists"]["T"]:
            return "T"
        else:  # N
            return "N"

