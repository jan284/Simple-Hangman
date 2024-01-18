"""
File: guess_letters.py

This module contains the function guess_letters which runs
a single iteration of hangman with the word provided. The
placeholder parameter is a list of underscores the length of
the given word.
"""


from config import LETTERS, MAX_GUESSES


def guess_letters(word, placeholder):
    """
    Takes input from user until word is guesses or max guesses
    is exceeded
    :param word: random word from dictionary
    :type word: str
    :param placeholder: list of underscores representing word
    :type placeholder: list
    """
    # Initialize number of guesses to increment each time an new incorrect guess is made
    num_guesses = 0
    # Create empty list to store guessed letters
    guesses = []

    print('Here\'s your word:', ''.join(placeholder))
    guess = input('Guess a letter: ')

    while True:

        # Checks length of input for validity
        if len(guess) > 1:
            print('Invalid entry.')
            guess = input('Enter 1 letter: ')
            print()

        # Checks that input is a letter
        elif guess not in LETTERS:
            print('Invalid entry.')
            guess = input('Try a letter: ')
            print()

        # Checks if input has already been guessed
        elif guess.upper() in guesses:
            print('You\'ve already guessed the letter', guess.upper())
            guess = input('Try another letter: ')
            print()

        # Searches word for correctly guessed letter and replaces underscores in correct postion(s)
        elif guess.upper() in word:
            for letter in range(len(placeholder)):
                if guess.upper() == word[letter]:
                    placeholder[letter] = guess.upper()
            # Adds correct guess to list of guessed letters
            guesses.append(guess.upper())
            print(' '.join(placeholder), '\n')

            # Word has been correctly guessed if remaining underscores have been replaced with current guess
            if '_' not in placeholder:
                print('Awesome! You win! =)')
                break
            else:
                guess = input('Guess a letter: ')
                print()

        else:
            # Checks if user has reached maximum number of incorrect allowed guesses
            if num_guesses == MAX_GUESSES:
                print('Sorry. You lose. =(')
                print('The word was', word)
                break
            else:
                # Increment number of guesses and prompt user to continue guessing
                guesses.append(guess.upper())
                num_guesses += 1
                print('The letter', guess.upper(), 'is not in your word.\n\
You have', (MAX_GUESSES - num_guesses), 'incorrect guesses left.')
                print(' '.join(placeholder), '\n')
                guess = input('Guess a letter: ')
