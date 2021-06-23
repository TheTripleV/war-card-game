from collections import deque
from enum import Enum, auto
from random import shuffle
from typing import Deque, List

from cards import Card
from cards.standardcard import StandardCard


class SmallStandardCard(StandardCard):
    def __init__(self, rank: StandardCard.Rank):
        super().__init__(StandardCard.Suit.HEART, rank)

    @staticmethod
    def create_decks(num_players: int) -> List[Deque["Card"]]:
        decks = [deque() for _ in range(num_players)]
        full_deck = []
        for rank in StandardCard.Rank:
            full_deck.append(StandardCard(StandardCard.Suit.HEART, rank))

        shuffle(full_deck)

        for i in range(len(full_deck)):
            decks[i % num_players].append(full_deck[i])

        return decks
