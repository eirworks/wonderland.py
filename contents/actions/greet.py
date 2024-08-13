from wonder.game import Game
from wonder.visual.character_frame import character_frame


def action_greet(game: Game) -> Game:
    print("Hello {}".format(game.player.first_name))
    return game


def action_stats(game: Game) -> Game:
    character_frame(game.player)
    return game
