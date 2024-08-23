import click

from game import Game
from persists.save_game import save_game
from prompts.main_menu import load_game_menu
from visual.character_frame import character_frame


def action_save(game: Game) -> Game:
    save_game(game)
    click.echo("Game saved successfully")
    return game


def action_load(game: Game) -> Game:
    loaded_game = load_game_menu()
    if loaded_game is not None:
        game = loaded_game
        character_frame(game, game.player)

    return game
