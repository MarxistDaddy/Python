from abc import ABC, abstractmethod

#self name, cost an rarit
class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    #include play when overwriting this abstract method!
    @abstractmethod
    def play(self, gane_state: dict) -> dict:
        pass

    #rturn a dic thta include the info about card!
    #the only added is the name of the card
    def get_card_info(self) -> dict:
        return {
            "name": self.name, 
            "cost": self.cost, 
            "rarity": self.rarity, 
            "type": self.__class__.__name__.replace("card", "")
        }

    #we pass mana, and see if the amount of mana we have can pay for itself
    #we return a boolean of true or false!
    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost

