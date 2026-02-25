# Core Cards
from .ex0.Card import Card
from .ex0.CreatureCard import CreatureCard

# Deck System
from .ex1.SpellCard import SpellCard
from .ex1.ArtifactCard import ArtifactCard
from .ex1.Deck import Deck

# Ability System
from .ex2.Combatable import Combatable
from .ex2.Magical import Magical
from .ex2.EliteCard import EliteCard

# Engine + Patterns
from .ex3.GameStrategy import GameStrategy
from .ex3.AggressiveStrategy import AggressiveStrategy
from .ex3.CardFactory import CardFactory
from .ex3.FantasyCardFactory import FantasyCardFactory
from .ex3.GameEngine import GameEngine

# Tournament System
from .ex4.Rankable import Rankable
from .ex4.TournamentCard import TournamentCard
from .ex4.TournamentPlatform import TournamentPlatform


__all__ = [
    # Core
    "Card",
    "CreatureCard",

    # Deck
    "SpellCard",
    "ArtifactCard",
    "Deck",

    # Abilities
    "Combatable",
    "Magical",
    "EliteCard",

    # Engine
    "GameStrategy",
    "AggressiveStrategy",
    "CardFactory",
    "FantasyCardFactory",
    "GameEngine",

    # Tournament
    "Rankable",
    "TournamentCard",
    "TournamentPlatform",
]
