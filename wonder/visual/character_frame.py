import locale

import click

from data.character import Character
from data.npc import FamilyRelationship
from data.relationship import find_by_family
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

        father = find_by_family(game, FamilyRelationship.FATHER)
        mother = find_by_family(game, FamilyRelationship.MOTHER)
        print("-" * 6)

        click.echo("Father: {}".format(father.name_summary() or "None"))
        click.echo("Mother: {}".format(mother.name_summary() or "None"))
    print("-" * 10)
