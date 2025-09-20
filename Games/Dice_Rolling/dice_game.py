import random

playing = False
not_answered = True
exit_msg = "That's too bad. Have a nice day!"

print("Hello, would you like to play the dice game?")
user_inp = input()
user_inp.lower()

# Check if user wants to play.
while not_answered:
    if user_inp == "":
        user_inp = input("Please re-enter response: ")
    if user_inp == "yes" or user_inp == "y":
        print ("Great, Let's Play!")
        playing = True
        not_answered = False
    elif user_inp == "no" or user_inp == "n":
        not_answered = False
        print(exit_msg)    
    else:
        print("Input is incorrect.\nPlease enter a 'yes' 'y' 'no' or 'n'")
        user_inp = ""

# loop through game unitl user quits
while playing:
    rand_num = random.randint(1, 6)

    print("\n-------------------------\n I Have Chosen a Number! \n-------------------------")

    #check for input error, int only allowed
    while True:
        try:
            user_inp = int(input("What is your guess?\n"))
            break
        except:            
            print("Input is incorrect. Please enter a valid number")

    if user_inp == rand_num:
        print("\nCongratulations! The number was: " + str(rand_num))
    else:
        print("\nI'm Sorry, the number was: " + str(rand_num))
    not_answered = True

    #check if player wants to keep playing
    while not_answered:
        user_inp = input("Would you like to play again?\n")
        user_inp.lower()
        if user_inp == "no" or user_inp == "n":
            playing = False
            not_answered = False
            print(exit_msg)
        elif user_inp == "yes" or user_inp == "y":
            not_answered = False
        else:
            print("Input is incorrect.\nPlease enter a 'yes' 'y' 'no' or 'n'")
            user_inp = ""

