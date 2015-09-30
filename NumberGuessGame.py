__author__ = 'demi'
#myNumber
# This game uses a home made function

import random

#think of a number
computer_number = random.randint(1,100)

def is_same(target, number):
    if target == number:
        result ="Win"
    elif target > number:
        result="Low"
    else:
        result = "High"
    return result

#Start the Game
print("Hello \n I have thought of a number between 1 and 100")

# Collect the users guess as an integer
guess = int(input("Can you guess it? "))

#Use our function
higher_or_lower = is_same(computer_number, guess)

#Run the Game until user is correct
while higher_or_lower != "Win":
    if higher_or_lower == "Low":
        guess = int(input("Sorry you are too low, Try Again. "))
    else:
        guess = int(input("Sorry you are too High, Try Again "))

    higher_or_lower = is_same(computer_number, guess)

input("Correct!\nWell done \n\n\nPress ENTER to Exit.")
