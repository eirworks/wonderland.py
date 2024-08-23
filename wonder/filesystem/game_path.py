import os.path


def game_dir() -> str:
    return os.path.join(os.path.expanduser("~"), "wonderfile")


def game_save_dir() -> str:
    return os.path.join(game_dir(), "saves")
