from contents.actions.cheats import action_cheats
from contents.actions.character_info import action_greet, action_stats, action_stats_all
from contents.actions.main import action_age, action_time
from contents.actions.relationships import action_family, action_characters
from contents.help import action_help


def action_registry(debug: bool = False) -> dict:
    activities = {
        "greet": action_greet,
        "help": action_help,
        "stats": action_stats,
        "stats:all": action_stats_all,
        "age": action_age,
        "continue": action_age,
        "c": action_age,
        "time": action_time,
        "family": action_family,
        "characters": action_characters,
    }

    cheats = {
        "cheats": action_cheats,
    }

    if debug:
        print("Added cheat commands")
        activities.update(cheats)

    return activities
