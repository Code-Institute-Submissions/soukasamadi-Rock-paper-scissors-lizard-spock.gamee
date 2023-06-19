from game import *
from colorama import Fore
from extras import *


def main() -> None:
    """Main function to start the game
    """

    logo = [
        # Game logo
        """
        Welcome To :
              __            _        ___                            
             /__\ ___   ___| | __   / _ \__ _ _ __  _ __   ___ _ __ 
            / \/// _ \ / __| |/ /  / /_)/ _` | '_ \| '_ \ / _ \ '__|
           / _  \ (_) | (__|   <  / ___/ (_| | |_) | |_) |  __/ |   
           \/ \_/\___/ \___|_|\_\ \/    \__,_| .__/| .__/ \___|_|   
                                             |_|   |_|              
          __                                  __ _                  _ 
         / _\ ___ ___  ___ ___  ___  _ __    / /(_)______ _ _ __ __| |
         \ \ / __/ _ \/ __/ __|/ _ \| '__|  / / | |_  / _` | '__/ _` |
         _\ \ (_|  __/\__ \__ \ (_) | |    / /__| |/ / (_| | | | (_| |
         \__/\___\___||___/___/\___/|_|    \____/_/___\__,_|_|  \__,_|
                                                                      
                            __                  _    
                           / _\_ __   ___   ___| | __
                           \ \| '_ \ / _ \ / __| |/ /
                           _\ \ |_) | (_) | (__|   < 
                           \__/ .__/ \___/ \___|_|\_\
                              
                              |_|    
   
        """
    ]

    print(f"{Fore.BLUE}{logo[0]}")
    typewriter(f"""
    G O O D  L U C K ! ! 
    I  W I C H  Y O U  W I N  T H E  G A M E ! !
    P L E A S E  E N T E R  Y O U R  N A M E : \n""")

    user_name = Game.get_user_name()
    game = Game(user_name)

    print(Fore.YELLOW + '\n       ---Game Rules---\n')
    print(Fore.YELLOW + ' -Scissors decapitate Lizard.')
    print(Fore.YELLOW + ' -Scissors cuts paper.')
    print(Fore.YELLOW + ' -Paper covers rock.')
    print(Fore.YELLOW + ' -Rock crushes lizard.')
    print(Fore.YELLOW + ' -Lizard poisons Spock.')
    print(Fore.YELLOW + ' -Spock smashes scissors.')
    print(Fore.YELLOW + ' -Scissors decapitates lizard.')
    print(Fore.YELLOW + ' -Lizard eats paper.')
    print(Fore.YELLOW + ' -Paper disproves Spock.')
    print(Fore.YELLOW + ' -Spock vaporizes rock.')
    print(Fore.YELLOW + ' -Rock crushes scissors.')
    print(Fore.BLUE + '\n------You will play 5 Rounds------\n')
    print(Fore.WHITE + "Press [Enter] to start:")
    _ = input()
    game.play()
    print(Fore.YELLOW + '+++++++++++++The End++++++++++++\n')
    game.restart()


if __name__ == '__main__':
    main()
