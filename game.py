import random
from rules import Rules
from entity import Entity
from collections import defaultdict
from typing import Dict

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


    def get_user_input(self) -> Entity:
        """Takes user inputs and selects the entities then returns Entity selected by user
        """
        available_choices = [entity.value for entity in self.entities]
        while True:
            try:
                self.Display_user_choices()
                choice = int(input())
                
                if choice not in available_choices:
                    print("Please select a valid choice[1-2-3-4-5]!")
                else:
                    return self.entities(choice)    
            except ValueError:
                print("You typed somthing different than a number.")
            

    def get_computer_input(self) -> Entity:
        """Choose a random entity for the computer
        """
        computer_choice = random.randint(1, len(self.entities))
        return self.entities(computer_choice)        


    def display_both_entities(self, user_entity: Entity, computer_intity: Entity) -> None:
        """Displays current user entity VS computer entity
        """
        print("------------------------------------")
        print(f"{self.user} ({user_entity.name}) - VS - {self.computer} ({computer_intity.name})")
        print("------------------------------------")    


    def display_tie(self) -> None:
        print(f"Oops! It's a tie..")    


    def display_entities_relation(self, message: str) -> None:
        """Display the relation between the entities 
        """
        print(f"   ({message})\n")    