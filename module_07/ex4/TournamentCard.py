from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
        self,
        card_id,
        name,
        cost,
        rarity,
        power,
        health,
        rating=1200
    ):
        super().__init__(name, cost, rarity)
        self.card_id = card_id
        self.power = power
        self.health = health
        self.wins = 0
        self.losses = 0
        self.rating = rating

    def play(self, game_state: dict) -> dict:
        return {"action": "played", "card": self.name}

    def attack(self, target) -> dict:
        return {
            "attacker": self.card_id,
            "target": target.card_id,
            "damage": self.power,
        }

    def defend(self, incoming_damage: int) -> dict:
        self.health -= incoming_damage

        if self.health <= 0:
            status = "defeated"
        else:
            status = "alive"

        return {
            "card_id": self.card_id,
            "remaining_health": self.health,
            "status": status
        }

    def get_combat_stats(self) -> dict:
        return {
            "power": self.power,
            "healht": self.health
        }

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += 16 * wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= 16 * losses

    def get_rank_info(self) -> dict:
        return {
            "id": self.card_id,
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}"
        }

    def get_tournament_stats(self) -> dict:
        return {
            "name": self.name,
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }
