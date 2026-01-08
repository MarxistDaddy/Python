#!/usr/bin/python3.10

class Plant:
    """
    plant class with name, height and age info
    """
    def __init__(self, name: str, height: int, days: int):
        self.name = name
        self.height = height
        self.days = days


"""
list of tuples that contain values of our plant objects that we want to create!
"""
Flower_list = [("Rose", 25, 30),
               ("Oak", 200, 365), ("Cactus", 5, 90),
               ("Sunflower", 80, 45), ("Fern", 15, 120)]


Plants = []
total = 0

for a, b, c in Flower_list:
    Plants += [Plant(a, b, c)]
    total += 1


print("=== Plant Factory Output ===")
for p in Plants:
    print(f"Created: {p.name} ({p.height}cm, {p.days} days)")

print("\nTotal plants created:", total)
