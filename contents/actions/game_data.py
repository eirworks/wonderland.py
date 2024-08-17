import click

from game import Game
from persists.save_game import save_game


def action_save(game: Game) -> Game:
    save_game(game)
    click.echo("Game saved successfully")
    return game
