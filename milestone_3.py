
import random





word_list=['banana', 'apple', 'blueberry', 'mango', 'peach']
word = random.choice(word_list)
#word_guessed=['_']*len(word)
#num_lives = 7
print(word)

def check_guess(guess): 
    for i in word:
        if i in guess.lower():
            print("Good guess!" ,guess, " is in the word.")
        else:
            print("Sorry" ,guess , "is not in the word. Try again.")

    
def ask_for_input():
    guess =input("enter a single letter")
    while True:
        if len(guess)==1 and guess.isalpha():
            check_guess(guess)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
            ask_for_input()
   

check=ask_for_input()
print(check)

