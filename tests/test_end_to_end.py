from collections import deque
from pydoc import plain

from cards.smallstandardcard import SmallStandardCard
from games.wikipediagame import WikipediaGame
from play import play_war
from players.naiveplayer import NaivePlayer

Rank = SmallStandardCard.Rank


def test1():
    class TestCard(SmallStandardCard):
        @staticmethod
        def create_decks(num_players: int):
            return [
                deque(
                    [
                        SmallStandardCard(r)
                        for r in [Rank.TEN, Rank.TEN, Rank.FOUR, Rank.SIX, Rank.QUEEN]
                    ]
                ),
                deque(
                    [
                        SmallStandardCard(r)
                        for r in [Rank.SIX, Rank.KING, Rank.KING, Rank.NINE, Rank.QUEEN]
                    ]
                ),
            ]

    assert 1 == play_war(TestCard, WikipediaGame, [NaivePlayer, NaivePlayer])
