from contents.actions.cheats import action_add_money, action_cheat_adult, action_cheats
from contents.actions.greet import action_greet, action_stats
from contents.actions.main import action_age, action_time


def action_registry(debug: bool = False) -> dict:
    activities = {
        "greet": action_greet,
        "stats": action_stats,
        "age": action_age,
        "continue": action_age,
        "c": action_age,
        "time": action_time,
    }

    cheats = {
        "money:add": action_add_money,
        "adult": action_cheat_adult,
        "cheats": action_cheats,
    }

    if debug:
        print("Added cheat commands")
        activities.update(cheats)

    return activities
