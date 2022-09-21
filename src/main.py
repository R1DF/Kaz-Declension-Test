"""
Kazakh Declension test (Python)
Generates a random sentence containing a noun using a chosen case by the user.
"""

# Imports
import os
from data_getter import json_data

# Clear function
def clear():
    os.system("clear" if os.name != "nt" else "cls")

# Main code
os.system("title Kazakh Declension Test")
while True:
    clear()  # Must always clear first
    print("Kazakh Declension test\nSelect a case to generate:")
    for noun_case in range(len(json_data["cases"])):
        print(f"{noun_case + 1}. {json_data['cases'][noun_case]}")
    print("8. Quit")

    user_input = input("Select by number: ")

    # Validation
    if not user_input.isnumeric():
        print("Please enter a numeric value.")
        continue
    else:
        user_input = int(user_input)
        if user_input < 1 or user_input > 8:
            print("Please enter a value in the range.")
            continue

    # If the option is to quit
    if user_input == 8:
        break

# Quit scenario
clear()
