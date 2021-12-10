import random


GAME_RULES = 'What number is missing in the progression?'


MIN_STEP = 1
MAX_STEP = 10

MIN_START = -10
MAX_START = 100

NUMBER = 10


def run():
    step = random.randint(MIN_STEP, MAX_STEP)
    start = random.randint(MIN_START, MAX_START)
    stop = start + step * NUMBER
    progression = list(map(str, range(start, stop, step)))

    replace_index = random.randint(0, NUMBER - 1)
    correct_answer = progression[replace_index]
    progression[replace_index] = '..'

    question = ' '.join(progression)

    return question, correct_answer
