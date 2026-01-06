#!/usr/bin/python3.10

def garden_operations():
    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: invalid literal for int()\n")

    try:
        print("Testing ZeroDivisionError...")
        10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")


    try:
        print("Testing FileNotFoundError...")
        open("missing.txt")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: No such file '{e.filename}'\n")


    try:
        print("Testing KeyError...")
        plants = {"rose": 10, "tulips": 11}
        print(plants["missing_plant"])
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")


    try:
        print("Testing multiple errors together...")
        int("abc") / 0
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")

def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")

test_error_types()
