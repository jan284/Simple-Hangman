# Simple Hangman

## Description

A bare-bones game of hangman you can run in your terminal. No fancy graphics nor pygame involved.

***

### dictionary.txt
List of 267750 words and non-words.

### config.py
Contains constants for ASCII letters and maximum number of incorrect guesses allowed 
along with helper functions to 1. display the game's welcome banner (print_lets_play) and 2.
create a blank placeholder to display the word as the user continues to guess (create_placeholder).

### io_utils.py
The get_filehandle function is used to open the dictionary (and potentially any future files) safely.

### get_word.py
The get_word function opens the dictionary and returns a random word from the list.

### guess_letters.py
The guess_letters function is the bulk of the gameplay. It prompts the user for
input until the word is guessed or the number of incorrect number of guesses allowed
has been exhausted.

### gameplay.py
Imports and calls the functions above and starts a new game if the user wants to play again. 

_Running the program:_  
python gameplay.py  
OR  
python3 gameplay.py

***

### Author
Janiel Thompson

### Date Created
October 30, 2018  
Refactored January 17, 2024