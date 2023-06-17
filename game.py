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

        # register players names in scoreboard 
        self.scoreboard.register_player(self.user)
        self.scoreboard.register_player(self.computer)


    def display_user_choices(self) -> None:
        choices_text = "\n ".join(f"{entity.value} : {entity.name}" for entity  in self.entities)
        print(f"Select a number[1-2-3-4-5]:\n {choices_text}:" , end = '\t')    


    def get_user_input(self) -> Entity:
        """Takes user inputs and selects the entities 
        then returns Entity selected by user
        """
        available_choices = [entity.value for entity in self.entities]
        while True:
            try:
                self.display_user_choices()
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


    def do_round(self) -> None:
        """Function to continue the rounds
        """
        user_entity = self.get_user_input()
        computer_intity = self.get_computer_input()
        self.display_both_entities(user_entity, computer_intity)
        if computer_intity == user_entity:
            self.display_tie()
            return

        winner, message = self.rules.get_winner(user_entity, computer_intity)
        if winner == user_entity:
            self.display_entities_relation(message)
            self.scoreboard.points[self.user] += 1
        else:
            self.display_entities_relation(message)
            self.scoreboard.points[self.computer] += 1


    def play(self):
        """Loop until all rounds are done
        """
        for i in range(self.max_round):
            self.do_round()
            self.scoreboard.display_scores()        



    @staticmethod
    def get_user_name() -> str:
        """Get player name
        """
        print("Please enter your name:", end = '\t')
        return str(input().strip())



    def display_game_winner(self):
        if self.scoreboard.points[self.user] > self.scoreboard.points[self.computer]:
            print("  congratulation you are the Winner!\n")
        elif self.scoreboard.points[self.user] < self.scoreboard.points[self.computer]: 
            print("  Oh oooh! Computer wins!")
        else:
            print("  there is No winner\n")   


    def restart(self):
        while True:
            replay = input("Do you want to replay: Enter (Yes) OR (No):\n")
            if replay == "Yes":
                self.scoreboard.points[self.user] = 0
                self.scoreboard.points[self.computer] = 0
                self.play()
            elif replay == "No":
                break                   


class Scoreboard:
    """Show Scores
    """
    def __init__(self) -> None:
        self.points: Dict[str, int] = defaultdict(int)

  
    def register_player(self, user_name:str):
        self.points[user_name] = 0   


    def display_scores(self):
        print("\n      **Score**")
        print("****************************")
        for user, score in self.points.items():
            print(f"{user} : {score}", end='\t')
        print("\n*****************************\n")        
