#!/usr/bin/python3.10

def water_plants(plant_list):
    print("Opening watering system")
    
    try:
        for plant in plant_list:
            if not plant:
                print(f"Error: Cannot water {plant} - invalid plant!")
                return 
            print(f"Watering {plant}")
    finally:
        print("Closing watering system (cleanup)")

def test_watering_system():
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("\nWatering completed succesfully!")
    print("\n")
    water_plants(["tomato", None])
    print("\nWatering completed succesfully!")


test_watering_system()    
