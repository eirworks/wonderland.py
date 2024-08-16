import click

from wonder.character.browser import character_browser
from wonder.game import Game


def action_family(game: Game) -> Game:
    click.echo("Your family members:")
    character_browser(game, relationship_type="family")
    return game


def action_characters(game: Game) -> Game:
    click.echo("All characters:")
    character_browser(game)
    return game


def action_lovers(game: Game) -> Game:
    click.echo("Your lovers:")
    character_browser(game, relationship_type="lover")
    return game
