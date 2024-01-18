"""
File: gameplay.py

This program runs hangman gameplay
Running the program:
python gameplay.py
python3 gameplay.py
"""

import sys

from config import create_placeholder, print_lets_play
from get_word import get_word
from guess_letters import guess_letters


def main():
    """
    Main logic
    """

    random_word = get_word()
    placeholder = create_placeholder(random_word)
    print_lets_play()
    guess_letters(random_word, placeholder)

    # Start another game
    another = input('\nDo you want to play again, Y/N? ')
    if another.upper().startswith('Y'):
        main()
    else:
        print('\nThanks for playing.\nGoodbye!\n')
        sys.exit()


if __name__ == '__main__':
    main()
