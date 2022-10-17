# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

In this code I set up a list of 5 fruits and using the random module created a variable word which would pick a random fruit from the list. I also created an input called guess, to guess a sing letter. Then created an if conditon checking if the letter has length 1 and is a letter in the alphabet.

"""import random
word_list=['banana', 'apple', 'blueberry', 'mango', 'peach']
word = random.choice(word_list)

guess =input("enter a single letter")

if len(guess)==1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input." )"""

I created 2 functions called, check_guess and ask_for_input. The check_guess function will take the guessed letter as an argument and check if the letter is in the word. I alsoo coverted the guess to lowercase and in the fuction ask_for_input I moved the code I wrote previously to iteratively check if the input is a valid guess. If it is not it will exit the while loop and the user will be asked to enter another input guess.


