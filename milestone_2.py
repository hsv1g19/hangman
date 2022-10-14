
import random


guess =input("enter a single letter")
while True:
    if len(guess)==1 and guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character." )


word_list=['banana', 'apple', 'blueberry', 'mango', 'peach']
word = random.choice(word_list)
print(word)

 
for i in word:
    if i in guess:
        print("Good guess! {guess} is in the word.")
        break
else:
    print("Sorry, {guess} is not in the word. Try again.")
        
        