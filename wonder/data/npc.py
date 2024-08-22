from enum import IntEnum, StrEnum

from data.character import Gender
from wonder.data.character import Character


class FamilyRelationship(StrEnum):
    GRANDPARENT = "grandparent"
    PARENT = "parent"
    LEGAL_PARENT = "legal_parent"
    SIBLING = "sibling"
    COUSIN = "cousin"
    PARENT_SIBLING = "parent_sibling"
    SIBLING_CHILDREN = "niece"
    CHILDREN = "children"
    GRANDCHILDREN = "grandchildren"
    NONE = ""


class Lover(IntEnum):
    NONE = 0
    LOVER = 1
    SPOUSE = 2
    FLING = 3
    EX_LOVER = 100
    EX_SPOUSE = 101

    @staticmethod
    def types() -> dict:
        return {
            Lover.NONE: "Stranger",
            Lover.LOVER: "Lover",
            Lover.SPOUSE: "Spouse",
            Lover.FLING: "Fling",
            Lover.EX_LOVER: "Ex-Lover",
            Lover.EX_SPOUSE: "Ex-Spouse",
        }


class NonPlayerCharacter(Character):
    in_laws: bool
    step_family: bool
    lover: Lover
    family: FamilyRelationship
    relationship: float

    def __init__(self):
        super().__init__()

        self.relationship = 0.0
        self.family = FamilyRelationship.NONE
        self.step_family = False
        self.in_laws = False
        self.lover = Lover.NONE

    def family_relationship_name(self) -> str:
        if self.family == FamilyRelationship.NONE:
            return ""
        match self.family:
            case FamilyRelationship.PARENT:
                return "Father" if self._gender == Gender.MALE else "Mother"
            case FamilyRelationship.LEGAL_PARENT:
                return "Legal Father" if self._gender == Gender.MALE else "Legal Mother"
            case FamilyRelationship.SIBLING:
                return "Brother" if self._gender == Gender.MALE else "Sister"
            case FamilyRelationship.COUSIN:
                return "Cousin"
            case FamilyRelationship.CHILDREN:
                return "Son" if self._gender == Gender.MALE else "Daughter"
            case FamilyRelationship.PARENT_SIBLING:
                return "Uncle" if self._gender == Gender.MALE else "Aunt"
            case FamilyRelationship.GRANDPARENT:
                return "Grandfather" if self._gender == Gender.MALE else "Grandmother"
            case FamilyRelationship.GRANDCHILDREN:
                return "Grandson" if self._gender == Gender.MALE else "Granddaughter"
            case FamilyRelationship.SIBLING_CHILDREN:
                return "Nephew" if self._gender == Gender.MALE else "Niece"
            case _:
                return self.family.value.capitalize() + "?"

    def lover_relationship_name(self) -> str:
        match self.lover:
            case Lover.NONE:
                return ""
            case Lover.EX_LOVER:
                return "Ex-Boyfriend" if self._gender == Gender.MALE else "Ex-Girlfriend"
            case Lover.LOVER:
                return "Boyfriend" if self._gender == Gender.MALE else "Girlfriend"
            case Lover.FLING:
                return "Sex Friend"
            case Lover.SPOUSE:
                return "Husband" if self._gender == Gender.MALE else "Wife"
            case Lover.SPOUSE:
                return "Ex-Husband" if self._gender == Gender.MALE else "Ex-Wife"

        return ""

