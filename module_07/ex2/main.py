from ex2.EliteCard import EliteCard


def main():
    print("=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    elite = EliteCard("Arcane Warrior", 5, "Legendary", attack=5, health=10, mana_pool=4)

    print("- Card: ['play', 'get_card_info', 'is_playable']")  # <<< FIXED
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")  # <<< FIXED
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")  # <<< FIXED

    print(f"\nPlaying Arcane Warrior (Elite Card):\n")


    print("Combat phase:")
    print(f"Attack result: {elite.attack('Enemy')}")
    print(f"Defence result: {elite.defend(5)}")
    print(f"Combat stats: {elite.get_combat_stats()}")

    print("\nMagical phase:")
    print(f"Spell cast: {elite.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {elite.channel_mana(3)}")
    print(f"Magic stats: {elite.get_magic_stats()}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
