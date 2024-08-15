import sys

from faker import Faker

from contents.action_registry import action_registry
from contents.event_registry import calculate_trigger_weight
from contents.events.birth import list_birth_events
from wonder.character.spawner import spawn_random_npc
from wonder.data.character import Character
from wonder.game import Game
from wonder.visual.character_frame import character_frame

debug = "debug" in sys.argv


print("WonderLife")
print("V1.0 {}".format("debug" if debug else ""))

fake = Faker()
print("What is your name?")
first_name = fake.first_name_male()
last_name = fake.last_name()
first_name = input("First name ({}):".format(first_name)) or first_name
last_name = input("Last name ({}):".format(last_name)) or last_name

# Create player's character
player = Character()
player.first_name = first_name
player.last_name = last_name

# Set up the game
game = Game()
game.player = player
game.debug = debug

# Display character info
character_frame(game)

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
