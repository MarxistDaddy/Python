#!/usr/bin/python3.10

class Plant:
    def __init__(self, name: str, height: int, days: int):
        self.name = name
        self.height = height
        self.days = days

    def grow(self):
        self.height += 1

    def age(self):
        self.days += 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.days} days old")


if __name__ == "__main__":
    print("=== Day 1 ===")
    
    rose = Plant("Rose", 25, 30)
    rose.get_info()

    for i in range(1, 8):
        rose.grow()
        rose.age()

    print("=== Day 7 ===")
    rose.get_info()
