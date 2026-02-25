import ex0


def main():
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")
    print("CreatureCard:")
    c_card = ex0.CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print(c_card.get_card_info(), "\n")
    print("Playing Fire Dragon with 6 mana available:")
    print(f"Playable: {c_card.is_playable(6)}")
    print(c_card.play(c_card.get_card_info()), "\n")
    print("Fire Dragon attacks Goblin Warrior:")
    print("Attack result:", c_card.attack_target("Goblin Warrior"))
    print("\nTesting insufficient mana (3 available):")
    print("Playable: ", c_card.is_playable(3))
    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
