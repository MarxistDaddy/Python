from abc import ABC, abstractmethod

class CardFactory(ABC):
    @abstrctmethod
    def create_creatuere(self, name_or_power) -> Card:
       pass

    @abstractmethod
    def create_spell(sekf, name_power) -> Card:
        pass

    @abstractmethod
    def create_artifact(self, name_or_power) -> Card:
        pass

    @abstractmethod
    def create_themed_deck(self, size:int) -> dict:
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        pass

