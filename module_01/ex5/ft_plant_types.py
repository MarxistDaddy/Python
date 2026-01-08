#!/usr/bin/python3.10

class Plant():
    """
    represents a generic plant

    this basic class stores common attributes shared by all plants
    such as name, height and age
    """
    def __init__(self, name, height, age):
        """
        initializer special method: name, height and age!
        """
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """
        Simulate the flower blooming
        """
        print(f"{self.name} is blooming beautifully!")

    def describe(self):
        """
        Display detailed info about the flower
        """
        print(
            f"{self.name} (Flower): {self.height}cm, "
            f"{self.age} days, {self.color} color"
        )


class Tree(Plant):
    """
    represents a tree instance

    a tree extends plant by ading trunk diamter and behaviors related to shade
    production
    """
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """
        calculate and display the approximate shade provided by the tree
        """
        shade = self.trunk_diameter * 1.56
        print(f"{self.name} provides {int(shade)} square meters of shade")

    def describe(self):
        """
        display detailed info about the tree
        """
        print(
            f"{self.name} (Tree): {self.height}cm, "
            f"{self.age} days, {self.trunk_diameter}cm diameter"
        )


class Vegetable(Plant):
    """
    represents a vegerable plant

    a vegetable extends plant by adding harvest season and nutritional info
    """
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def describe(self):
        """
        display detailed info about the plant
        """
        print(
            f"{self.name} (Vegetable): {self.height}cm, "
            f"{self.age} days, {self.harvest_season} harvest"
        )

    def nutrition_info(self):
        """
        display nutritional info about the vegetable
        """
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    rose = Flower("Rose", 25, 30, "color")
    rose.describe()
    rose.bloom()
    print()
    tree = Tree("Oak", 500, 1825, 50)
    tree.describe()
    tree.produce_shade()
    print()
    veggie = Vegetable("Tomato", 80, 90, "summer", "C")
    veggie.describe()
    veggie.nutrition_info()
