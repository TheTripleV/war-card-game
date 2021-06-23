from collections import deque

from cards.smallstandardcard import SmallStandardCard
from games.wikipediagame import WikipediaGame
from players.naiveplayer import NaivePlayer

Rank = SmallStandardCard.Rank


def test_end_condition_counts():
    players = [
        NaivePlayer(deque([SmallStandardCard(Rank.TEN)])),
        NaivePlayer(deque([])),
    ]

    game = WikipediaGame(players)

    assert game.is_end_condition_met() == True


def test_end_condition_out():
    players = [
        NaivePlayer(deque([SmallStandardCard(Rank.TEN)])),
        NaivePlayer(deque([])),
    ]

    game = WikipediaGame(players)
    players[0].is_out = False
    players[1].is_out = True

    assert game.is_end_condition_met() == True


def test_battle_not_finished():
    players = [NaivePlayer(deque()), NaivePlayer(deque())]

    players[0].hand.append(SmallStandardCard(Rank.TEN))
    players[1].hand.append(SmallStandardCard(Rank.TEN))

    game = WikipediaGame(players)

    assert game.is_battle_finished() == False


def test_battle_finished():
    players = [NaivePlayer(deque()), NaivePlayer(deque())]

    players[0].hand.append(SmallStandardCard(Rank.TEN))
    players[1].hand.append(SmallStandardCard(Rank.JACK))

    game = WikipediaGame(players)

    assert game.is_battle_finished() == True


def test_deal():
    players = [
        NaivePlayer(deque([SmallStandardCard(Rank.TEN)])),
        NaivePlayer(deque([SmallStandardCard(Rank.JACK)])),
    ]

    game = WikipediaGame(players)
    game.deal()

    assert players[0].hand == deque([SmallStandardCard(Rank.TEN)])
    assert players[1].hand == deque([SmallStandardCard(Rank.JACK)])


def test_partial_deal():
    players = [NaivePlayer(deque([SmallStandardCard(Rank.TEN)])), NaivePlayer(deque())]

    game = WikipediaGame(players)
    game.deal()

    assert players[0].hand == deque([SmallStandardCard(Rank.TEN)])
    assert players[1].hand == deque()


def test_tie():
    players = [
        NaivePlayer(deque([SmallStandardCard(Rank.TEN)] * 10)),
        NaivePlayer(deque([SmallStandardCard(Rank.TEN)] * 10)),
    ]

    game = WikipediaGame(players)
    game.on_tie()

    assert players[0].hand == deque([SmallStandardCard(Rank.TEN)] * 4)
    assert players[1].hand == deque([SmallStandardCard(Rank.TEN)] * 4)


def test_return_cards_to_decks():
    players = [
        NaivePlayer(deque()),
        NaivePlayer(deque()),
    ]

    game = WikipediaGame(players)

    players[0].hand.append(SmallStandardCard(Rank.ACE))
    players[1].hand.append(SmallStandardCard(Rank.SEVEN))

    game.return_cards_to_decks(0)

    assert len(players[1].deck) == 0
    assert len(players[1].hand) == 0

    assert len(players[0].deck) == 2
    assert len(players[0].hand) == 0

    assert SmallStandardCard(Rank.ACE) in players[0].deck
    assert SmallStandardCard(Rank.SEVEN) in players[0].deck


def test_return_cards_to_decks_1():
    players = [
        NaivePlayer(deque()),
        NaivePlayer(deque()),
    ]

    game = WikipediaGame(players)

    players[0].hand.append(SmallStandardCard(Rank.ACE))
    players[1].hand.append(SmallStandardCard(Rank.SEVEN))

    game.return_cards_to_decks(1)

    assert len(players[0].deck) == 0
    assert len(players[0].hand) == 0

    assert len(players[1].deck) == 2
    assert len(players[1].hand) == 0

    assert SmallStandardCard(Rank.ACE) in players[1].deck
    assert SmallStandardCard(Rank.SEVEN) in players[1].deck


def test_get_battle_winner():
    players = [
        NaivePlayer(deque()),
        NaivePlayer(deque()),
    ]

    game = WikipediaGame(players)

    players[0].hand.append(SmallStandardCard(Rank.ACE))
    players[1].hand.append(SmallStandardCard(Rank.SEVEN))

    assert game.get_battle_winner() == 0


def test_get_battle_winner_1():
    players = [
        NaivePlayer(deque()),
        NaivePlayer(deque()),
    ]

    game = WikipediaGame(players)

    players[0].hand.append(SmallStandardCard(Rank.SEVEN))
    players[1].hand.append(SmallStandardCard(Rank.ACE))

    assert game.get_battle_winner() == 1
