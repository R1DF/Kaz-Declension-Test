"""c
This is the base for a case test.
Functions:
is_soft()
"""
# Imports
import os
import json
import random

# Class
class BaseTest:
    def __init__(self):
        self.sentence = []
        self.types_lists = []
        self.endings = []

        # Has its own version of data_getter
        with open(os.getcwd() + "\\data.json", encoding="utf-8") as f:
            self.json_data = json.load(f)

    # Universal functions (appear in every Test)
    def get_types_lists(self, case_type):
        self.types_lists = self.json_data["caseEndings"][case_type]["lists"]

    def get_endings(self, case_type):
        self.endings = self.json_data["caseEndings"][case_type]["word"]


    def print_sentence(self):
        """
        Prints out the sentence to the screen.
        """
        print(" ".join(self.sentence).capitalize() + ".")

    def is_consonant(self, word_index, letter_index):
        """
        Returns true if the letter of a specific word in self.sentence is a consonant. Else, false.
        """
        letter = self.sentence[word_index][letter_index].upper()
        return not (letter in self.json_data["vowels"]["soft"] or letter in self.json_data["vowels"]["hard"])

    def is_consonant_ext(self, letter):
        """
        self.is_constant() but the word doesn't have to be in self.sentence()
        """
        return not letter.upper() in self.json_data["vowels"]["all"]

    def word_type(self, word_index):
        """
        Returns whether the word is soft or hard based on the last vowel.
        """
        for letter in self.sentence[word_index][::-1]:
            if not self.is_consonant_ext(letter):
                if letter.upper() in self.json_data["vowels"]["hard"]:
                    return "hard"
                else:
                    return "soft"

    def word_ending_type(self, word_index):
        """
        Returns self.consonant_type of the last letter (if it's a consonant). If the letter is a vowel, it returns "voiced".
        """
        word = self.sentence[word_index]
        letter = word[len(word)-1]

        if self.is_consonant(word_index, len(word)-1):
            return self.consonant_type(word_index, len(word)-1)
        else:
            return "voiced"

    def consonant_type(self, word_index, letter_index):
        """
        Returns the type of the consonant: Sonorant (sonornye), voiceless (gluhie), voiced (zvonkie).
        If the letter isn't a consonant, None is returned.
        """
        letter = self.sentence[word_index][letter_index].upper()
        if letter in self.json_data["consonants"]["sonorant"]:
            return "sonorant"
        elif letter in self.json_data["consonants"]["voiceless"]:
            return "voiceless"
        elif letter in self.json_data["consonants"]["voiced"]:
            return "voiced"

    def make_word_normal(self, not_genitive=True):
        self.word = self.word_before = random.choice(self.json_data["words"])
        if not_genitive:  # Useless feature but I'll keep it on just in case I ever revisit this again -25.9.22
            self.sentence = [self.word]

