from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):
    def create_creature(self, name):
        if name == "dragon":
            return CreatureCard("Fire Dragon", 5, 'Legendary', 7, 5)
        return CreatureCard("Goblin Warrior", 2, "common", 2, 2)

    def create_spell(self, name):
        return SpellCard("FireBall", 3, "Rare", "damage")

    def create_artifact(self, name):
        return ArtifactCard("Mana Ring", 2, "Common", 5, "mana boost")

    def create_themed_deck(self, size: int) -> list:
        deck = []
        options = [
            self.create_creature("dragon"),
            self.create_creature("goblin"),
            self.create_spell("fireball"),
        ]

        for _ in range(size):
            deck.append(options[_])
        return deck[:size]

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }
