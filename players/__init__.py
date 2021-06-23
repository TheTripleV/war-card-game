from abc import ABC, abstractmethod
from collections import deque
from dataclasses import dataclass, field
from typing import Deque, List

from cards import Card


@dataclass
class Player(ABC):
    deck: Deque[Card] = field(default_factory=deque)
    hand: Deque[Card] = field(default_factory=deque)
    is_out: bool = False

    def __len__(self) -> int:
        return len(self.deck) + len(self.hand)

    @abstractmethod
    def return_cards_to_deck(self, cards: List[Card]) -> None:
        """Insert cards into the player's deck"""
        raise NotImplementedError
