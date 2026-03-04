from functools import reduce, partial, lru_cache, singledispatch
import operator

spell_powers = [48, 44, 45, 49, 45, 34]
operations = ['add', 'multiply', 'max', 'min']
fibonacci_tests = [16, 15, 10]


def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {
        "add": operator.add,
        "sub": operator.sub,
        "min": lambda x, y: x if x < y else y,
        "max": lambda x, y: x if x > y else y,
    }
    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant": partial(base_enchantment, 50, "fire"),
        "ice_enchant": partial(base_enchantment, 50, "ice") ,
        "lightning_enchant": partial(base_enchantment, 50, "lightining")
    }


def memoized_fibonacci(n: int) -> int:








def main():
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(spell_powers, 'add')}")
    print(f"sub: {spell_reducer(spell_powers, 'sub')}")
    print(f"min: {spell_reducer(spell_powers, 'min')}")
    print(f"max: {spell_reducer(spell_powers, 'max')}")

    print("\nTesting partial enchanter...")
    def base_enchantment(power, element, target):
        return f"{element} enchantment ({power}) on {target}"

    enchants = partial_enchanter(base_enchantment)
    print(enchants["fire_enchant"]("sword"))
    print(enchants["ice_enchant"]("wand"))
    print(enchants["lightning_enchant"]("staff"))

    print("\nTesting memoized fibonacci...")
    



if __name__ == "__main__":
    main()
