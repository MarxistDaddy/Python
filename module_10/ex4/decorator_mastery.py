from functools import wraps
import time

test_powers = [15, 9, 5, 7]
spell_names = ['meteor', 'darkness', 'lightning', 'shield']
mage_names = ['Ash', 'Casey', 'Phoenix', 'Storm', 'Jordan', 'Zara']
invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper():
        print(f"Casting {wrapper.__name__}...")
        start = time.time()
        res = func()
        time.sleep(0.5)
        end = time.time()
        print(f"Spell completed in {end - start:2.1f} seconds")
        return res
    return wrapper


def fireball():
    return "Fireball cast!"


def power_validator(min_power: int) -> callable:
    def decorator_func(base_func: callable) -> callable:
        @wraps(base_func)
        def enhanced(*args, **kwargs):
            power = args[-1]
            if power >= min_power:
                return base_func(*args, **kwargs)
            return "Insufficient power for this spell"
        return enhanced
    return decorator_func


def cast_spell(power: int):
    return f"casting a spell with {power} power"


def retry_spell(max_attempts: int) -> callable:
    def retry_decorator(base_func: callable):
        def enhanced_f(power: int):
            i = 0
            while i < max_attempts:
                try:
                    return base_func(power)
                except Exception:
                    print("Spell failed, retrying... ")
                    power += 1
                i += 1
            return "Spell casting failed after max_attempts attempts"
        return enhanced_f
    return retry_decorator


def cast_power(power: int):
    if power >= 5:
        return f"casting power: {power} damage"
    else:
        raise ValueError("power is too low!")


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str):
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Casting {spell_name} with {power} power"


def main():
    print("Testing spell timer...")
    wrap_f = spell_timer(fireball)
    res = wrap_f()
    print("Result:", res)
    print("\nTesting power validator...")
    enh = power_validator(6)(cast_spell)
    for v in test_powers:
        print(enh(v))

    print("\nTesting retry spell...")
    safe_casting = retry_spell(3)(cast_power)
    print(safe_casting(4))

    print("\nTesting Mafe Guild...")
    mage_object = MageGuild()
    print(MageGuild.validate_mage_name("hello world"))
    print(mage_object.validate_mage_name("hello world"))
    for name, power in zip(spell_names, test_powers):
        print(mage_object.cast_spell(name, power))


if __name__ == "__main__":
    main()
