import click

from wonder.game import Game
from wonder.prompts.ask import wait_prompt


def character_browser(game: Game, filter: str = 'all', size: int = 6):
    characters = game.relationships
    chunk_list = list()

    for i in range(0, len(characters), size):
        chunk_list.append(characters[i:i+size])

    current_page = 0

    while True:
        click.echo("Page {} of {}".format(current_page + 1, len(chunk_list)))
        for character in chunk_list[current_page]:
            click.echo("- {} - {}".format(character.name_summary(), character.char_id))
        click.echo("Type `more`, `quit`, `page`")
        prompt = input(">> ")

        if prompt == "more":
            if current_page == len(chunk_list) - 1:
                current_page = 0
            else:
                current_page += 1
        elif prompt == "quit":
            break
        elif prompt == "page":
            page = int(input("Which page: "))
            if 1 <= page <= len(chunk_list):
                current_page = page - 1
            else:
                click.echo("Invalid page number!")
                wait_prompt()
