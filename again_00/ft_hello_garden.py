def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if(unit == "packets"):
        print(seed_type.capitalize(), quantity, "packets avaialble")
    elif(unit == "grams"):
        print(seed_type.capitalize(), quantity, "grams toatl")
    elif(unit == "meters"):
        print(seed_type.capitalize(), quantity, "square meters")
    else:
        print("unknown type!")
 
