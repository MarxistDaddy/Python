#!/usr/bin/python3.10

class Plant:
    """
    this is Plant class. it represents a Plant in the garden

    this Plant class stores basic descriptive info like: name, height and age
    """
    def __init__(self, name: str, height: int, age: int):
        """
        under special methods. used to initliaze a new Plant instance

        args: descrptive info about the plant!
              name, height in cm, age days
        """
        self.name = name
        self.height = height
        self.age = age


plant_1 = Plant("Rose", 25, 30)
plant_2 = Plant("Sunflower", 80, 45)
plant_3 = Plant("Cactus", 15, 120)

if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    print(f"{plant_1.name}: {plant_1.height}cm, {plant_1.age} days old")
    print(f"{plant_2.name}: {plant_2.height}cm, {plant_2.age} days old")
    print(f"{plant_3.name}: {plant_3.height}cm, {plant_3.age} days old")
