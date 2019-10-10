import random

user_input = input("Hello, would you like to play the dice game?\n")
playing = False
not_answered = True
while not_answered:
    if user_input.lower() == "yes":
        print ("Great, Let's Play!")
        playing = True
        not_answered = False
    elif user_input.lower() == "no":
        not_answered = False
    else:
        print ("Sorry I couldn't understand you" + "\nYou said: " + user_input)

while playing:
    the_number = str(random.randint(1, 6))
    print ("\n-------------------------\n I Have Chosen a Number! \n-------------------------")
    user_num = input("What is your guess?\n")
    if user_num == the_number:
        print ("\nCongratulations! The number was: " + the_number)
    else:
        print ("\nI'm Sorry, the number was: " + the_number)
    
    not_answered = True
    while not_answered:
        user_input = input("Would you like to play again?\n")
        if user_input.lower() == "no":
            playing = False
            not_answered = False
        elif user_input.lower() == "yes":
            not_answered = False
        else:
            print ("Sorry I couldn't understand you" + "\nYou said: " + user_input)

print ("That's too bad. Have a nice day!")