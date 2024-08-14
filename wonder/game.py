import locale

import click

from data.character import Character
from data.npc import NonPlayerCharacter, FamilyRelationship


class Game:
    _player: Character

    data = {}

    def __init__(self):
        self.month = 1
        self._city = None
        self._player = Character()
        self.debug = False

        """
        Relationships contains NonPlayerCharacter objects
        """
        self.relationships = []

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, character: Character):
        self._player = character

    def give_money(self, amount: float):
        self.player.money += amount
        click.secho("-> You get {} <-".format(locale.currency(amount)), bg='green')
