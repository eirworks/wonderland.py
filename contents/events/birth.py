"""
Birth events are special events that triggered when character created.
It introduces parents and siblings of player's character.
"""
import locale
import random

import click
from faker import Faker

import data.npc
from contents.event_registry import calculate_trigger_weight
from data.character import Gender
from wonder.game import Game


def list_birth_events() -> list:
    return [
        (event_birth_good, 10),
        (event_birth_bad, 0.1),
    ]


def event_birth_good(game: Game) -> Game:
    sub_events = [
        (perfect_parent, 0.5),
        # (good_parent, 1),
        # (normal_parent, 5),
    ]

    game = calculate_trigger_weight(game, sub_events)(game)

    return game


def event_birth_bad(game: Game) -> Game:
    print("You were born with severe disfunctional limbs!")
    return game


def perfect_parent(game: Game) -> Game:
    """
    Create perfect parents:
    - alive and healthy parents
    - young parents (20 - 25)
    - rich parents

    :param Game game: The game object
    :return game object
    """

    fake = Faker()

    family_name = game.player.last_name

    father = data.npc.NonPlayerCharacter()
    father.adult()
    father.first_name = fake.first_name_male()
    father.last_name = family_name
    father.family = data.npc.FamilyRelationship.FATHER
    father.money = random.randrange(10000, 100000)
    father.relationship = 1

    game.relationships.append(father)

    mother = data.npc.NonPlayerCharacter()
    mother.adult()
    mother.first_name = fake.first_name_female()
    mother.last_name = family_name
    mother.gender = Gender.FEMALE
    mother.family = data.npc.FamilyRelationship.MOTHER
    mother.money = random.randrange(10000, 100000)
    mother.relationship = 1

    game.relationships.append(mother)

    allowance = 5000
    click.echo("You are lucky being born from father {} and mother {}".format(father.full_name, mother.full_name))
    click.echo("Your parent are rich, you got {} allowance".format(locale.currency(allowance)))
    game.give_money(allowance)

    return game
