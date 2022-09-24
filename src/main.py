"""
Kazakh Declension test (Python)
Generates a random sentence containing a noun using a chosen case by the user.
"""

# Imports
import os
import random
from data_getter import json_data
from tests.genitive import GenitiveTest

# Clear function
def clear():
    os.system("clear" if os.name != "nt" else "cls")

def make_genitive():
    clear()
    tester = GenitiveTest()
    if random.randint(1, 2) == 1:
        tester.make_normal()
    else:
        tester.make_special()
    print(F"GENITIVE CASE\n{tester.description}\n")
    tester.print_sentence()
    input(f"\"Parent\" noun: {tester.parent_before}\n\"Child\" noun: {tester.child_before}\n\nPress Enter to return.\n\n")

# Main code
os.system("title Kazakh Declension Test")
while True:
    clear()  # Must always clear first
    print("Kazakh Declension test\nSelect a case to generate a sentence from:")
    for noun_case in range(len(json_data["cases"])):
        print(f"{noun_case + 1}. {json_data['cases'][noun_case]}")
    print("8. Quit")

    user_input = input("Select by number: ")

    # Validation
    if not user_input.isnumeric():
        input("Please enter a numeric value.\n")
        continue
    else:
        user_input = int(user_input)
        if user_input < 1 or user_input > 8:
            input("Please enter a value in the range.\n")
            continue

    # Options
    match user_input:
        case 1:
            pass
        case 2:
            make_genitive()
        case 8:
            break

# Quit scenario
clear()
