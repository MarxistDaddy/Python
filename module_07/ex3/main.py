from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy

def main():
    print("=== DataDeck Game Engine ===")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    engine = GameEngine()
    engine.configure_engine(factory, strategy)
    
    print("Factory:", factory.__class__.__name__)
    print("Strategy:". strategy.__class__.__name__)
    print("Available types", factory.get_supported_types())


    print("\nSimulating aggressive turn...")
    print("Hand:", [f"{card.name}}" for card in engine.hand])

    tun_result = engine.simulate_turn()

    print("Turn execution:", turn_result)

    print("\nGame Report:")
    print(engine.get_engine_status())


if __name__ = "__main__":
    main()
