import random


GAME_RULES = 'Find the greatest common divisor of given numbers.'


MIN_RAND = 1
MAX_RAND = 30


def gcd(first_num, second_num):
    if second_num == 0:
        return first_num

    return gcd(second_num, first_num % second_num)


def run():
    first_num = random.randint(MIN_RAND, MAX_RAND)
    second_num = random.randint(MIN_RAND, MAX_RAND)

    question = f'{first_num} {second_num}'
    correct_answer = gcd(first_num, second_num)

    return question, str(correct_answer)
