#!/usr/bin/python3.10

class Plant:
    def __init__(self, name: str, height: int, age: int):
      self.name = name
      self.height = height
      self.age = age

plant_1 = Plant("Rose", 25, 3)

if __name__ == "__main__":
    print(f"{plant_1.name}:", f"{plant_1.height}cm,", f"{plant_1.age} days old")
