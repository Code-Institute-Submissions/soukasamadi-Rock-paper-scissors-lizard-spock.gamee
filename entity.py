from enum import Enum, auto


class Entity(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3
    SPOCK = 4
    LIZARD = 5

    def __str__(self) -> str:
        return self.value
