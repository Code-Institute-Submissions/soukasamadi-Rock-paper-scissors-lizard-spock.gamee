import random
from rules import Rules
from entity import Entity
from collections import defaultdict
from typing import Dict
import gspread
from google.oauth2.service_account import Credentials
import datetime
import time
from colorama import Fore


# Import date from datetime
date = datetime.datetime.today()
today_date = date.strftime("%d/%m/%Y")


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('rock_paper_game')

gamesheet = SHEET.worksheet('gamesheet')

data = gamesheet.get_all_values()


class Game:
    def __init__(self, user, max_round: int = 5) -> None:
        self.scoreboard = Scoreboard()
        self.max_round = max_round
        self.user = user
        self.entities = Entity
        self.rules = Rules()
        self.computer = "computer"

        # register players names in scoreboard
        self.scoreboard.register_player(self.user)
        self.scoreboard.register_player(self.computer)

    def display_user_choices(self) -> None:
        print(Fore.WHITE + f"\nSelect a number[1-2-3-4-5]:\n ")
        print(" 1 : ROCK\n 2 : PAPER\n 3 : SCISSOR\n 4 : SPOCK\n 5 : LIZARD\n")

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
                    print(
                        Fore.RED +
                        '\nPlease select a valid choice[1-2-3-4-5]!\n')
                else:
                    return self.entities(choice)
            except ValueError:
                print(
                    Fore.RED +
                    '\nYou typed somthing different than a number.\n')

    def get_computer_input(self) -> Entity:
        """Choose a random entity for the computer
        """
        computer_choice = random.randint(1, len(self.entities))
        return self.entities(computer_choice)

    def display_both_entities(
            self,
            user_entity: Entity,
            computer_intity: Entity) -> None:
        """Displays current user entity VS computer entity
        """
        print(Fore.GREEN + '------------------------------------')
        print(Fore.GREEN + f"{self.user}({user_entity.name})  - VS -", end=" ")
        print(f" {self.computer}{computer_intity.name})")
        print(Fore.GREEN + '------------------------------------')

    def display_tie(self) -> None:
        print(f"Oops! It's a tie..")

    def display_entities_relation(self, message: str) -> None:
        """Display the relation between the entities
        """
        print(Fore.CYAN + f"      ({message})\n")

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
        self.display_game_winner()
        self.update_worksheet()

    def update_worksheet(self):
        # update worksheet
        print(Fore.YELLOW + '\nUpdating Worksheet ...\n')
        access_sheet = SHEET.worksheet("gamesheet")
        access_sheet.append_row([self.user,
                                 today_date,
                                 self.scoreboard.points[self.user],
                                 self.scoreboard.points[self.computer]])
        time.sleep(3)
        print(Fore.GREEN + 'Worksheet Update successful.\n')

    @staticmethod
    def get_user_name() -> str:
        """Get player name
        """
        return str(input().strip())

    def display_game_winner(self):
        user_point = self.scoreboard.points[self.user]
        computer_point = self.scoreboard.points[self.computer]
        if user_point > computer_point:
            print(Fore.GREEN + '  congratulation you are the Winner!\n')
        elif user_point < computer_point:
            print(Fore.RED + '  Oh oooh! Computer wins!')
        elif user_point == computer_point:
            print(Fore.YELLOW + '  There is No winner\n')

    def restart(self):
        while True:
            replay = input(
                Fore.WHITE +
                "Do you want to replay: Enter (Yes) OR (No):\n")
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

    def register_player(self, user_name: str):
        self.points[user_name] = 0

    def display_scores(self):
        print(Fore.MAGENTA + '\n\n***********Score*************')
        for user, score in self.points.items():
            print(f"{user} : {score}", end='\t')
        print(Fore.MAGENTA + '\n*****************************\n')
