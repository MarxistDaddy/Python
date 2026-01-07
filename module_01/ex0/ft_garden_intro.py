#!/usr/bin/python3.10

"""
this program is about knowing how the module is being executed by relying on __name__ variable

a python module can either be run directly or imported!
__name__ in python, the special module variable, is a special bulit-in variable that exists in every Python module. its automatically set by Python and its value depends on how the module is being executed.







"""

if __name__ == "__main__":
    print("=== Welcome to My Garden ===")
    print("Plant: Rose")
    print("Height: 25cm")
    print("Age: 30 days\n")
    print("=== End of Program ===\n\n")
