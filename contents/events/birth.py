"""
Birth events are special events that triggered when character created.
It introduces parents and siblings of player's character.
"""
from wonder.game import Game


def list_birth_events() -> list:
    return [
        (event_birth_good, 3),
        (event_birth_bad, 0.1),
    ]


def event_birth_good(game: Game) -> Game:
    print("You were born healthy!")
    return game


def event_birth_bad(game: Game) -> Game:
    print("You were born with severe disfunctional limbs!")
    return game
