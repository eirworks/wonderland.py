import sys

from contents.action_registry import action_registry
from contents.event_registry import calculate_trigger_weight
from contents.events.birth import list_birth_events
from prompts.main_menu import main_menu
from wonder.character.spawner import spawn_random_npc
from wonder.visual.character_frame import character_frame

debug = "debug" in sys.argv

game = main_menu()

# Display character info
character_frame(game, game.player)

if not game.data["loaded"]:
    # trigger birth event
    calculate_trigger_weight(game, list_birth_events())(game)

# get all commands
actions = action_registry(game.debug)

# populate the world with random characters
game = spawn_random_npc(game, 10)

# main loop
while True:

    action = input("> ") or ""

    if action in ["quit", "q", "qqq", "exit"]:
        print("Bye, thank you for playing")
        sys.exit(0)
    elif action == "":
        print("Type 'help' for some guidance.")
    elif action in actions:
        game = actions[action](game) or game
    elif action == "test":
        if game.debug:
            print("Nothing to test")
    else:
        print("Unknown command '{}', type 'help' for more info.".format(action))
