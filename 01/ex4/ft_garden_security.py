#!/usr/bin/python3.10

class SecurePlant:
    def __init__(self, name):
        self.name = name
        self._height = 0
        self._age = 0
        print(f"Plant created: {self.name}")

    def set_height(self, height):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self._height = height
        print(f"Height updated: {self._height}cm [OK]")

    def set_age(self, age):
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
            return
        self._age = age
        print(f"Age updated: {self._age} days [OK]")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

# -------------------- MAIN --------------------

print("=== Garden Security System ===")

plant = SecurePlant("Rose")
plant.set_height(25)
plant.set_age(25)
print()
plant.set_height(-4)
print()
print(f"Current plant: {plant.name} ({plant.get_height()}cm, {plant.get_age()} days)")
