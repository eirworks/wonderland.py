import random
import sys
import uuid
from enum import Enum
from uuid import UUID

from contents.traits.common_traits import random_traits
from wonder.data.skill import Skill
from wonder.data.stats import Stats
from wonder.data.trait import Trait


class Gender(Enum):
    MALE = 1
    FEMALE = 0


class Orientation(Enum):
    ASEXUAL = 0
    HETEROSEXUAL = 1
    HOMOSEXUAL = 2
    BISEXUAL = 3

    @staticmethod
    def orientations():
        return {
            Orientation.ASEXUAL: "Asexual",
            Orientation.HETEROSEXUAL: "Heterosexual",
            Orientation.HOMOSEXUAL: "Homosexual",
            Orientation.BISEXUAL: "Bisexual",
        }


class Character:
    char_id: UUID
    _orientation: Orientation
    _gender: Gender
    skills: set

    data = {}

    def __init__(self):
        self.age = 0
        self.char_id = uuid.uuid4()
        self.first_name = ""
        self.last_name = ""
        self.birth_month = 1
        self.traits = []
        self.skills = set()
        self.stats = Stats()

        self._gender = Gender.MALE
        self._orientation = Orientation.HETEROSEXUAL

        self.exp = 0
        self.base_exp = 10
        self._money = 0

        self.alive = True
        self.died_at = (None, None)

        """
        Character marked as minor will disappear from character list
        randomly after certain years. Minor character can be persisted
        by befriend.
        """
        self.minor = False

        self.set_up_traits()

    @property
    def gender(self):
        return "Male" if self._gender == Gender.MALE else "Female"

    @gender.setter
    def gender(self, value):
        self._gender = value

    @property
    def orientation(self) -> str:
        return Orientation.orientations()[self._orientation] or "?"

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, money: int | float):
        self._money = money

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def name_summary(self):
        return "{}{} ({}/{})".format(self.full_name, self.dead_or_alive_symbol(), self.age, self.gender[0])

    def adult(self, max_age: int = 30):
        self.age = random.randrange(20, max_age)

    def alive_summary(self) -> str:
        if self.alive:
            return "Alive"
        else:
            return "Died at {} {}".format(self.died_at[0], self.died_at[1])

    def dead_or_alive_symbol(self) -> str:
        if self.alive:
            return ""
        else:
            return "†"

    def add_skill(self, skill: Skill):
        self.skills.add(skill)

    def add_trait(self, trait: Trait) -> bool:
        """
        Add a trait, if already exists it will not add anything
        And if reversed trait exists, it will be replaced.
        :param trait:
        :return:
        """

        if self.has_trait(trait.trait_id):
            return False

        if self.has_reverse_trait(trait):
            # remove existing reversed trait
            self.remove_trait(trait.reverse_trait_id)

        self.traits.append(trait)

        return True

    def has_trait(self, trait_id: str) -> bool:
        return len(list(filter(lambda trait: trait.trait_id == trait_id, self.traits))) > 0

    def has_reverse_trait(self, trait: Trait) -> bool:
        return len(list(filter(lambda t: t.trait_id == trait.reverse_trait_id, self.traits))) > 0

    def remove_trait(self, trait_id: str):
        self.traits[:] = [trait for trait in self.traits if trait.trait_id != trait_id]
        if "debug" in sys.argv:
            print(self.traits)

    def set_up_traits(self, num: int = 3):
        self.traits = set(random_traits(num))



