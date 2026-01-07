#!/usr/bin/python3.10

class Plant:
    def __init__(self, name, water, sun):
        self.name = name
        self.water = water
        self.sun = sun


class GardenError(Exception):
    pass

class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass

class SunError(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.plants = []

    def add_plants(self, p):
        try:
            if not p.name:
                raise PlantError("Plant name cannot be empty!")
            self.plants += [p]
            print(f"Added {p.name} successfully")
        except PlantError as e:
            print(f"Error add plant: {e}\n")


    def water_plants(self):
        print("Watering plants...")
        try:
            print("Opening watering system")
            for p in self.plants:
                p.water += 1
                print(f"Watering {p.name} - success")
        finally:
            print("Closing watering system (cleanup)\n")

            
    def check_plant(self):
        print("Checking plant health...")
        try:
            for p in self.plants:
                if p.water < 1:
                    raise WaterError(f"Water level {p.water} is too low (min 1)") 
                if p.water > 10:
                    raise WaterError(f"Water level {p.water} is too high (max 10)")
                if p.sun < 2:
                    raise SunError(f"Sunlight hours {p.sun} is too low (min 2)")
                if p.sun > 12:
                    raise SunError(f"Sunlight hours {p.sun} is too high (max 12)")
                print(f"{p.name}: healthy (water: {p.water}, sun: {p.sun})")
        except (WaterError, SunError) as e:
            print(f"Error checking {p.name}: {e}\n")


if __name__ == "__main__":
    print("=== Garden Management System ===\n")
    print("Adding plants to garden...")
    plants_list = [Plant("tomato", 5, 8), Plant("lettuce", 14, 8), Plant("", 0, 0)]
    garden = GardenManager()
    for i in plants_list:
        garden.add_plants(i)
    garden.water_plants()
    garden.check_plant()    
    print("Testing error recovery...")
    try:
        raise GardenError(" Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("System recovered and continuing...")
    print("Garden management system test complete!")
