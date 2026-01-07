#!/usr/bin/python3.10

def check_plant_health(plant_name, water_level, sunlight_hours):
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")
    
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")

    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too high (max 12)")    
    print(f"Plant {plant_name} is healthy!\n")

def test_plant_checks():
    print("=== Garden Plant Health Checker ===\n")
    try:
        print("Testing good values...")
        check_plant_health("tomato", 5, 5)
    except ValueError as e:
        print(f"Error: {e}\n")

    try:
        print("Testing empty plant name...")
        check_plant_health("", 5, 5)
    except ValueError as e:
        print(f"Error: {e}\n")

    try:
        print("Testing bad water level...")
        check_plant_health("black tulip", 15, 5)
    except ValueError as e:
        print(f"Error: {e}\n")
        
    try:
        print("Testing bad sunlight hours...")
        check_plant_health("tulip", 5, 0)
    except ValueError as e:
        print(f"Error: {e}\n")

    print("All error raising tests completed!")

test_plant_checks()    
