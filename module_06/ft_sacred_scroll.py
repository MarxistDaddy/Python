import alchemy

if __name__ == "__main__":
    print("=== Sacred Scroll Mastery ===\n")
    
    print("Testing direct module access:")
    print("alchemy.elements.create_fire():", end=" ")
    print(f"{alchemy.elements.create_fire()}")
    
    print("alchemy.elements.create_water():", end=" ")
    print(f"{alchemy.elements.create_water()}")
    
    print("alchemy.elements.create_earth():", end=" ")
    print(f"{alchemy.elements.create_earth()}")
    
    print("alchemy.elements.create_air():", end=" ")
    print(f"{alchemy.elements.create_air()}")
    
    
    
    print("\nTesting package-level access (controlled by __init__.py):")
    
    print("alchemy.create_fire():", end=" ")
    print(f"{alchemy.create_fire()}")
    
    print("alchemy.create_water():", end=" ")
    print(f"{alchemy.create_water()}")
    
    try:
        print("alchemy.create_earth():", end=" ")
        print(f"{alchemy.create_earth()}")
    except Exception as e:
        print("AttributeError - not exposed")
    
    try:
        print("alchemy.create_air():", end=" ")
        print(f"{alchemy.create_air()}")
    except Exception as e:
        print("AttributeError - not exposed")
    
    print("\nPackage metadata")
    print("Version:", alchemy.__version__)
    print("Author:", alchemy.__author__)
