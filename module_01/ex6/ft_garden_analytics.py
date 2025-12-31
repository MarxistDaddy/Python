#!/usr/bin/python3.10

#------------------------------Plant----------------------------------#
class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")

    def describe(self):
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color

    def describe(self):
        return f"- {self.name}: {self.height}cm, {self.color} flower (booming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize):
        super().__init__(name, height, color)
        self.prize = prize

    def describe(self):
        return f"- {self.name}: {self.height}cm, {self.color} flower (booming), Prize points: {self.prize}"

#------------------------------garden---------------------------------#

class Garden():
    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        total_plants = 0
        total_height = 0

    def add_plant(self, plant):
        self.plants.append(plant)
        self.total_plants += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_grow(self):
        print(f"{self.owner} is helping all plants grow...")
        for p in self.plants:
            p.grow()
            self.total_height += 1

    def report(self):
        print(f"=== {self.owner}'s Graden Report ===")
        print("Plants in garden:")
        for p in self.plants:
            print(p.describe())

        def plants_added(self):
            print(f"Plants added: {self.total_plants}, Total growth: {self.total_height}cm")
            

#--------------------------garden_manager-----------------------------#

class GardenManager:
    def __init__(self):
        self.gardens = []
        self.total_gardens = 0

    class GardenStats:
       def __init__(self, garden):
           self.garden = garden

       def total_plants(self):
           total_plants = 0
           for p in self.garden.plants:
               total_plants += 1
               return (total_plants)

       def plant_types(self):
            regular = flowering = prize = 0
            for p in self.garden.plants:
                if isinstance (p, PrizeFlower):
                   prize += 1
                elif isinstance(p, PrizeFlower):
                   flowering += 1
                else:
                   regular += 1
            
            return regular, flowering, prize

    def add_garden(self, garden):
        self.gardens.append(garden)
        self.total_gardens += 1
        print("garden been added!")

#------------------------------main--------------------------------#


if __name__ == "__main__":
    manager = GardenManager()

    alice = Garden("Alice")
    print("Garden:", alice.owner)

    #Oak_Tree = Plant("Oak Tree", 100)
    #Rose = FloweringPlant("Rose", 25, "red")
    #Sunflower = PrizeFlower("Sunflower", 50, "black", 10)

    alice.add_plant(Plant("Oak Tree", 100))
    alice.add_plant(FloweringPlant("Rose", 25, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, "black", 10))

    alice.help_grow()
    alice.report()

    manager.add_garden(alice)
    stats = manager.GardenStats(alice)
    
    print(stats.total_plants())
    print()
