import sys
import time


def typewriter(string):
        """
        Typewriter for the main sentence at the beginning of the game
        The Python code for the typewriter was taken from this Source:
        [PedroCristo](https://github.com/PedroCristo/portfolio_project_3/blob/main/hangman_extras.py)
        """
        for i in string:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05)