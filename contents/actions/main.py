import click

from contents.event_registry import trigger_event
from wonder.game import Game
from wonder.visual.time import month_name


def action_age(game: Game) -> Game:
    ageing(game)

    trigger_event(game)

    click.secho("{}, Year {}".format(month_name(game.month), game.player.age))

    return game


def action_time(game: Game) -> Game:
    print("Month: {} Year: {}".format(game.month, game.player.age))
    return game


def ageing(game: Game) -> Game:
    # update month
    if game.month == 12:
        game.month = 1
    else:
        game.month += 1

    # ageing player
    if game.month == game.player.birth_month:
        game.player.age += 1

    # ageing all characters
    for character in game.relationships:
        if game.month == character.birth_month:
            character.age += 1

    return game
