import locale

import click

from wonder.data.character import Character, Gender


class Game:
    perform: float
    _player: Character

    """
    Data is a global variables used to store variable that affect
    the gameplay. It could only store integer.
    This has similar concept to RPG Maker's `Variable`.
    """
    data: dict[str, int] = {}

    def __init__(self):
        self.month = 1
        self._city = None
        self._player = Character()
        self.debug = False

        self.last_id = 0

        """
        Relationships contains NonPlayerCharacter objects
        """
        self.relationships = []

        """
        Perform used in school or work. Greater the perform
        greater the grades and salary bonus.
        It reset on new school year and when player changed job.
        Initial value depends on player's stat modifier depend on the
        type/job, eg School uses INT and job as miner uses STR.
        It can increase with
        """
        self.perform = 0.0

    def to_json(self) -> dict:
        return {
            "month": self.month,
            "player": self._player.to_json(),
            "relationships": [character.to_json() for character in self.relationships],
            "perform": self.perform,
            "last_id": self.last_id,
        }

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, character: Character):
        self._player = character

    def give_money(self, amount: float):
        self.player.money += amount
        click.secho("-> You get {} <-".format(locale.currency(amount)), bg='green')
