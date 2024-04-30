import random


# Game choices
# We store the possible choices in a list like this
choices = ["rock", "paper", "scissors"]

# Get user choice
# How do we get the input from you, the user?
user_choice = #You have to fix this line
print(user_choice)

# Generate a random number for computer choice
computer_choice = choices[random.randint(0, 2)] #this code decides the computer's choice by randomly choosing between rock paper and scissors
print("Computer chose: {computer_choice}")

# Determine the winner using only if-else logic
# Compare the user's choice with the computer's choice to determine the outcome
# Check if it's a tie
if user_choice == computer_choice:
    # If it's a tie, print that it's a tie

# Check if the user chose 'rock'

    # If the computer chose 'scissors', print that the user wins
  
        # Fill in the appropriate print statement for rock beating scissors
   
        # Otherwise, print that the user loses because paper covers rock

# Check if the user chose 'paper'

    # If the computer chose 'rock', print that the user wins
  
        # Fill in the appropriate print statement for paper covering rock
   
        # Otherwise, print that the user loses because scissors cut paper

# Check if the user chose 'scissors'

    # If the computer chose 'paper', print that the user wins
    
        # Fill in the appropriate print statement for scissors cutting paper

        # Otherwise, print that the user loses because rock smashes scissors
