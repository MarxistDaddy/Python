#!/usr/bin/python3.10

#------------------------------Plant----------------------------------#
class Plant:
    def __init__(self, name, height):
        self.name = name
        if height < 0:
           print(f"Invalid height for {name}, setting height to 0")
           self.height = 0
        else:
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
        self.total_plants = 0
        self.total_height = 0

    def add_plant(self, plant):
        self.plants.append(plant)
        self.total_plants += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_grow(self):
        print(f"{self.owner} is helping all plants grow...")
        for p in self.plants:
            p.grow()
            self.total_height += 1
        print("")

    def report(self):
        print(f"\n=== {self.owner}'s Graden Report ===")
        print("Plants in garden:")
        for p in self.plants:
            print(p.describe())
        print("")
    
    def get_score(self):
        score_total = 0
        for p in self.plants:
            if isinstance(p, PrizeFlower):
               score_total += p.height
               score_total += p.prize
               score_total += 20
            elif isinstance(p, FloweringPlant):
               score_total += p.height
               score_total += 10
            else:
               score_total += p.height

        return score_total
 
    def plants_added(self):
        print(f"Plants added: {self.total_plants}, Total growth: {self.total_height}cm")
            

#--------------------------garden_manager-----------------------------#

class GardenManager:
    def __init__(self):
        self.gardens = []
        self.total_gardens = 0

    def add_garden(self, garden):
        self.gardens.append(garden)
        self.total_gardens += 1

    class GardenStats:
        def __init__(self, garden):
            self.garden = garden

        def total_PH(self):
            self.garden.plants_added()

        def plant_types(self):
            regular = flowering = prize = 0
            for p in self.garden.plants:
                if isinstance (p, PrizeFlower):
                   prize += 1
                elif isinstance(p, FloweringPlant):
                   flowering += 1
                else:
                   regular += 1 
            print(f"Plant types: {regular} regular, {flowering} flowering, {prize} prize flowers")

        def check_height(self):
            height = 1
            for p in self.garden.plants:
                if p.height < 0:
                     height = 0
            if height > 0:
                print("Height validation test: True")
            else:
                print("Height validation test: False")
                     
        def report_garden(self):
            self.garden.report()

        def print_score(self):
            score = self.garden.get_score()
            print(f"Garden scores - {self.garden.owner}: {score}")

    def get_total_gardens(self):
        print(f"Total gardens managed: {self.total_gardens}")

#------------------------------main--------------------------------#

if __name__ == "__main__":

    print("=== Garden Managment System ===\n")
    alice = Garden("Alice")
    bob = Garden("Bob")

    alice.add_plant(Plant("Oak Tree", 100))
    alice.add_plant(FloweringPlant("Rose", 25, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))
 
    print("") 
    alice.help_grow()

    manager = GardenManager()
    manager.add_garden(alice)
    manager.add_garden(bob)
    
    bob.add_plant(Plant("pine", 60)) 
    bob.add_plant(FloweringPlant("kika", 20, "pink"))
    bob.help_grow() 
    def print_stats(owner):
        stats = manager.GardenStats(owner)
        stats.report_garden() 
        stats.total_PH()
        stats.plant_types()
        print("")
        stats.check_height()
        stats.print_score()

    
    print_stats(alice)
    print_stats(bob)
    print("")
    manager.get_total_gardens()

