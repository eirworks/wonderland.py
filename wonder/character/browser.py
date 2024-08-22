import click

from data.character import Character
from data.npc import NonPlayerCharacter
from wonder.prompts.ask import wait_prompt


def character_browser(characters: list, size: int = 6):
    if len(characters) == 0:
        click.secho("No result", fg='yellow')
        return

    if len(characters) <= size:
        for character in characters:
            click.echo(character_info_line(character))
        return

    chunk_list = list()

    for i in range(0, len(characters), size):
        chunk_list.append(characters[i:i + size])

    current_page = 0

    while True:
        click.echo("Page {} of {}".format(current_page + 1, len(chunk_list)))
        for character in chunk_list[current_page]:
            click.echo(character_info_line(character))
        click.echo("Type `more`, `c` to cancel, `page` to go to a page")
        prompt = input(">> ")

        if prompt == "more":
            if current_page == len(chunk_list) - 1:
                current_page = 0
            else:
                current_page += 1
        elif prompt in ["c", "cancel"]:
            break
        elif prompt == "page":
            page = int(input("Which page: "))
            if 1 <= page <= len(chunk_list):
                current_page = page - 1
            else:
                click.echo("Invalid page number!")
                wait_prompt()


def character_info_line(character: NonPlayerCharacter | Character) -> str:
    return "- {} - {} - {} {}".format(
        character.name_summary(),
        character.char_id,
        character.family_relationship_name(),
        character.lover_relationship_name())
