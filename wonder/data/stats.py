from enum import Enum
from math import floor
from random import randrange


class Stat(Enum):
    CHA = "cha"
    WIS = "wis"
    STR = "str"
    DEX = "dex"
    CON = "con"
    INT = "int"


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

    def modifier(self, stat: Stat) -> int:
        match stat:
            case Stat.STR:
                return floor((self._str - 10) / 2)
            case Stat.CON:
                return floor((self._con - 10) / 2)
            case Stat.DEX:
                return floor((self._dex - 10) / 2)
            case Stat.INT:
                return floor((self._int - 10) / 2)
            case Stat.WIS:
                return floor((self._wis - 10) / 2)
            case Stat.CHA:
                return floor((self._cha - 10) / 2)

    def print_stats(self):
        print("Strength     : {}    ({})".format(self._str, self.modifier(Stat.STR)))
        print("Constitution : {}    ({})".format(self._con, self.modifier(Stat.CON)))
        print("Dexterity    : {}    ({})".format(self._dex, self.modifier(Stat.DEX)))
        print("Intelligence : {}    ({})".format(self._int, self.modifier(Stat.INT)))
        print("Wisdom       : {}    ({})".format(self._wis, self.modifier(Stat.WIS)))
        print("Charisma     : {}    ({})".format(self._cha, self.modifier(Stat.CHA)))

    def to_json(self):
        return {
            "str": self._str,
            "con": self._con,
            "dex": self._dex,
            "int": self._int,
            "wis": self._wis,
            "cha": self._cha,
        }

    def from_json(self, value: dict):
        self._str = value['str']
        self._con = value['con']
        self._dex = value['dex']
        self._int = value['int']
        self._wis = value['wis']
        self._cha = value['cha']
