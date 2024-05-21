
playing_game = False
# ask if we want to play.
user_play = input("Do you want to play RPS? (y/n) ")

# if the player says Y:
if user_play == 'y':
    playing_game = True
    
while playing_game == True:
    # play the game
    print("Playing Game")
    
    
    
    
    # end of game
    # ask player if they want to play again
    user_play = input("Do you want to play again? (y/n) ")
    # if yes - loop back to beginning
    if user_play == 'y':
        playing_game = True
    else:
        playing_game = False
            
# otherwise:
    # say thanks goodbye
print("Thanks, goodbye")
