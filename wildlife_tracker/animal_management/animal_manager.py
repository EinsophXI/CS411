from typing import Optional

from wildlife_tracker.animal_management.animal import Animal

class AnimalManager:

    def __init__(self) -> None:
        self.animals: dict[int, Animal] = {}

    def get_animal_by_id(self, animal_id: int) -> Optional[Animal]:
        pass

    def register_animal(self, animal_id: int, species: str, age: Optional[int] = None, health_status: Optional[str] = None) -> None:
        pass

    def remove_animal(self, animal_id: int) -> None:
        pass