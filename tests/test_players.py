from cards.standardcard import StandardCard

Suit = StandardCard.Suit
Rank = StandardCard.Rank

from players.naiveplayer import NaivePlayer


def test_return_cards():
    cards_to_ret = [
        StandardCard(Suit.HEART, Rank.TWO),
        StandardCard(Suit.DIAMOND, Rank.THREE),
    ]

    player = NaivePlayer()
    player.return_cards_to_deck(cards_to_ret)

    for card in cards_to_ret:
        assert card in player.deck
