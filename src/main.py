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
def make_test(test_type):
    # Clearing the screen required
    clear()

    # Getting correct test
    match test_type:
        case "nominative":
            tester = NominativeTest()
        case "genitive":
            tester = GenitiveTest()
        case "dative":
            tester = DativeTest()
        case "accusative":
            tester = AccusativeTest()
        case "locative":
            tester = LocativeTest()
        case "ablative":
            tester = AblativeTest()
        case "instrumental":
            tester = InstrumentalTest()
        case _:
            return

    # Making sentence + Description
    if test_type == "nominative":
        tester.make()
    else:
        if random.randint(1, 3) == 3:
            tester.make_special()
        else:
            tester.make_normal()

    print(f"{test_type.upper()} CASE:\n{tester.description}\n\nSENTENCE:")
    tester.print_sentence()

    # Printing details
    if test_type == "genitive":  # Genitive case is special and I hate it
        input(f"\nDETAILS:\n\"Parent\" noun: {tester.parent_before}\n\"Child\" noun: {tester.child_before}\n\nPress Enter to return.\n\n")
    elif test_type == "nominative": # This one too
        input("\nPress Enter to return.\n\n")
    else:
        input(f"\nDETAILS:\nOriginal noun: {tester.word_before}\n\nPress Enter to return.\n\n")

# Main code
try:
    os.system("title Kazakh Declension Test")
    while True:
        clear()  # Must always clear first
        print("Kazakh Declension Test (by R1DF)\nSelect a case to generate a sentence from:")
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
                make_test("nominative")
            case 2:
                make_test("genitive")
            case 3:
                make_test("dative")
            case 4:
                make_test("accusative")
            case 5:
                make_test("locative")
            case 6:
                make_test("ablative")
            case 7:
                make_test("instrumental")
            case 8:
                break

    # Quit scenario
    clear()

except KeyboardInterrupt:
    clear()
    print("Terminated.")

