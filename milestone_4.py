
import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    
    
    
    
    def __init__(self, word_list, num_lives=5):
        # TODO 2: Initialize the attributes as indicated in the docstring
        # TODO 2: Print two message upon initialization:
        # 1. "The mistery word has {num_letters} characters"
        # 2. {word_guessed}
        self.word_list=word_list#list of fruits
        self.num_lives= num_lives#number of lives
        self.word = random.choice(self.word_list)#random word chosen from list of words
        self.word_guessed=['_']*len(self.word)#list of the correct word which will be filled with correct guesses
        self.list_of_guesses=[]#the list of guesses which the guesses will be appended to
        self.num_letters=len(set(self.word))#number of letters still left to guess 
    

    def check_guess(self, guess):
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        # TODO 3: Check if the letter is in the word. TIP: You can use the lower() method to convert the letter to lowercase
        # TODO 3: If the letter is in the word, replace the '_' in the word_guessed list with the letter
        # TODO 3: If the letter is in the word, the number of UNIQUE letters in the word that have not been guessed yet has to be reduced by 1
        # TODO 3: If the letter is not in the word, reduce the number of lives by 1
        # Be careful! A letter can contain the same letter more than once. TIP: Take a look at the index() method in the string class
        guess=guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if self.word[i]==guess:
                    self.word_guessed[i]=guess
            self.num_letters-=1
        else:
            self.num_lives-=1
            print(f"Sorry {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left")     
        self.list_of_guesses.append(guess) 


    def ask_for_input(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        # TODO 1: Ask the user for a letter iteratively until the user enters a valid letter
        # TODO 1: Assign the letter to a variable called `letter`
        # TODO 1: The letter has to comply with the following criteria: It has to be a single character. If it is not, print "Please, enter just one character"
        # TODO 2. It has to be a letter that has not been tried yet. Use the list_letters attribute to check this. If it has been tried, print "{letter} was already tried".
        # TODO 3: If the letter is valid, call the check_letter method
        
        
        guess =input("enter a single letter")
        guess=guess.lower()
        if len(guess)!=1 or not guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)
       
                

# In the play game definition I call the hangman class and create in instance called game. 
#using a while loop I set the conditions for winning and losing. Aswell as continuing the game 
#is its still in progress.

def play_game():
    # As an aid, part of the code is already provided:
    game = Hangman(word_list, num_lives=5)
    while True:
        if game.num_lives==0:
            print(f'You lost! The word was {game.word}')
            break
        elif game.num_letters>0:
            game.ask_for_input()

        elif game.num_lives!=0 and game.num_letters==0:
            print('Congratulations!you won!')
            break
         


word_list = ["apple", "mango", "peach", "blueberry", "watermelon"]
play_game()
    
