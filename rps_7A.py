import random


# Game choices
# We store the possible choices in a list like this
choices = ["rock", "paper", "scissors"]

#TASK 1 
# Get user choice
# How do we get the input from you, the user? Can't figure it out? Have you tried looking for Python input on W3 schools? 
user_choice = #You have to fix this line


# Generate a random number for computer choice
computer_choice = choices[random.randint(0, 2)] #this code decides the computer's choice by randomly choosing between rock paper and scissors
print(f"Computer chose: {computer_choice}")

#TASK 2
# Determine the winner using only if-else logic
# Compare the user's choice with the computer's choice to determine the outcome
# TASK2.1 Check if it's a tie
#Delete the # on the line below this one 
#if user_choice == computer_choice:
    # If it's a tie, print that it's a tie

# TASK 2.2 Check if the user chose 'rock'

    #Task 2.3 If the computer chose 'scissors', print that the user wins
  
        # Fill in the appropriate print statement for rock beating scissors
   
        # Otherwise, print that the user loses because paper covers rock

#Task 2.3 Check if the user chose 'paper'

    # TASK 2.4 If the computer chose 'rock', print that the user wins
  
        # Fill in the appropriate print statement for paper covering rock
   
        # Otherwise, print that the user loses because scissors cut paper

# TASK 2.5 Check if the user chose 'scissors'

    # TASK 2.6 If the computer chose 'paper', print that the user wins
    
        # Fill in the appropriate print statement for scissors cutting paper

        # Otherwise, print that the user loses because rock smashes scissors