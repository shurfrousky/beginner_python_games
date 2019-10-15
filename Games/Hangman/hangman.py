import random


wordlist = ['happy', 'holiday', 'tremendous', 'warrior', 'priest', 'mage', 'saints']
playing = True
count = 0
won = True

def chooseWord():
	return wordlist[random.randint(1,len(wordlist))-1]

def checkGuess(guess, answer):
	return guess in answer

def checkEndgame(status):
	global count
	global playing
	global won
	if not status:		
		count += 1
	if count > 5:
		playing = False
		won = False

def play():
	answer = chooseWord()
	global playing
	global won
	while playing:
		guess = input('Guess a letter\n')
		checkEndgame(checkGuess(guess, answer))
	if won:
		print('Congrats!')
	else:
		print('Try Again!')
	

play()