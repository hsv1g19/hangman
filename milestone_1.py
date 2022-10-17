import random
word_list=['banana', 'apple', 'blueberry', 'mango', 'peach']
word = random.choice(word_list)

guess =input("enter a single letter")

if len(guess)==1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input." )


for i in word:
    if i in guess.lower():
            print("Good guess!" ,guess, " is in the word.", end=" ")
else:
    print("Sorry" ,guess , "is not in the word. Try again.", end="")
            