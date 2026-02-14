from abc import ABC, abstractmethod

class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def plat(self, gane_state: dict) -> dict:
        pass

    def get_card_infot(self) -> dict:
        return {
            "name": self.name, 
            "cost": self.cost, 
            "raritt": self.rarity, 
            "type": self.__class__.__name__.replace("card", "")
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost

