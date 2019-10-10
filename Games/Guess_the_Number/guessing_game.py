import random

def main():
    solved = False
    num_to_guess = get_num()
    print (num_to_guess)
    while not solved:
        guess = input("Guess a number: ")
        if guess == num_to_guess:
            print ("Congratulations! You Win!\nThe number was: " + num_to_guess)
            solved = True
        else:
            give_hint(guess, num_to_guess)

def get_num():
    high_end = input("What number do you want to guess up to?\n")
    print (high_end)
    num = str(random.randint(0, int(high_end)))
    print ('You will be guessing a number between 0 - ' + high_end)
    return num

def give_hint(guess, num_to_guess):
    if guess < num_to_guess:
        # within 10 'youre a little low'
        if int(guess) >= int(num_to_guess) - 10:
            print ("you're a little low")
        elif int(guess) >= int(num_to_guess) - 25:
            print ("guess higher")
        else:
            print ("Way too low")
        # within 25 'guess higher'
        # more than that 'way too low'



if __name__ == "__main__":
    main()