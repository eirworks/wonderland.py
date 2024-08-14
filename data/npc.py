from enum import Enum

from data.character import Character

class FamilyRelationship(Enum):
    FATHER = "father"
    MOTHER = "mother"
    SIBLING = "sibling"
    NONE = ""

class NonPlayerCharacter(Character):

    is_lover: bool
    family: FamilyRelationship
    relationship: float

    def __init__(self):
        super().__init__()

        self.relationship = 0.0
        self.family = FamilyRelationship.NONE
        self.is_lover = False
