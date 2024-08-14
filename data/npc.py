from enum import Enum

from data.character import Character

class FamilyRelationship(Enum):
    GRANDPARENT = "grandparent"
    PARENT = "parent"
    FATHER = "father" #deprecated
    MOTHER = "mother" #deprecated
    SIBLING = "sibling"
    COUSIN = "cousin"
    PARENT_SIBLING = "parent_sibling"
    SIBLING_CHILDREN = "sibling"
    CHILDREN = "children"
    GRANDCHILDREN = "grandchildren"
    NONE = ""

    def relationship_name(self, relationship: 'FamilyRelationship', character: Character) -> str:
        if relationship == FamilyRelationship.PARENT and character.gender :
            return

class NonPlayerCharacter(Character):

    is_lover: bool
    family: FamilyRelationship
    relationship: float

    def __init__(self):
        super().__init__()

        self.relationship = 0.0
        self.family = FamilyRelationship.NONE
        self.is_lover = False


