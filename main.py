from cards.smallstandardcard import SmallStandardCard
from cards.standardcard import StandardCard
from games.wikipediagame import WikipediaGame
from play import play_war
from players.naiveplayer import NaivePlayer

play_war(
    card_type=SmallStandardCard,
    game_type=WikipediaGame,
    player_types=[NaivePlayer, NaivePlayer],
)
