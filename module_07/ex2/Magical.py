from abc import ABC, abstractmethod

class Magical(ABC):
    @abstractclass
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        pass

    @abstractclass
    def channel_mana(self, amout: int) -> dict:
        pass

    @abstractclass
    def get_magic_stats(self) -> dict:
        pass
