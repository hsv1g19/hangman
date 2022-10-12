# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

import random
word_list=['banana', 'apple', 'blueberry', 'mango', 'peach']
word = random.choice(word_list)

guess =input("enter a single letter")

if len(guess)==1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input." )
