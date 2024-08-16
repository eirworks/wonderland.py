import click

from character.query import find_by_id
from visual.character_frame import character_frame
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


def action_character_find(game: Game) -> Game:
    click.echo("Input character ID to find character")
    character_id = click.prompt("ID", default="", show_default=False)
    character = find_by_id(game, character_id)
    if character:
        character_frame(game, character, complete=True)
    else:
        click.secho("Cannot find character with ID `{}`".format(character_id), fg='red')

    return game
