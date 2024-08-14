import locale

import click

from data.relationship import get_family_characters
from wonder.game import Game


def action_family(game: Game) -> Game:
    click.echo("Your family members:")
    for member in get_family_characters(game):
        click.echo("{}".format(member.name_summary()))
        click.echo("|- Relationship : {} ({})".format(member.family.value.title(), member.relationship))
        click.echo("|- Money        : {}".format(locale.currency(member.money)))
    return game


def action_characters(game: Game) -> Game:
    click.echo("All characters:")
    for member in game.relationships:
        click.echo("{}".format(member.name_summary()))
        click.echo("|- ID           : {}".format(member.char_id))
        click.echo("|- Relationship : {} ({})".format(member.family.value.title(), member.relationship))
        click.echo("|- Money        : {}".format(locale.currency(member.money)))
    return game
