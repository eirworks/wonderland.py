import click

from wonder.game import Game
from wonder.visual.character_frame import character_frame


def action_greet(game: Game) -> Game:
    print("Hello {}".format(game.player.first_name))
    return game


def action_stats(game: Game) -> Game:
    character_frame(game, game.player)
    return game


def action_stats_all(game: Game) -> Game:
    character_frame(game, game.player, True)
    return game


def action_traits(game: Game) -> Game:
    traits = ", ".join([trait.name for trait in game.player.traits])
    click.echo("Traits: {}".format(traits))

    return game
