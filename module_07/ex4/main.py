from ex4.TournamentCard import TournamentCard
from ex4.TournamanetPlatfrom import TournamentPlatform

def main():
    print("=== DataDeck Tournament Platform ===\n")

    platform = TournamentPlatform()

    dragon = TournamentCard("dragon_001", "Fire Dragon", 10, 8, 1200)
    wizard = TournamentCard("wizard_001", "Ice Wizard", 7, 6, 1150)

    print("\negistering Tournament Cards...")

    platform.register_card(dragon)
    platform.register_card(wizard)

    print(f"{dragon.name} (id: {dragon.card_id})")
    print("- interface: [card, combatable, rankable]")
    print("- rating:", dragon.rating)
    print("- record: 0-0")



    print(f"{wizard.name} (id: {wizard.card_id})")
    print("- interface: [card, combatable, rankable]")
    print("- rating:", wizard.rating)
    print("- record: 0-0")
    
    print("\nCreating tournament match...")
    result = platform.create_match("dragon_001", "wizard_001")
    print("Match result:", result)

    print("\nTournament Leaderboard:")
    for entry in platform.het_leaderboad():
        print(entry)

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")

if __name__ == "__main__":
    main()

