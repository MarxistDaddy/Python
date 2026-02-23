import alchemy.elements
from alchemy.elements import create_fire
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_fire, create_water, create_earth
from alchemy.potions import strength_potion



print("=== Import Transmutation Mastery ===\n")

print("Method 1 - Full module import:")
print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}\n")


print("Method 2 - Specific function import:")
print(f"create_water(): {create_water()}\n")


print("Method 3 - Aliased import:")
print(f"heal(): {heal()}\n")


print("Method 4 - Multiple imports:")
print(f"create_earth(): {create_earth()}")
print(f"create_fire(): {create_fire()}")
print(f"strength_potion(): {strength_potion()}")

print("\nAll import transmutation methods mastered!")
