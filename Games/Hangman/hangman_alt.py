from random import randint
from ascii_hangman import ascii_hangman
from time import sleep

# Ask the user some info and be friendly
name = input('Hello, what is your name? ')
print('\nHello', name)

# ask what their favorite color is
color = input('\nWhat is your favorite color? ')

colors = ['orange', 'pink', 'blue', 'red', 'teal', 'violet']
print(color, 'is cool, but I like', colors[randint(0, len(colors)-1)])

# Gather words to be used
words = [word.strip('\n') for word in open('easy_words.txt')]

# Pick a secret word and prepare the game list
secret = words[randint(0, len(words)-1)]
secret_list = list(secret)
empty_list = ['_' for num in range(len(secret_list))]

empty = ''
empty = empty.join(empty_list)

# set the number of tries and failures
tries = 7
failures = 0

sleep(2)

# Start the game
print('\nI have a secret word, try and guess it. You get', tries, 'wrong guesses. Good luck!')

sleep(1)
print('\nThe secret word has', len(secret), 'letters in it')

# Loop until too many wrong guesses or the complete word
while failures < tries:
    print('Here is the word', empty)

    letter = input('\nGuess a letter: ').lower()

    # If letter is contained in the secret, process it as correct
    if letter in secret:
        print('\nCorrect')
        for idx, val in enumerate(secret_list):
            if val == letter:
                empty_list[idx] = val
                empty = ''
                empty = empty.join(empty_list)
        # If the word is complete, end the loop
        if empty == secret:
            break
    # If the letter isnt in the secret, its wrong
    else:
        print('\nWrong! Try again')

        # Adds hangman ascii art, you can comment this out if not desired
        print(ascii_hangman[failures])

        failures += 1

    left = tries - failures
    print('You have ', left, " guesses left")

# End Game ... not the movie...
if failures == 7:
    print('The word was', secret)
else:
    print('Congrats!!')
