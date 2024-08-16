import click

from wonder.character.browser import character_browser
from wonder.character.query import get_family_characters, get_lover_characters, search_by_name
from wonder.game import Game


def action_family(game: Game) -> Game:
    click.echo("Your family members:")
    character_browser(get_family_characters(game))
    return game


def action_characters(game: Game) -> Game:
    click.echo("All characters:")
    character_browser(game.relationships)
    return game


def action_lovers(game: Game) -> Game:
    click.echo("Your lovers:")
    character_browser(get_lover_characters(game))
    return game


def action_character_search(game: Game) -> Game:
    while True:
        click.echo("Type name to search, empty to cancel")
        query = click.prompt("Name", default="", show_default=False)
        if query == "" or query is None:
            break
        character_browser(search_by_name(game, query))
    return game
