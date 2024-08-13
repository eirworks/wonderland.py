import locale

from data.character import Character
from wonder.visual.time import month_name


def character_frame(character: Character, complete: bool = False):
    locale.setlocale(locale.LC_ALL, '')
    print("-"*10)
    print("{} {}".format(character.first_name, character.last_name))
    print("Age: {} Birth: {}".format(character.age, month_name(character.birth_month)))
    print("{} {}".format(character.gender, character.orientation))
    print("Cash: {}".format(locale.currency(character.money)))
    if complete:
        print("-" * 6)
        print("ID: {}".format(character.char_id))
        character.stats.print_stats()
    print("-" * 10)
