from game import *
from colorama import Fore


def main() -> None:
    """Main function to start the game
    """

    logo = [
        # Game logo
        """
    Welcome To :

    ______                 ______
    | ___ \\         | |    | ___ \
    | |_/ /___   ___| | __ | |_/ /_ _ _ __   ___ _ __
    |    // _ \\ / __| |/ / |  __/ _` | '_ \\ / _ \\ '__|
    | |\\ \\ (_) | (__|   <  | | | (_| | |_) |  __/ |
    \\_| \\_\\___/ \\___|_|\\_\\ \\_|  \\__,_| .__/ \\___|_|
    _____ _                        | |
    /  ___(_)                       |_|
    \\ `--. _ ___ ___  ___  _ __ ___
    `--. \\ / __/ __|/ _ \\| '__/ __|
    /\\__/ / \\__ \\__ \\ (_) | |  \\__ \
    \\____/|_|___/___/\\___/|_|  |___/
    _     _                  _   _____                  _
    | |   (_)                | | /  ___|                | |
    | |    _ ______ _ _ __ __| | \\ `--. _ __   ___   ___| | __
    | |   | |_  / _` | '__/ _` |  `--. \\ '_ \\ / _ \\ / __| |/ /
    | |___| |/ / (_| | | | (_| | /\\__/ / |_) | (_) | (__|   <
    \\_____/_/___\\__,_|_|  \\__,_| \\____/| .__/ \\___/ \\___|_|\\_\

                                    |_|
    """
    ]

    print(f"{Fore.BLUE}{logo[0]}")

    user_name = Game.get_user_name()
    game = Game(user_name)

    print(Fore.YELLOW + '\n       ---Game Rules---\n')
    print(Fore.YELLOW + ' -Scissors decapitate Lizard.\n')
    print(Fore.YELLOW + ' -Scissors cuts paper.\n')
    print(Fore.YELLOW + ' -Paper covers rock.\n')
    print(Fore.YELLOW + ' -Rock crushes lizard.\n')
    print(Fore.YELLOW + ' -Lizard poisons Spock.\n')
    print(Fore.YELLOW + ' -Spock smashes scissors.\n')
    print(Fore.YELLOW + ' -Scissors decapitates lizard.\n')
    print(Fore.YELLOW + ' -Lizard eats paper.\n')
    print(Fore.YELLOW + ' -Paper disproves Spock.\n')
    print(Fore.YELLOW + ' -Spock vaporizes rock.\n')
    print(Fore.YELLOW + ' -Rock crushes scissors.\n')
    print(Fore.BLUE + '------You will play 5 Rounds------\n')
    print(Fore.WHITE + "Press [Enter] to start:")
    _ = input()
    game.play()
    print(Fore.YELLOW + '+++++++++++++The End++++++++++++\n')
    game.restart()


if __name__ == '__main__':
    main()
