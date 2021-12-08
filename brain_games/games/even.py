import random


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


MIN_RAND = -30
MAX_RAND = 20


def run():
    num = random.randint(MIN_RAND, MAX_RAND)
    correct_answer = 'yes' if num % 2 == 0 else 'no'

    return num, correct_answer
