"""
Kazakh Declension Test (Python)
Generates a random sentence containing a noun using a chosen case by the user.
"""

# Imports
import os
import random
from data_getter import json_data
from tests.nominative import NominativeTest
from tests.genitive import GenitiveTest
from tests.dative import DativeTest
from tests.accusative import AccusativeTest
from tests.locative import LocativeTest
from tests.ablative import AblativeTest
from tests.instrumental import InstrumentalTest

# Clear function
def clear():
    os.system("clear" if os.name != "nt" else "cls")

# Test makers
def make_nominative():
    clear()
    tester = NominativeTest()
    print(f"NOMINATIVE CASE\n{tester.description}\n")
    tester.make()
    tester.print_sentence()
    input("\n\nPress Enter to return.")

def make_genitive():
    clear()
    tester = GenitiveTest()
    if random.randint(1, 2) == 1:
        tester.make_normal()
    else:
        tester.make_special()
    print(f"GENITIVE CASE\n{tester.description}\n")
    tester.print_sentence()
    input(f"\"Parent\" noun: {tester.parent_before}\n\"Child\" noun: {tester.child_before}\n\nPress Enter to return.\n\n")

def make_dative():
    clear()
    tester = DativeTest()
    if random.randint(1, 2) == 1:
        tester.make_normal()
    else:
        tester.make_special()
    print(f"DATIVE CASE\n{tester.description}\n")
    tester.print_sentence()
    input(f"Original noun: {tester.word_before}\n\nPress Enter to return.\n\n")

def make_accusative():
    clear()
    tester = AccusativeTest()
    if random.randint(1, 2) == 1:
        tester.make_normal()
    else:
        tester.make_special()
    print(f"ACCUSATIVE CASE\n{tester.description}\n")
    tester.print_sentence()
    input(f"Original noun: {tester.word_before}\n\nPress Enter to return.\n\n")

def make_locative():
    clear()
    tester = LocativeTest()
    if random.randint(1, 2) == 1:
        tester.make_normal()
    else:
        tester.make_special()
    print(f"LOCATIVE CASE\n{tester.description}\n")
    tester.print_sentence()
    input(f"Original noun: {tester.word_before}\n\nPress Enter to return.\n\n")

def make_ablative():
    clear()
    tester = AblativeTest()
    if random.randint(1, 2) == 1:
        tester.make_normal()
    else:
        tester.make_special()
    print(f"ABLATIVE CASE\n{tester.description}\n")
    tester.print_sentence()
    input(f"Original noun: {tester.word_before}\n\nPress Enter to return.\n\n")

def make_instrumental():
    clear()
    tester = InstrumentalTest()
    if random.randint(1, 2) == 1:
        tester.make_normal()
    else:
        tester.make_special()
    print(f"INSTRUMENTAL CASE\n{tester.description}\n")
    tester.print_sentence()
    input(f"Original noun: {tester.word_before}\n\nPress Enter to return.\n\n")


# Main code
try:
    os.system("title Kazakh Declension Test")
    while True:
        clear()  # Must always clear first
        print("Kazakh Declension Test\nSelect a case to generate a sentence from:")
        for noun_case in range(len(json_data["cases"])):
            print(f"{noun_case + 1}. {json_data['cases'][noun_case]}")
        print("8. Quit")

        user_input = input("Select by number: ")

        # Validation
        if not user_input.isnumeric():
            continue
        else:
            user_input = int(user_input)
            if user_input < 1 or user_input > 8:
                continue

        # Options
        match user_input:
            case 1:
                make_nominative()
            case 2:
                make_genitive()
            case 3:
                make_dative()
            case 4:
                make_accusative()
            case 5:
                make_locative()
            case 6:
                make_ablative()
            case 7:
                make_instrumental()
            case 8:
                break

    # Quit scenario
    clear()
except KeyboardInterrupt:
    clear()
    print("Terminated.")


