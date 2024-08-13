from math import floor
from random import randrange


class Stats:
    _cha: int
    _wis: int
    _int: int
    _dex: int
    _con: int
    _str: int

    def __init__(self):
        self._str = 0
        self._con = 0
        self._dex = 0
        self._int = 0
        self._wis = 0
        self._cha = 0

        self.roll()

    def roll(self):
        self._str = randrange(1, 18)
        self._con = randrange(1, 18)
        self._dex = randrange(1, 18)
        self._int = randrange(1, 18)
        self._wis = randrange(1, 18)
        self._cha = randrange(1, 18)

    def modifier(self, stat: str) -> int:
        match stat:
            case 'str':
                return floor((self._str - 10) / 2)
            case 'con':
                return floor((self._con - 10) / 2)
            case 'dex':
                return floor((self._dex - 10) / 2)
            case 'int':
                return floor((self._int - 10) / 2)
            case 'wis':
                return floor((self._wis - 10) / 2)
            case 'cha':
                return floor((self._cha - 10) / 2)

    def print_stats(self):
        print("Strength     : {} ({})".format(self._str, self.modifier('str')))
        print("Constitution : {} ({})".format(self._con, self.modifier('con')))
        print("Dexterity    : {} ({})".format(self._dex, self.modifier('dex')))
        print("Intelligence : {} ({})".format(self._int, self.modifier('int')))
        print("Wisdom       : {} ({})".format(self._wis, self.modifier('wis')))
        print("Charisma     : {} ({})".format(self._cha, self.modifier('cha')))
