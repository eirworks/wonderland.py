from wonder.character.spawner import spawn_friend, spawn_lover
from wonder.game import Game


def action_cheats(game: Game) -> Game:
    cheats = [
        "Add money +1000",
        "Add money +10000",
        "Add money +1000000",
        "Instant adult",
        "Back to baby",
        "Go to high school",
        "Summon a friend",
        "Summon a lover",
    ]

    from wonder.prompts.ask import ask_options
    cheat = ask_options("Which cheat you want to use?", cheats, allow_quit=True)

    match cheat:
        case 1:
            game.player.money = game.player.money + 1000
        case 2:
            game.player.money = game.player.money + 10000
        case 3:
            game.player.money = game.player.money + 100000
        case 4:
            game.player.age = 18
        case 5:
            game.player.age = 0
        case 6:
            game.player.age = 15
        case 7:
            game.relationships.append(spawn_friend(game.player))
        case 8:
            game.relationships.append(spawn_lover(game.player))
    if cheat > 0:
        print("Cheat Activated! ({})".format(cheat))
    else:
        print("No cheat activated")
    return game
