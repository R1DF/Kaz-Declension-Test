# Imports
import random
from .base import BaseTest

# Genitive case
class NominativeTest(BaseTest):
    def __init__(self):
        BaseTest.__init__(self)
        self.description = "The nominative case is the easiest and simplest case. It shows that the noun is the subject of the sentence and adds no endings."
        self.word = ""

    def make(self):
        self.sentence = [random.choice([
            random.choice(self.json_data["words"]), # normal
            self.json_data["pronounsAndEndings"][random.choice(list(self.json_data["pronounsAndEndings"].keys()))][0] # special
        ])]

