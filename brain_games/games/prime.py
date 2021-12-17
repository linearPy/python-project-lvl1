import random
import math


GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


MIN_RAND = 1
MAX_RAND = 30


def is_prime(num):
    for div in range(2, math.isqrt(num) + 1):
        if num % div == 0:
            return False

    return True


def run():
    num = random.randint(MIN_RAND, MAX_RAND)

    correct_answer = 'yes' if is_prime(num) else 'no'

    return str(num), correct_answer
