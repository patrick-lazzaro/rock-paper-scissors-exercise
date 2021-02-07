# game.py

import os
import dotenv 
import random

#
# Customize player name 
#

dotenv.load_dotenv()
PLAYER_NAME = os.getenv("PLAYER_NAME", default="Player One") 

#
# Welcome screen
#

print("-------------------")
print(f"Welcome '{PLAYER_NAME}' to my Rock-Paper-Scissors game...")
print("-------------------")

#
# Asking user for an input
#

user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")

user_choice = user_choice.lower()

#
# Validate the user selection
# Exit program if choice is invalid 
#

options = ["rock", "paper", "scissors"]

if user_choice not in options:
    print("OOPS, please choose a valid option and try again")
    exit()

print(f"You chose: {user_choice}")

#
# Simulating a computer input
#

computer_choice = random.choice(options)

print(f"The computer chose: {computer_choice}")

#
# Determining who won
# If statement is adapted from solution shared by Estelle in slack 
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

#
# Exit message
#

print("Thanks for playing. Please play again!")

exit()