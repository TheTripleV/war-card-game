from typing import List

from cards import Card
from players import Player


class NaivePlayer(Player):
    def return_cards_to_deck(self, cards: List[Card]) -> None:
        self.deck.extend(cards)
