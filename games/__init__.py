from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

from players import Player


@dataclass
class Game(ABC):
    players: List[Player]

    @abstractmethod
    def is_end_condition_met(self) -> bool:
        """Whether the game can be ended at this point"""
        raise NotImplementedError

    @abstractmethod
    def is_battle_finished(self, ties_played: int = 0) -> bool:
        """Whether a battle has ended at this point"""
        raise NotImplementedError

    @abstractmethod
    def deal(self) -> None:
        """Move cards(s) from each players decks to their hands"""
        raise NotImplementedError

    @abstractmethod
    def on_tie(self, ties_played: int = 0):
        """Action to attempt to resolve the tie"""
        raise NotImplementedError

    @abstractmethod
    def return_cards_to_decks(self, winning_player_idx: int):
        """Give all hands to the winning player"""
        raise NotImplementedError

    @abstractmethod
    def get_battle_winner(self) -> int:
        """Determine the winning player of a battle"""
        raise NotImplementedError
