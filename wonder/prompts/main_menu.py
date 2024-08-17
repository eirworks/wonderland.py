import sys

import click
from faker import Faker

from data.character import Character, Gender
from game import Game
from prompts.ask import ask_options


def main_menu() -> Game:
    debug = "debug" in sys.argv

    click.secho("WonderLife")
    click.echo("V1.0 {}".format("debug" if debug else ""))

    while True:
        click.echo("++++++++++++++++++")
        click.echo("[c] Continue")
        click.echo("[n] New Game")
        click.echo("[q] Quit")
        menu = click.prompt(">", prompt_suffix="")

        if menu == "n":
            game = new_game()
            break
        elif menu == "q":
            click.echo("Bye, play again soon!")
            sys.exit(0)
        else:
            click.secho("Feature not available", fg='red')

    return game


def new_game() -> Game:
    debug = "debug" in sys.argv

    gender_answer = ask_options("Select Gender:", [
        "Male",
        "Female",
    ])

    gender = Gender.MALE
    if gender_answer == 2:
        gender = Gender.FEMALE

    fake = Faker()

    print("What is your name?")
    if gender == Gender.FEMALE:
        first_name = fake.first_name_female()
    else:
        first_name = fake.first_name_male()

    last_name = fake.last_name()

    first_name = input("First name ({}):".format(first_name)) or first_name
    last_name = input("Last name ({}):".format(last_name)) or last_name

    # Create player's character
    player = Character()
    player.first_name = first_name
    player.last_name = last_name
    player.gender = gender

    # Set up the game
    game = Game()
    game.player = player
    game.debug = debug

    return game
