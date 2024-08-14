from data.npc import NonPlayerCharacter, FamilyRelationship
from wonder.game import Game


def search_by_id(game: Game, character_id: str) -> NonPlayerCharacter | None:
    filtered_characters = list(filter(lambda cha: cha.char_id == character_id, game.relationships))

    if len(filtered_characters) == 0:
        return None
    else:
        return filtered_characters[0]


def search_by_family(game: Game, family_type: FamilyRelationship) -> NonPlayerCharacter | None:
    filtered_characters = list(filter(lambda cha: cha.family == family_type, game.relationships))

    if len(filtered_characters) == 0:
        return None
    else:
        return filtered_characters[0]
