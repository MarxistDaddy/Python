from ex0.Card import Card

class CreatureCard(Card):
    def __init__(self, 
            name: str, cost: int, rarity: str, attack: int, health: int):

        #extend th constructor method, by adding attack and heakth
        super().__init__(name, cost, rarity)

        if attack <= 0 or health <= 0:
            raise ValueError("Attack and health must be positive integers")

        self.attack = attack
        self.health = health

    #override abstract class
    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned tp battlefield",
        }

    def attack_target(self, target: str) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }

    def get_card_info(self) -> dict:
        
        #extend this get_card_info method, by adding attack and health!
        base_info = super().get_card_info()
        
        return {
            "name": base_info["name"], 
            "cost": base_info["cost"], 
            "rarity": base_info["rarity"], 
            "type": base_info["type"], 
            "attack": self.attack, 
            "health": self.health,
        }


