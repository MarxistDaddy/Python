#!/usr/bin/python3.10

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
        self.total_height = 0

    def grow(self):
        self.height += 1
        self.total_height += 1

    def age(self):
        self.age += 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        return self.total_height


if __name__ == "__main__":
    print("=== Day 1 ===")
    p = Plant("Rose", 25, 30)
    p.get_info()

    print("=== Day 7 ===")
    for i in range(7):
        p.grow()

    info = p.get_info()
    print(f"Total growth this week: +{info}cm")
