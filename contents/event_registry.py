import random

from contents.events.baby import event_baby_fun_play, event_baby_fun_eats
from wonder.game import Game


def event_registry() -> list:
    return [
        (event_baby_fun_eats, 4),
        (event_baby_fun_play, 1),
    ]


def execute_event_weights(game: Game, events: list):
    total = sum(weight for _, weight in events)
    print("Total weights = {}".format(total)) if game.debug else None
    r = random.uniform(0, total)
    print("Chance: r = {}".format(r)) if game.debug else None
    up_to = 0
    for event, weight in events:
        if up_to + weight >= r:
            return event
        up_to += weight
    assert False, "Why are you here?"


def trigger_event(game: Game) -> Game:
    return execute_event_weights(game, event_registry())(game)
