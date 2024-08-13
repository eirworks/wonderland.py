from contents.event_registry import trigger_event
from wonder.game import Game


def action_age(game: Game) -> Game:
    game.month = game.month + 1
    game.player.age = game.player.age + 1

    trigger_event(game)

    return game


def action_time(game: Game) -> Game:
    print("Month: {} Year: {}".format(game.month, game.player.age))
    return game
