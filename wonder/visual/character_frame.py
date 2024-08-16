import locale

import click

from wonder.data.character import Gender
from wonder.data.npc import FamilyRelationship
from wonder.character.query import find_by_family
from wonder.game import Game
from wonder.visual.time import month_name


def character_frame(game: Game, complete: bool = False):
    locale.setlocale(locale.LC_ALL, '')
    print("-"*10)
    print(game.player.full_name)
    print("Age: {} Birth: {}".format(game.player.age, month_name(game.player.birth_month)))
    print("{} {}".format(game.player.gender, game.player.orientation))
    print("Cash: {}".format(locale.currency(game.player.money)))
    if complete:
        print("-" * 6)
        print("ID: {}".format(game.player.char_id))
        game.player.stats.print_stats()

        father = find_by_family(game, FamilyRelationship.PARENT, gender=Gender.MALE)
        mother = find_by_family(game, FamilyRelationship.PARENT, gender=Gender.FEMALE)
        print("-" * 6)
        if father is not None:
            click.echo("Father: {}".format(father.name_summary() or "None"))
        if mother is not None:
            click.echo("Mother: {}".format(mother.name_summary() or "None"))

        traits = ", ".join([trait.name for trait in game.player.traits])
        click.echo("Traits: {}".format(traits))
    print("-" * 10)
