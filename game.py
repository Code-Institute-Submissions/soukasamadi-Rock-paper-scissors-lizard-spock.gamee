from rules import Rules
from entity import Entity


class Game:
   
    def __init__(self, user: str, max_round: int = 5) -> None:
         
        self.scoreboard = Scoreboard()
        self.max_round = max_round
        self.user: str = user
        self.entities = Entity
        self.rules = Rules()
        self.computer: str = "computer"

        