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



    def Display_user_choices(self) -> None:
       
        choices_text = "\n ".join(f"{entity.value} : {entity.name}" for entity  in self.entities)
        print(f"Select a number[1-2-3-4-5]:\n {choices_text}:", end='\t')    