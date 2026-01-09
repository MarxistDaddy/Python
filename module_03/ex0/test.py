#!/usr/bin/python3.10

import sys

print(dir(sys.version))
print("===\n", sys.version)
print("===\n", sys.path)


if len(sys.argv) >= 2:
   for av in sys.argv:
       print(av.capitalize())
