import sys
import time


def typewriter(string):
    """source code
        [PedroCristo](https://github.com/PedroCristo/portfolio_project_3/blob/main/hangman_extras.py)
        """
    for i in string:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
