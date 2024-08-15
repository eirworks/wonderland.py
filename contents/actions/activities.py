import click

from contents.activities_registry import activities_registry
from wonder.game import Game


def action_activity(game: Game) -> Game:
    click.echo("Activities -- Select Category:")
    for category in activities_registry():
        click.echo("- {} ({})".format(category.name, len(category.activities)))
    return game
