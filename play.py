import code
from typing import List, Type

from cards import Card
from games import Game
from players import Player


def play_war(
    card_type: Type[Card], game_type: Type[Game], player_types: List[Type[Player]]
) -> int:

    rounds_played = 0

    decks = card_type.create_decks(len(player_types))
    players = [player_type(deck) for player_type, deck in zip(player_types, decks)]
    game = game_type(players)

    while not game.is_end_condition_met():
        print("Deck Sizes:", len(players[0].deck), len(players[1].deck))
        game.deal()

        for player in players:
            print(f"{str(player.hand[0]):11}", end="")

        ties_played = 0

        while not game.is_battle_finished(ties_played):  # tie
            print("   tie")
            game.on_tie()

            for player in players:
                print(f"{str(player.hand[0]):11}", end="")

            ties_played += 1

        winner_idx = game.get_battle_winner()

        print(f"  {winner_idx} wins battle.")

        game.return_cards_to_decks(winner_idx)

        rounds_played += 1

    for idx, player in enumerate(players):
        if not player.is_out:
            winner_idx = idx
            print(f"Player {winner_idx} Wins! (0-indexed)")
            return winner_idx
    else:
        raise Exception("Impossible Situation")
