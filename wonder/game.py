from data.character import Character


class Game:
    _player: Character

    data = {}

    def __init__(self):
        self.month = 1
        self._city = None
        self._player = Character()
        self.debug = False

        """
        Relationship format:
        Tuple with order: (character, relationship_value, family type, is lover).
        Example: (father, 1, 'father', False)
        Example: (girlfriend, 0.88, None, True)
        """
        self.relationships = []

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, character: Character):
        self._player = character
