__author__ = 'demi'
#  MyMagicBall

import random

# write answers

ans1="Go for it!"
ans2="No way Jose"
ans3="I'm not sure, ask me again"
ans4="Fear of the unknown is what imprisons us"
ans5="What would Jesus Do?"
ans6="Your stomach is right"
ans7="Birds of a feather, flock together"
ans8="I don't think that is a good idea, do you?"
ans9="Always act with kindness and love"
ans10="Either way it makes no difference at all"
ans11="He/She loves you"

print("Welcome to MyMagic8Ball.\n")

name = input("Please enter your name so we can get to know each other!\n")

doagain = "Y"
while doagain == "Y":
    print("Hi " + name + "\n")
    question = input("Ask me for advice, then press enter to shake me.\n")

    print("Shaking ....\n" * 4)

    choice=random.randint(1,11)
    if choice == 1:
        answer = ans1
    elif choice == 2:
        answer = ans2
    elif choice == 3:
        answer = ans3
    elif choice == 4:
        answer = ans4
    elif choice == 5:
        answer = ans5
    elif choice == 6:
        answer = ans6
    elif choice == 7:
        answer = ans7
    elif choice == 8:
        answer = ans8
    elif choice == 9:
        answer = ans9
    elif choice == 10:
        answer = ans10
    else:
        answer = ans11

    print(answer)
    doagain = input("Do you want to ask again? (Y/N)? \n")

input("\n\n Press the RETURN key to Exit.")



