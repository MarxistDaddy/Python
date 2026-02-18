from abc import ABC, abstractmethod

class GameStrategy(ABC):
    @abstractmethod
    def execute_turn(self, hand:list, battlefield: list) -> dict:
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        pass

    @abstractmethod
    def execute_turn(self, available_targets: list) -> list:
        pass
