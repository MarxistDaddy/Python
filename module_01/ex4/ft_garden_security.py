#!/usr/bin/python3.10

class SecurePlant:
    '''
    represents a plant with protected attributes

    the secureplant class prevents invalud data assignements by
    validating height and age value before applying changes
    '''
    def __init__(self, name):
        """
        intialize new class instance!
        """
        self.name = name
        self._height = 0
        self._age = 0
        print(f"Plant created: {self.name}")

    def set_height(self, height):
        """
        set the plant height in cm: (setter method)

        negative values are rejected to protect data integrity

        args: height (int): the new height of plant to assign!
        """
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self._height = height
        print(f"Height updated: {self._height}cm [OK]")

    def set_age(self, age):
        """
        set the plant age in days:  (setter method)

        negative values are rejected to protect data integrity

        args: age (int): the age of plant when assign it
        """
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
            return
        self._age = age
        print(f"Age updated: {self._age} days [OK]")

    def get_height(self):
        """
        retrieve the plant current height: (getter method)
        to prevent modifying data

        return: (int) height in cm
        """
        return self._height

    def get_age(self):
        """
        retrieve the plant current age:
        (getter method) to prevent modifying data

        return: (int) age in days
        """
        return self._age


# -------------------- MAIN --------------------
print("=== Garden Security System ===")


plant = SecurePlant("Rose")
plant.set_height(25)
plant.set_age(25)
print()
plant.set_height(-5)
print()
print(f"Current plant: {plant.name}"
      f"({plant.get_height()}cm, {plant.get_age()} days)")
