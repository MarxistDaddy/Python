from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck



def main():
    print("=== DataDeck Deck Builder ===\n")
    print("Building Deck with different card types...")

    Deck_card = Deck()
    creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    spell = SpellCard("Lightning Bold", 3, "Rare", "damage")
    artifact = ArtifactCard("Mana Crystal", 2, "Common", 10, "1 mana per turn")
    
    #building Deck
    Deck_card.add_card(spell)
    Deck_card.add_card(artifact)
    Deck_card.add_card(creature)

    print(Deck_card.get_deck_stats())
    print("\nDrawing and playing cards:\n")

    while Deck_card.cards:
        c = Deck_card.draw_card()
        if isinstance(c, CreatureCard):
            print(f"drew: {c.name} (Creature)")
        elif isinstance(c, SpellCard):
            print(f"drew: {c.name} (Spell)")
        elif isinstance(c, ArtifactCard):
            print(f"drew: {c.name} (Artifact)")
        print(f"Play result: {c.play(c.get_card_info())} \n")

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()

