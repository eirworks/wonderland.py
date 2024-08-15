from wonder.data.character import Gender
from wonder.data.npc import NonPlayerCharacter, FamilyRelationship
from wonder.game import Game


def find_by_id(game: Game, character_id: str) -> NonPlayerCharacter | None:
    filtered_characters = list(filter(lambda cha: cha.char_id == character_id, game.relationships))

    if len(filtered_characters) == 0:
        return None
    else:
        return filtered_characters[0]


def find_by_family(game: Game, family_type: FamilyRelationship, gender: Gender = Gender.MALE) -> NonPlayerCharacter | None:
    chars = list(filter(lambda cha: cha.family == family_type and cha._gender == gender, game.relationships))

    if len(chars) == 0:
        return None
    else:
        return chars[0]


def get_family_characters(game: Game) -> list:
    return list(filter(lambda cha: cha.family != FamilyRelationship.NONE, game.relationships))
