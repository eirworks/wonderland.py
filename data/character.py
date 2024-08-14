import random
import uuid
from enum import Enum

from data.stats import Stats


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
    _orientation: Orientation
    _gender: Gender

    data = {}

    def __init__(self):
        self.age = 0
        self.char_id = uuid.uuid4()
        self.first_name = ""
        self.last_name = ""
        self.birth_month = 1
        self.traits = []
        self.stats = Stats()

        self._gender = Gender.MALE

        # asexual = 0, hetero = 1, homo = 2, bi = 3
        self._orientation = Orientation.HETEROSEXUAL

        self._money = 0

        self.alive = True
        self.died_at = (None, None)

        """
        Character marked as minor will disappear from character list
        randomly after certain years. Minor character can be persisted
        by befriend.
        """
        self.minor = False

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
        return "{} ({}/{}) - {}".format(self.full_name, self.age, self.gender[0], self.alive_summary())

    def adult(self, max_age: int = 30):
        self.age = random.randrange(20, max_age)

    def alive_summary(self) -> str:
        if self.alive:
            return "Alive"
        else:
            return "Died at {} {}".format(self.died_at[0], self.died_at[1])
