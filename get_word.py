"""
File: get_word.py

This module contains the get_word function to pick a random word
from the dictionary for the user to guess
"""

import random

from io_utils import get_filehandle


def get_word():
    """
    Opens the dictionary and picks a word
    :return: random word
    """
    # Open dictionary and grab a random word
    dictionary = get_filehandle("dictionary.txt")
    words = dictionary.readlines()
    num_words = len(words)
    random_word = words[random.randint(1, num_words)].strip()

    return random_word
