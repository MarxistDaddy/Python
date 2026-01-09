#!/usr/bin/python3.10

class Plant:
    """
    Plant class: represents a plant that can grow and age over time.

    relying on grow in its methods, it can tracks Plant's info: name,
    current height in cm and age in days, and it can return
    the total height gainged through growth!
    """
    def __init__(self, name: str, height: int, Age: int):
        """
        init special method: (dunder methods)
        initilize the following args: name, height and Age
        """
        self.name = name
        self.height = height
        self.Age = Age
        self.total_height = 0

    def grow(self):
        """
        Plant class' method! increase height by 1cm
        this method updates both the current height and total accumlated growth
        """
        self.height += 1
        self.total_height += 1

    def age(self):
        """
        increase Plant age by 1 day
        """
        self.Age += 1

    def get_info(self):
        """
        display the plant's current info
        prints the plant's name, height and age
        and returns total height gained throught growth

        return:
           int: te total height gaint in cm
        """
        print(f"{self.name}: {self.height}cm, {self.Age} days old")
        return self.total_height


if __name__ == "__main__":
    print("=== Day 1 ===")
    p = Plant("Rose", 25, 30)
    p.get_info()

    print("=== Day 7 ===")
    for i in range(1, 7):
        p.grow()
        p.age()

    info = p.get_info()
    print(f"Total growth this week: +{info}cm")
