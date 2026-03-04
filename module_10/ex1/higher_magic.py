test_values = [14, 6, 10]
test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']


def fireball(target: str) -> str:
    return f"Fireball hits {target}"


def heal(target: str) -> str:
    return f"Heals {target}"


def damage_spell(power: int) -> int:
    return power


def strong_only(target: str) -> bool:
    return target == "Knight"


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(arg):
        res1 = spell1(arg)
        res2 = spell2(arg)
        return (res1, res2)
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplifier(arg):
        return base_spell(arg) * multiplier
    return amplifier


def conditional_caster(condition: callable, spell: callable) -> callable:
    def check_condition(arg):
        if condition(arg):    #target value to strong only!
            return spell(arg) #function that returns output of spell, fireball!
        else:
            return "Spell fizzled"
    return check_condition


def spell_sequence(spells: list[callable]) -> callable:
    def run_all(arg):
        res = []
        for s in spells:
            res.append(s(arg))
        return res
    return run_all


def main():
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print("Combined spell result:", combined(test_targets[0]))
    
    print("\nTesting power amplifier...")
    amp = power_amplifier(damage_spell, 3)
    for n in test_values:
        print(f"Original: {n}, Amplified: {amp(n)}")

    print("\nTesting conditional caster...")
    check = conditional_caster(strong_only, heal)
    for n in test_targets:
        print(f"can I hit this target {n}: {check(n)}")
    
    print("\nTesting spell sequence...")
    run = spell_sequence([fireball, heal, strong_only])
    for v in test_targets:
        print(f"casting all spells: {run(v)}")

if __name__ == "__main__":
    main()

