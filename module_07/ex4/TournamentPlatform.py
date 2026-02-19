
class TournamanePlatform:
    def __init__(self):
        self.cards = {}
        self.matches_played = 0

    def register_card(self, card) -> str:
        self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        self.matches_played += 1

        if card1.power > card2.power:
            winner = card1
            loser = card2
        else:
            winner = card2
            loser = card1

        winner.update_wins(1)
        loser.update_losses(1)

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating,
        }


    def get_leaderboard(self) -> list:
        cards_list = list(self.cards.values())

        for i in range(len(cards_list))
            max_index = i
            for j in range(i + 1, len(cards_list)):
                if cards_list[j].rating > cards_list[max_index].rating:
                    max_index = j
        
            cards_list[i], cards_list[max_index] = cards_list[max_index], cards_list[i]

        leaderboard = []

        position = 1
        for card in cards_list:
            leaderboard.append(
                f"{position}. {card.name} - Rating: {card.ratng} ({card.wins}-{card.losses})"
            )
            position += 1

        return leaderboard


    def generate_tournament_reort(self) -> dict:
        total_rating = sum(card.rating for card in self.cards.values())

        avg_rating = total_rating // len(self.cards) if self.cards else 0

        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }

