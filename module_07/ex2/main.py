from ex2.EliteCard import EliteCard


def main():
    print("=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    elite = EliteCard("Arcane Warrior", 5, "Legendary", attack=5, health=10, mana_pool=4)

    print(f"\nPlaying ElitCard: {elite.__class__.__name__} (Elite Card):\n")
    print("Combat phase:")
    print(f"Attack result: {elite.attack('Enemy')}")
    print(f"Defence result: {elite.defend(5)}")
    print(f"Combat stats: {elite.get_combat_stats()}")

    print("\nMagical phase:")
    print(f"Spell cast: {elite.cast_spell('Fireball', ['Enemey1', 'Enemey2'])}")
    print(f"Mana channel: {elite.channel_mana(3)}")
    print(f"Magic stats: {elite.get_magic_stats()}")

    print("Multiple interface implementation successful!")

