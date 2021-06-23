import pytest

from cards.standardcard import StandardCard

Suit = StandardCard.Suit
Rank = StandardCard.Rank

params_lt = [
    (StandardCard(Suit.HEART, Rank.TWO), StandardCard(Suit.DIAMOND, Rank.THREE)),
    (StandardCard(Suit.CLOVER, Rank.TWO), StandardCard(Suit.HEART, Rank.ACE)),
    (StandardCard(Suit.SPADE, Rank.FOUR), StandardCard(Suit.SPADE, Rank.KING)),
    (StandardCard(Suit.DIAMOND, Rank.JACK), StandardCard(Suit.HEART, Rank.QUEEN)),
]


@pytest.mark.parametrize("card1,card2", params_lt)
def test_lt(card1, card2):
    assert card1 < card2


params_eq = [
    (StandardCard(Suit.HEART, Rank.TWO), StandardCard(Suit.HEART, Rank.TWO)),
    (StandardCard(Suit.CLOVER, Rank.TWO), StandardCard(Suit.CLOVER, Rank.TWO)),
    (StandardCard(Suit.SPADE, Rank.FOUR), StandardCard(Suit.SPADE, Rank.FOUR)),
    (StandardCard(Suit.DIAMOND, Rank.JACK), StandardCard(Suit.DIAMOND, Rank.JACK)),
]


@pytest.mark.parametrize("card1,card2", params_eq)
def test_eq(card1, card2):
    assert card1 == card2


params_neq = [
    (StandardCard(Suit.HEART, Rank.TWO), StandardCard(Suit.DIAMOND, Rank.THREE)),
    (StandardCard(Suit.CLOVER, Rank.TWO), StandardCard(Suit.HEART, Rank.ACE)),
    (StandardCard(Suit.SPADE, Rank.FOUR), StandardCard(Suit.SPADE, Rank.KING)),
    (StandardCard(Suit.DIAMOND, Rank.JACK), StandardCard(Suit.HEART, Rank.QUEEN)),
]


@pytest.mark.parametrize("card1,card2", params_neq)
def test_neq(card1, card2):
    assert card1 != card2


def test_1_deck():
    decks = StandardCard.create_decks(1)
    assert len(decks) == 1
    assert len(decks[0]) == 52


def test_2_decks():
    decks = StandardCard.create_decks(2)
    assert len(decks) == 2
    assert len(decks[0]) == 26
    assert len(decks[1]) == 26


@pytest.mark.parametrize("n", range(1, 52))
def test_n_decks(n):
    decks = StandardCard.create_decks(n)
    assert len(decks) == n
    for deck in decks:
        assert abs(len(deck) - (52 // n)) <= 1
