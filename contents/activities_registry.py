from data.activity import ActivityCategory


def activities_registry() -> list:
    return [
        ActivityCategory("Friends", []),
        ActivityCategory("Romance", []),
        ActivityCategory("Entertainment", []),
        ActivityCategory("Health", []),
        ActivityCategory("Personal", []),
        ActivityCategory("Education", []),
    ]
