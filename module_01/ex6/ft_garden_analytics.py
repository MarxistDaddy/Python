#!/usr/bin/python3.10

class Plant:
    """
    represents a basic plant

    stores a plant's name and height, and ensures height cannot be negative
    """
    def __init__(self, name, height):
        """
        initialize a plant instance
        """
        self.name = name
        if height < 0:
            print(f"Invalid height for {name}, setting height to 0")
            self.height = 0
        else:
            self.height = height

    def grow(self):
        """
        Increase the plants's height bu 1 centimeter
        """
        self.height += 1
        print(f"{self.name} grew 1cm")

    def describe(self):
        """
        return a string description of the plant

        returns: str: descirption containing name and height.
        """
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """
    represents a flowering plant

    extends Plant by adding a flower color and a more detailed description
    """
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color

    def describe(self):
        """
        return descriptive info about flower plant + color
        """
        return f"- {self.name}: {self.height}cm, {self.color} flower (booming)"


class PrizeFlower(FloweringPlant):
    """
    represents a prize-winning flowering plant

    extends flowering plant by adding prize points!
    """
    def __init__(self, name, height, color, prize):
        super().__init__(name, height, color)
        self.prize = prize

    def describe(self):
        """
        return a string description of the prize flower

        return: str: descriptopn including prize points
        """
        return f"- {self.name}: {self.height}cm, " \
               f"{self.color} flower (booming), Prize points: {self.prize}"


class Garden():
    """
    represnts a garden class owner by a specific person

    a garden manages collection of plants, tracks growth, and calculates a score
    based on plant types!
    """
    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.total_plants = 0
        self.total_height = 0

    def add_plant(self, plant):
        """
        add a plant to the garden

        args: the plant to add
        """
        self.plants.append(plant)
        self.total_plants += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_grow(self):
        """
        Make all plants in the garden grow by one unit
        """
        print(f"{self.owner} is helping all plants grow...")
        for p in self.plants:
            p.grow()
            self.total_height += 1
        print("")

    def report(self):
        """
        Print a detailed report of all plants in the garden
        """
        print(f"\n=== {self.owner}'s Graden Report ===")
        print("Plants in garden:")
        for p in self.plants:
            print(p.describe())
        print("")

    def get_score(self):
        """
        calculate the garden's score based on plant types

        return: (int) the total score for the garden
        """
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
        """
        Display statistics about plants added and tatal growth
        """
        print(f"Plants added: "
              f"{self.total_plants}, Total growth: {self.total_height}cm")


class GardenManager:
    """
    Manages multiple gardens and provides garden-level statics
    """
    def __init__(self):
        self.gardens = []
        self.total_gardens = 0

    def add_garden(self, garden):
        """
        add garden to the manager

        args: (object) garden to manage
        """
        self.gardens.append(garden)
        self.total_gardens += 1

    class GardenStats:
        """
        provides statistical reports for a spefic garden
        """
        def __init__(self, garden):
            """
            initialize a GardenStats instance
            """
            self.garden = garden

        def total_PH(self):
            """
            Display the number of plant types in the garden
            """
            self.garden.plants_added()

        def plant_types(self):
            """
            display the number of plants in the garden
            """
            regular = flowering = prize = 0
            for p in self.garden.plants:
                if isinstance(p, PrizeFlower):
                    prize += 1
                elif isinstance(p, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            print(f"Plant types: {regular} regular, "
                  f"{flowering} flowering, {prize} prize flowers")

        def check_height(self):
            """
            validate that all plant heights are non-negative
            """
            height = 1
            for p in self.garden.plants:
                if p.height < 0:
                    height = 0
            if height > 0:
                print("Height validation test: True")
            else:
                print("Height validation test: False")

        def report_garden(self):
            """
            print the garden's detailed report
            """
            self.garden.report()

        def print_score(self):
            """
            display the garden total score
            """
            score = self.garden.get_score()
            print(f"Garden scores - {self.garden.owner}: {score}")

    def get_total_gardens(self):
        """
        display the total number of gardens managed
        """
        print(f"Total gardens managed: {self.total_gardens}")


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
