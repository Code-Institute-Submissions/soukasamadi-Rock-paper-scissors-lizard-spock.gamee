from entity import Entity
from typing import Tuple

class Rules:
    """Game Rules
    """
    rules = {
            (Entity.PAPER, Entity.ROCK): {
                'winner': Entity.PAPER,
                'message': 'Paper covers Rock'
            },
            (Entity.PAPER, Entity.SPOCK): {
                'winner': Entity.PAPER,
                'message': 'Paper disapproves Spock'
            },
            (Entity.ROCK, Entity.LIZARD): {
                'winner': Entity.ROCK,
                'message': 'Rock crushes Lizard'
            },
            (Entity.ROCK, Entity.SCISSOR): {
                'winner': Entity.ROCK,
                'message': 'Rock crushes Scissor'
            },
            (Entity.SCISSOR, Entity.PAPER): {
                'winner':  Entity.SCISSOR,
                'message': 'Scissor cuts Paper'
            },
            (Entity.SCISSOR, Entity.LIZARD): {
                'winner': Entity.SCISSOR,
                'message': 'Scissor decapitates Lizard'
            },
            (Entity.SPOCK, Entity.SCISSOR): {
                'winner': Entity.SPOCK,
                'message': 'Spock smashes Scissor'
            },
            (Entity.SPOCK, Entity.ROCK): {
                'winner': Entity.SPOCK,
                'message': 'Spock vaporizes Rock'
            },
            (Entity.LIZARD, Entity.SPOCK): {
                'winner': Entity.LIZARD,
                'message': 'Lizard poisons Spock'
            },
            (Entity.LIZARD, Entity.PAPER): {
                'winner': Entity.PAPER,
                'message': 'Lizard eats Paper'
            },
            
        }git