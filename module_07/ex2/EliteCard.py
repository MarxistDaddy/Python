from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
        mana_pool: int
    ):
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.health = health
        self.mana = mana_pool

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elit card enters the battlefield",
        }

    def attack(self, target: str) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_blocked = min(self.attack_power // 2, incoming_damage)
        damage_taken = incoming_damage - damage_blocked
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack_power": self.attack_power,
            "health": self.health,
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_cost = len(targets)
        if self.mana < mana_cost:
            return {"error": "Not enough mana"}
        self.mana -= mana_cost
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_cost,
        }

    def channel_mana(self, amount: int) -> dict:
        return {
            "channeled": amount,
            "total_mana": self.mana,
        }

    def get_magic_stats(self) -> dict:
        return {"mana_pool": self.mana}
