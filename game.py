# game.py


import random

print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

#
# asking user for an input
#


user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")

print(f"You chose: {user_choice}")

#
#simulating a computer input
#

#computer_choice = "paper"

#foo = ['a', 'b', 'c', 'd', 'e']
#computer_choice = random.choice(foo)

options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)

print(f"The computer chose: {computer_choice}")

#
# validate the user selection
#
# stop the program (not try to determine the winner)
# ... if the user chocie is invalid

#user_choice.lower()

#if user_choice in options:
    #print("GOOD")
    #pass
#else:
    #print("OOPS, please choose a valid option and try again")
    #exit()

if user_choice not in options:
    print("OOPS, please choose a valid option and try again")
    exit()


#
# Determining who won
# If statement is adapted from solution shared by Estelle in class 
#

if computer_choice == "paper" and user_choice == "scissors":
    print("Congrats! You Won!")
elif computer_choice == "scissors" and user_choice == "rock":
    print("Congrats! You Won!")
elif computer_choice == "rock" and user_choice == "paper":
    print("Congrats! You Won!")
elif computer_choice == user_choice:
    print("It's a tie!")
else:
    print("Oh, the computer won. It's ok.")

print("-------------------")

#exit message

print("Thanks for playing. Please play again!")

exit()