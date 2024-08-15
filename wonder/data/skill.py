import uuid
from enum import Enum
from uuid import UUID

from wonder.data.stats import Stat


class SkillTarget(Enum):
    SELF = 0
    ANY = 1
    OTHER = 2
    FAMILY = 3
    LOVER = 4
    FRIEND = 5


class Skill:
    base_exp: int
    skill_id: str | None | UUID
    name: str
    target: SkillTarget
    affect_stat: Stat

    def __init__(self, name: str, skill_id: str = None):
        self.affect_stat = Stat.STR
        self.name = name
        self.skill_id = skill_id or uuid.uuid4()
        self.target = SkillTarget.OTHER
        self.base_exp = 100
