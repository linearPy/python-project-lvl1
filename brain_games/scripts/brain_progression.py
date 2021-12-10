#!/usr/bin/env python


from brain_games.core_game import core
from brain_games.games.progression import GAME_RULES
from brain_games.games.progression import run


def main():
    core(GAME_RULES, run)


if __name__ == '__main__':
    main()
