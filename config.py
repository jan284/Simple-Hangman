"""
File: config.py

This module defines basic constants and functions for gameplay
"""

import string

LETTERS = string.ascii_letters

MAX_GUESSES = 6


def print_lets_play():
    print("\nLet's play a game of Hangman!\n\
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


def create_placeholder(random_word):
    placeholder = ['_'] * len(random_word)
    return placeholder
