import json
import os.path
import sys

import click

from game import Game


def save_game(game: Game):
    prepare_save_dir()
    with open(base_save_dir(game.player.char_id + ".json"), 'w') as file:
        json.dump(game.to_json(), file)


def prepare_save_dir():
    if not os.path.exists(base_save_dir()):
        os.makedirs(base_save_dir())
        if "debug" in sys.argv:
            click.echo("Save dir created")


def base_save_dir(filename: str = "") -> str:
    return os.path.join(os.path.expanduser("~"), "wonderfile", filename)
