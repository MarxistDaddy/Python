# Memory Depths Test Data
initial_powers = [20, 47, 79]
power_additions = [16, 5, 12, 9, 7]
enchantment_types = ['Earthen', 'Flaming', 'Flowing']
items_to_enchant = ['Amulet', 'Sword', 'Wand', 'Staff']

def mage_counter() -> callable:
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count

    return counter

def spell_accumulator(initial_power: int) -> callable:
    power = initial_power
    def add_power(total):
        nonlocal power
        power += total
        return power
    return add_power


def enchantment_factory(enchantment_type: str) -> callable:
    def enchant(item):
        return f"{enchantment_type} {item}"
    return enchant


def memory_vault() -> dict[str, callable]:
    memory = {}

    def store(key, value):
        nonlocal memory
        memory[key] = value

    def recall(key):
        if key in memory:
            return memory[key]
        return "Memory not found"

    return {
        "store": store,
        "recall": recall
    }

def main():
    print("Testing mage counter...")
    c = mage_counter()
    for i in range(1, 3 + 1):
        print(f"Call {i}:", c())


    print("\nTesting spell accumulator...")
    p = spell_accumulator(initial_powers[0])
    print(f"Initial power {initial_powers[0]}: accumulated power {p(10)}")
    

    print("\nTesting enchantant factory...")
    e = enchantment_factory(enchantment_types[1])
    for i in items_to_enchant:
        print(e(i))

    print("\nTesting memory vault...")
    function_dict = memory_vault()
    function_dict["store"]("color", "blue")
    print(function_dict["recall"]("color"))

if __name__ == "__main__":
    main()
