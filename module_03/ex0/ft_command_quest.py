#!/usr/bin/python3.10

import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    length = len(sys.argv)
    if length < 2:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
    else:
        print(f"Program name: {sys.argv[0]}")
        print("Arguments received:", length - 1)
        i = 1
        while i < length:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {length}")
