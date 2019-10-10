user_input = input("Hello, would you like to play the dice game?\n")
playing = False
if user_input.lower() == "yes":
    print ("Great, Let's Play!")
    playing = True
elif user_input.lower() == "no":
    print ("That's too bad. Have a nice day!")
else:
    print ("Sorry I couldn't understand you" + "\nYou said: " + user_input)

