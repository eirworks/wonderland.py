from contents.actions.activities import action_activity
from contents.actions.cheats import action_cheats
from contents.actions.character_info import action_greet, action_stats, action_stats_all, action_traits
from contents.actions.ageing import action_age, action_time, action_age_fast_forward, action_age_by_year
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
        "cy": action_age_by_year,
        "ff": action_age_fast_forward,
        "time": action_time,
        "family": action_family,
        "characters": action_characters,
        "chars": action_characters,
        "cs": action_characters,
        "activity": action_activity,
        "a": action_activity,
        "traits": action_traits,
    }

    cheats = {
        "cheats": action_cheats,
    }

    if debug:
        print("DEBUG: Added cheat commands")
        activities.update(cheats)

    return activities
