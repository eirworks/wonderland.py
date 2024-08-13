from wonder.game import Game


def action_help(game: Game) -> Game:
    print("-- HELP --")
    print("Type `c` to continue ageing. Your age will forward 1 month.")
    print("There might be event during ageing.")
    print("Type a command to do activities. List all commands by `list`.")
    print("To quit the game, type `quit` or `exit`.")
    return game
