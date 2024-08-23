import json
import os

from filesystem.game_path import game_save_dir


def list_game_save_files() -> list:
    results = []
    for root, dirs, files in os.walk(game_save_dir()):
        for file in files:
            if file.endswith(".json"):
                results.append(file)

    return results


def list_game_saves() -> list:
    """
    List game saves as ordered sets
    :return:
    """
    games = []

    for file in list_game_save_files():
        with open(os.path.join(game_save_dir(), file), 'r') as f:
            data = json.load(f)

            games.append(data)

    return sorted(games, key=lambda g: g['_timestamp'], reverse=True)
