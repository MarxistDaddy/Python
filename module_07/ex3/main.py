from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy

def main():
    print("=== DataDeck Game Engine ===\n")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    engine = GameEngine()
    engine.configure_engine(factory, strategy)
    
    print("Configuring Fantasy Card Game...")
    print("Factory:", factory.__class__.__name__)
    print("Strategy:", strategy.__class__.__name__)
    print("Available types:", factory.get_supported_types())


    print("\nSimulating aggressive turn...")
    print("Hand:", [f"{card.name} ({card.cost})" for card in engine.hand])

    turn_result = engine.simulate_turn()

    print("\nTurn execution:")
    print("Strategy:", strategy.get_strategy_name())
    print("Actions:", turn_result)

    print("\nGame Report:")
    print(engine.get_engine_status())
    print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")

if __name__ == "__main__":
    main()
