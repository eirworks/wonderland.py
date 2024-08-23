import click

from game import Game
from persists.load_game import list_game_save_files, list_game_saves
from persists.save_game import save_game
from visual.time import month_name


def action_save(game: Game) -> Game:
    save_game(game)
    click.echo("Game saved successfully")
    return game


def action_load(game: Game) -> Game:
    games = list_game_saves()
    if len(games) == 0:
        print("No game saves")
    else:
        for game in games:
            print("- {} - {}/{}".format(game['_summary']['name'], month_name(game['_summary']['month']), game['_summary']['age']))

    return game
