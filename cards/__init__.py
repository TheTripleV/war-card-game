from abc import ABC, abstractmethod
from collections import deque
from typing import Deque, List


class Card(ABC):
    @staticmethod
    @abstractmethod
    def create_decks(num_players: int) -> List[Deque["Card"]]:
        """Create decks for each player based on the card type"""
        raise NotImplementedError

    @abstractmethod
    def __lt__(self, other) -> bool:
        raise NotImplementedError

    @abstractmethod
    def __eq__(self, other) -> bool:
        raise NotImplementedError
