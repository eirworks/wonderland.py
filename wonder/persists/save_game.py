import json
import os.path
import sys

import click

from filesystem.game_path import game_dir, game_save_dir
from game import Game


def save_game(game: Game):
    prepare_save_dir()
    with open(save_path(game.player.char_id + ".json"), 'w') as file:
        json.dump(game.to_json(), file)


def prepare_save_dir():
    if not os.path.exists(save_path()):
        os.makedirs(save_path())
        if "debug" in sys.argv:
            click.echo("Save dir created")


def save_path(filename: str = "") -> str:
    return os.path.join(game_save_dir(), filename)
