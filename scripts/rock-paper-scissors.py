# Rock wins over the Scissors
# Scissors wins over the Paper
# Paper wins over the Rock
from random import randint

objects = ("rock", "scissors", "paper")

computer = objects[randint(0, 2)]

while True:
    user = input("rock, paper or scissors? ").lower().lstrip()
    if user == computer:
        print("Tie!")
    elif user == "rock":
        if computer == "paper":
            print ("You lose! - ", computer, " covers ", user)
        else:
            print ("You win! - ", user, " smashes ", computer)
    elif user == "scissors":
        if computer == "rock":
            print ("You lose! -  ", computer, " smashes ", user)
        else:
            print ("You win! - ", user, " cut ", computer)
    elif user == "paper":
        if computer == "scissors":
            print ("You lose! - ", computer, " cut ", user)
        else:
            print ("You win! - ", user, " covers ", computer)
    else:
        print ("Invalid input!")
    computer = objects[randint(0, 2)]