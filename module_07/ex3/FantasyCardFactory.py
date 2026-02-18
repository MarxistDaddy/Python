from ex3.CardFactory import CardFactory
from ex1.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random



class FantasyCardFactor(CardFactory):
    #name, cost_mana, rarity, attack, health
    def create_creature(self, name):
        if name == "dragon":
            return CreatureCard("Fire Dragon", 5, 'Legendary', 7, 5)
        return CreateCard("Goblin Warrior", 2, "common", 2, 2)

    #super, type_effect
    def create_spell(self, name):
        return SpellCard("FireBall", 3, "Rare", "damage")


    #super, durability, effect
    def create_artifact(self, name):
        return ArtifactCard("Mana Ring", 2, "Common", 5, "mana boost")


    def create_themed_deck(self, size: int) -> list:
        deck = []
        #create cards on here based on value passed
        options = [
            self.create_creature("dragon"),
            self.create_creature("goblin"),
            self.create_creature("fireball"),
        ]

        for _ in range(size):
            deck.append(random.choice(options))
        
        return deck


    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }
