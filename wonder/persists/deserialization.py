import json

from data.character import Character, Gender, Orientation
from data.npc import NonPlayerCharacter, FamilyRelationship
from data.stats import Stats
from game import Game
from traits.common_traits import traits_registry


def deserialize_game_data(data: str|dict) -> Game:
    """
    Rebuilt game instance from a json
    :param data:
    :return:
    """

    if data is str:
        raw_data = json.loads(data)
    else:
        raw_data = data

    game = Game()
    game.month = raw_data['month']
    game.perform = raw_data['perform']
    game.last_id = raw_data['last_id']
    game.player = deserialize_character(raw_data['player'])
    game.relationships = [deserialize_npc(npc) for npc in raw_data['relationships']]

    return game


def deserialize_character(data: dict) -> Character:
    character = Character()
    character.char_id = data['char_id']
    character.age = data['age']
    character.first_name = data['first_name']
    character.last_name = data['last_name']
    character.birth_month = data['birth_month']
    stats = Stats()
    stats.from_json(data['stats'])
    character.stats = stats
    character._gender = Gender.MALE if data['gender'] == 1 else Gender.FEMALE
    character._orientation = deserialize_orientation(data['orientation'])
    character.alive = data['alive']
    character.minor = data['minor']
    character.died_at = (data['died_at'][0], data['died_at'][1])
    character.traits = deserialize_trait(data['traits'])
    character.skills = deserialize_skills(data['skills'])
    character.pregnant_month = data['pregnant_month']

    return character


def deserialize_relationships(values: list) -> list:
    return [deserialize_npc(character) for character in values]


def deserialize_npc(data: dict) -> NonPlayerCharacter:
    character = NonPlayerCharacter()
    character.char_id = data['char_id']
    character.age = data['age']
    character.first_name = data['first_name']
    character.last_name = data['last_name']
    character.birth_month = data['birth_month']
    stats = Stats()
    stats.from_json(data['stats'])
    character.stats = stats
    character._gender = Gender.MALE if data['gender'] == 1 else Gender.FEMALE
    character._orientation = deserialize_orientation(data['orientation'])
    character.alive = data['alive']
    character.minor = data['minor']
    character.died_at = (data['died_at'][0], data['died_at'][1])
    character.traits = deserialize_trait(data['traits'])
    character.skills = deserialize_skills(data['skills'])
    character.pregnant_month = data['pregnant_month']

    character.family = deserialize_family(data['family'])
    character.relationship = data['relationship']
    character.lover = data['lover']
    character.step_family = data['step_family']
    character.in_laws = data['in_laws']

    return character


def deserialize_orientation(value: int) -> Orientation:
    return {
        Orientation.ASEXUAL.value: Orientation.ASEXUAL,
        Orientation.HETEROSEXUAL.value: Orientation.HETEROSEXUAL,
        Orientation.HOMOSEXUAL.value: Orientation.HOMOSEXUAL,
        Orientation.BISEXUAL.value: Orientation.BISEXUAL,
    }[value]


def deserialize_trait(values: list) -> list:
    traits = list()

    registered_traits = traits_registry()
    for value in values:
        for registered_trait in registered_traits:
            if registered_trait.trait_id == value:
                traits.append(registered_trait)

    return traits


def deserialize_skills(values: list) -> list:
    # TODO implement deserialize_skills after skill
    return []


def deserialize_family(value: str) -> FamilyRelationship:
    return {
        FamilyRelationship.NONE.value: FamilyRelationship.NONE,
        FamilyRelationship.GRANDPARENT.value: FamilyRelationship.GRANDPARENT,
        FamilyRelationship.PARENT.value: FamilyRelationship.PARENT,
        FamilyRelationship.LEGAL_PARENT.value: FamilyRelationship.LEGAL_PARENT,
        FamilyRelationship.SIBLING.value: FamilyRelationship.SIBLING,
        FamilyRelationship.COUSIN.value: FamilyRelationship.COUSIN,
        FamilyRelationship.PARENT_SIBLING.value: FamilyRelationship.PARENT_SIBLING,
        FamilyRelationship.SIBLING_CHILDREN.value: FamilyRelationship.SIBLING_CHILDREN,
        FamilyRelationship.CHILDREN.value: FamilyRelationship.CHILDREN,
        FamilyRelationship.GRANDCHILDREN.value: FamilyRelationship.GRANDCHILDREN,
    }[value]
