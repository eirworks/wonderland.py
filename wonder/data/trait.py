from wonder.string_helpers import to_snake_case


class Trait:
    def __init__(self, name: str, trait_id: str = None, reverse_id: str | None = None):
        self.name = name
        self.trait_id = trait_id

        if trait_id is None:
            self.trait_id = to_snake_case(self.name)

        self.reverse_trait_id = reverse_id

        if self.reverse_trait_id is not None:
            self.reverse_trait_id = to_snake_case(self.reverse_trait_id)
