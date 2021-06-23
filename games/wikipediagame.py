import enum
from typing import List

from games import Game
from players import Player


class WikipediaGame(Game):
    def is_end_condition_met(self) -> bool:
        for player in self.players:
            if not len(player):
                player.is_out = True

        return 1 == sum(not player.is_out for player in self.players)

    def is_battle_finished(self, ties_played: int = 0) -> bool:

        if self.is_end_condition_met():
            return True
        cards = [p.hand[0] for p in self.players]
        cards.sort(reverse=True)
        return cards[0] != cards[1]

    def deal(self) -> None:
        for player in self.players:
            if player.is_out:
                continue
            if not len(player.deck):
                player.is_out = True
                continue
            player.hand.appendleft(player.deck.popleft())

    def on_tie(self, ties_played: int = 0) -> None:
        # import code
        # code.interact(local={**locals(), **globals()})
        for player in self.players:
            if player.is_out:
                continue
            try:
                for _ in range(4):
                    player.hand.appendleft(player.deck.popleft())
            except IndexError:
                player.is_out = True

    def return_cards_to_decks(self, winning_player_idx: int):
        winning_pile = []

        for player in self.players:
            winning_pile.extend(player.hand)
            player.hand.clear()

        self.players[winning_player_idx].return_cards_to_deck(winning_pile)

    def get_battle_winner(self) -> int:
        possiblities = []
        for idx, player in enumerate(self.players):
            if not player.is_out:
                possiblities.append((idx, player))

        possiblities.sort(reverse=True, key=lambda possibility: possibility[1].hand[0])
        return possiblities[0][0]
