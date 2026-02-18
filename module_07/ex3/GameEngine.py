class GameEngine:
    def __init__(self):
        self.factory = None
        self.strategy = None
        self.hand = []
        self.battlefield = []
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0



        def configure_engine(self, factory, strategy):
            self.factory = factory
            self.strategy = strategy

            #create starting hand
            self.hand = self.factory.create_themed_deck(3)
            self.cards_created = len(self.hand)

        def simulate_turn(self) -> dict:
            self.turns_simulated += 1

            result = self.strategy.execute_turn(self.hand, self.battlefield)
            self.total_damage += result["damage_dealt"]
            return result


        def get_engine_status(self) -> dict:
            return {
                "turns_simulated": self.turns_simulated,
                "strategy_used": self.strategy.get_strategy_name(),
                "total_damage": self.total_damage,
                "cards_created": self.cards_created,
            }
