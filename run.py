import simple_colors  
from game import *


def main() -> None:
    """Main function to start the game
    """
    user_name = Game.get_user_name()
    game = Game(user_name)
    print(simple_colors.green('  --- Welcome To Rock paper scissor spock and lizard game! ---\n','bold'))  
    print(simple_colors.yellow('       Game Rules:\n'))
    print(simple_colors.yellow(' -Scissors decapitate Lizard.\n -Scissors cuts paper.\n -Paper covers rock.\n -Rock crushes lizard.\n -Lizard poisons Spock.\n -Spock smashes scissors.\n -Scissors decapitates lizard.\n -Lizard eats paper.\n -Paper disproves Spock.\n -Spock vaporizes rock.\n -Rock crushes scissors.\n'))
    print(simple_colors.blue('------You will play 5 Rounds------\n'))
    print("Press [Enter] to start:")
    _ = input()
    game.play()
    game.display_game_winner()
    game.update_worksheet()
    print(simple_colors.yellow('+++++++++++++The End++++++++++++\n'))
    game.restart()

if __name__ == '__main__':
    main()