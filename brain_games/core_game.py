import prompt


MAX_ITER_TO_WIN = 3


def core(game_rules, game_option):
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(game_rules)

    for _ in range(MAX_ITER_TO_WIN):
        quest, correct_ans = game_option()

        print(f'Question: {quest}')

        user_ans = prompt.string('Your answer: ')

        if user_ans == correct_ans:
            print('Correct!')
        else:
            print(f"'{user_ans}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{correct_ans}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
