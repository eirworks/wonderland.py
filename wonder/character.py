import random

from faker import Faker

from wonder.data.character import Gender, Orientation, Character
from wonder.data.npc import NonPlayerCharacter, FamilyRelationship, Lover


def spawn_npc(gender: Gender = Gender.MALE, min_age: int = 20, max_age: int = 60) -> NonPlayerCharacter:
    fake = Faker()
    char = NonPlayerCharacter()

    if gender == Gender.MALE:
        char.first_name = fake.first_name_male()
    else:
        char.first_name = fake.first_name_female()

    char.gender = gender
    char.last_name = fake.last_name()
    char.age = random.randrange(min_age, max_age)
    if char.age < 0:
        char.age = 0

    char.birth_month = random.randrange(1, 12)
    char._orientation = Orientation.HETEROSEXUAL

    return char


def spawn_family(
        gender: Gender = Gender.MALE,
        min_age: int = 20,
        max_age: int = 60,
        family_type: FamilyRelationship = FamilyRelationship.NONE) -> NonPlayerCharacter:
    char = spawn_npc(gender, min_age, max_age)
    char.family = family_type
    return char


def spawn_friend(player: Character) -> NonPlayerCharacter:
    char = spawn_npc(player.gender, player.age, player.age+3)
    char.relationship = 1
    return char


def spawn_lover(player: Character, lover_type: Lover = Lover.LOVER) -> NonPlayerCharacter:
    lover_gender = Gender.FEMALE
    if player.gender == Gender.FEMALE:
        lover_gender = Gender.MALE
    char = spawn_npc(lover_gender, player.age - 3, player.age + 3)
    char.relationship = random.randrange(1, 100) / 100
    char.lover = lover_type
    return char
