from enum import Enum

from data.character import Character


class FamilyRelationship(Enum):
    GRANDPARENT = "grandparent"
    PARENT = "parent"
    FATHER = "father"  #deprecated
    MOTHER = "mother"  #deprecated
    SIBLING = "sibling"
    COUSIN = "cousin"
    PARENT_SIBLING = "parent_sibling"
    SIBLING_CHILDREN = "sibling"
    CHILDREN = "children"
    GRANDCHILDREN = "grandchildren"
    NONE = ""


class Lover(Enum):
    NONE = 0
    LOVER = 1
    SPOUSE = 2
    EX_LOVER = 100
    EX_SPOUSE = 101

    @staticmethod
    def types() -> dict:
        return {
            Lover.NONE: "Stranger",
            Lover.LOVER: "Lover",
            Lover.SPOUSE: "Spouse",
            Lover.EX_LOVER: "Ex-Lover",
            Lover.EX_SPOUSE: "Ex-Spouse",
        }


class NonPlayerCharacter(Character):
    lover: Lover
    family: FamilyRelationship
    relationship: float

    def __init__(self):
        super().__init__()

        self.relationship = 0.0
        self.family = FamilyRelationship.NONE
        self.lover = Lover.NONE
