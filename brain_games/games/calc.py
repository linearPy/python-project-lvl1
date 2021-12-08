import random
import operator


GAME_RULES = 'What is the result of the expression?'


MIN_RAND = 1
MAX_RAND = 20


def run():
    first_num = random.randint(MIN_RAND, MAX_RAND)
    second_num = random.randint(MIN_RAND, MAX_RAND)

    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }

    op_str, operation = random.choice(list(operators.items()))

    question = f'{first_num} {op_str} {second_num}'
    correct_answer = operation(first_num, second_num)

    return question, str(correct_answer)
