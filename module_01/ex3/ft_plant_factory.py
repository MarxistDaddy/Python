#!/usr/bin/python3.10

class Plant:
    def __init__(self, name: str, height: int, days: int):
        self.name = name
        self.height = height
        self.days = days


Flower_list = [("Rose", 25, 30), ("Oak", 200, 365), ("Cactus", 5, 90), ("Sunflower", 80, 45), ("Fern", 15, 120)]


Plants = []
total = 0

for a, b, c in Flower_list:
    plant = Plant(a, b, c)
    Plants += [Plant(a, b, c)]
    total += 1


for p in Plants:
    print(f"Created: {p.name} ({p.height}cm, {p.days} days old)")

print("\nTotal plants created:", total)
