import uuid

from data.stats import Stats


class Character:
    _orientation: int
    _gender: int

    data = {}

    def __init__(self):
        self.age = 0
        self.char_id = uuid.uuid4()
        self.first_name = ""
        self.last_name = ""
        self.birth_month = 1
        self.traits = []
        self.stats = Stats()

        # male = 1, female = 0
        self._gender = 1

        # asexual = 0, hetero = 1, homo = 2, bi = 3
        self._orientation = 1

        self._money = 0

    @property
    def gender(self):
        return "Male" if self._gender == 1 else "Female"

    @property
    def orientation(self):
        orientations = {
            0: "Asexual",
            1: "Heterosexual",
            2: "Homosexual",
            3: "Bisexual",
        }

        return orientations[self._orientation]

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, money: int | float):
        self._money = money
