import random

from data.trait import Trait


def traits_registry() -> list:
    return [
        Trait("Honest", reverse_id="Liar"),
        Trait("Liar", reverse_id="Honest"),
        Trait("Humble", reverse_id="Arrogant"),
        Trait("Arrogant", reverse_id="Humble"),
        Trait("Chaste", reverse_id="Horny"),
        Trait("Horny", reverse_id="Chaste"),
        Trait("Patient", reverse_id="Angry"),
        Trait("Angry", reverse_id="Patient"),
        Trait("Courage", reverse_id="Coward"),
        Trait("Coward", reverse_id="Courage"),
        Trait("Giver", reverse_id="Greedy"),
        Trait("Greedy", reverse_id="Giver"),
        Trait("Extrovert", reverse_id="Introvert"),
        Trait("Introvert", reverse_id="Extrovert"),
        Trait("Abstinence", reverse_id="Glutton"),
        Trait("Glutton", reverse_id="Abstinence"),
        Trait("Kind", reverse_id="Evil"),
        Trait("Evil", reverse_id="Kind"),
        Trait("Stupid", reverse_id="Smart"),
        Trait("Smart", reverse_id="Stupid"),
        Trait("Ugly", reverse_id="Beautiful"),
        # Trait("Coming Out"),
        # Trait("Transitioning"),
    ]


def random_traits(number: int = 1) -> list:
    traits = list()
    ids = list()
    reversed_ids = list()

    count = 0
    all_traits = traits_registry()
    random.shuffle(all_traits)
    for trait in all_traits:
        combined = ids + reversed_ids
        print(combined)
        if trait.trait_id not in combined:
            traits.append(trait)
            ids.append(trait.trait_id)
            if trait.reverse_trait_id is not None:
                reversed_ids.append(trait.reverse_trait_id)
            count += 1

        if count == number:
            break
    return traits


def random_trait() -> Trait:
    return random.choice(traits_registry())
