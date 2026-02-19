from ex3.GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard

class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = []
        damage = 0
        mana_used = 0

        # Sort by cost manually
        for i in range(len(hand)):
            min_index = i
            for j in range(i + 1, len(hand)):
                if hand[j].cost < hand[min_index].cost:
                    min_index = j

            hand[i], hand[min_index] = hand[min_index], hand[i]

        count = 0
        for card in hand:
            if count == 2:
                break

            cards_played.append(card.name)
            mana_used += card.cost

            if isinstance(card, CreatureCard):
                damage += card.attack
            elif isinstance(card, SpellCard):
                damage += 6

            count += 1

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": damage
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets

