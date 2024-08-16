from typing import Callable

from wonder.string_helpers import to_snake_case


class ActivityCategory:
    def __init__(self, name: str, activities: list):
        self.name = name
        self.activities = activities
        self.category_id = to_snake_case(self.name)


class Activity:
    def __init__(self, name: str, activity: Callable):
        self.name = name
        self.activity = activity
        self.activity_id = to_snake_case(self.name)
