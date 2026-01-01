#!/usr/bin/python3.10

class Plant:
    def __init__(self, name: str, height: int, days: int):
        self.name = name
        self.height = height
        self.days = days


Flower_list = [("Rose", 25, 30), ("Oak", 200, 365), ("Cactus", 5, 90), ("Sunflower", 80, 45), ("Fern", 15, 120)]


for i in Flower_list: #i is the value itself in the iterable list!
    print(i)

Plants = []

for a, b, c in Flower_list:  #unpacking
    plant = Plant(a, b, c)
    Plants.append(plant)


for p in Plants:
    print(f"Created: {p.name} ({p.height}cm, {p.days} days old)")

print("\nTotal plants created:", len(Plants))
