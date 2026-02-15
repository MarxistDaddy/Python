from ex0.Card import Card

class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type


    def play(self, game_state: dict) -> dict:
        return {
            "name": self.name,
            "ncost": self.cost,
            "effect": f"{self.effect_type.capitalize()} effect activated",
        }


    def resolve_effect(self, target: list) -> dict:
        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets": targets,
            "resolved": True
        }
    
    
