#!/usr/bin/python3.10

"""
this program is about knowing how the module
is being executed by relying on __name__ variable

a python module can either be run directly or imported!

when run directly:
the module behaves like a script and displays basic info about the plane

when its imported:
the .py file functions as a helper file for the main one that was run directly!

==> we can use dunder variable __name__
to see if the file is run direcly or impoted!
"""

if __name__ == "__main__":
    print("=== Welcome to My Garden ===")
    print("Plant: Rose")
    print("Height: 25cm")
    print("Age: 30 days\n")
    print("=== End of Program ===")
