from collections import deque
from enum import Enum, auto
from random import shuffle
from typing import Deque, List

from cards import Card


class StandardCard(Card):
    class Suit(Enum):
        HEART = auto()
        SPADE = auto()
        CLOVER = auto()
        DIAMOND = auto()

    class Rank(Enum):
        TWO = auto()
        THREE = auto()
        FOUR = auto()
        FIVE = auto()
        SIX = auto()
        SEVEN = auto()
        EIGHT = auto()
        NINE = auto()
        TEN = auto()
        JACK = auto()
        QUEEN = auto()
        KING = auto()
        ACE = auto()

    def __init__(self, suit: Suit, rank: Rank) -> None:
        self.suit = suit
        self.rank = rank

    def __lt__(self, other) -> bool:
        return self.rank.value < other.rank.value

    def __eq__(self, other) -> bool:
        return self.rank.value == other.rank.value

    def __repr__(self) -> str:
        # return f"({self.suit}, {self.rank})"
        return f"{self.rank}"

    @staticmethod
    def create_decks(num_players: int) -> List[Deque["Card"]]:
        decks = [deque() for _ in range(num_players)]
        full_deck = []
        for suit in StandardCard.Suit:
            for rank in StandardCard.Rank:
                full_deck.append(StandardCard(suit, rank))

        shuffle(full_deck)

        for i in range(len(full_deck)):
            decks[i % num_players].append(full_deck[i])

        return decks
