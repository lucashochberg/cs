# Name: Lucas Hochberg
# Date: 3/9/2023
# Description: Rock, Paper, Scissors Simulator against a bot. It keeps score and asks if you want to play again.
# Bugs: If I imputed an invalid response into the first question, instead of it asking me if I wanted Rock, Paper, or Scissors, it would ask if I wanted to play again. It took me a while to change the code so instead of typing rock, paper, or scissors, any word that started with r would count as rock, any word that started with p would count as paper, and any word that started with s would count as scissors.
# Challenges: The game determines and shows who wins every round and can keep score over multiple rounds.
# Sources: Ms. Marciano / Henry Santangelo

import random # Generates a random output based on the weapons
print("hello.") # Prints what is in quotes
weapons = ["r", "p", "s"] # Creates a list of the weapons
print ("welcome to the rock, paper, scissors simulator.") # Prints what is in quotes
u_score = 0 # Keeps score for the user
bot_score = 0 # Keeps score for the bot
while True: # Creates a loop
    bot_play = random.choice(weapons) # Makes the bots choice random
    u_play = input("rock, paper, or scissors? ") # Asks the user what is in quotes
    u_play = u_play.lower() # If the response is lowercase it is still valid
    if u_play[0] not in weapons: # If the user enters a response that doesn't start with r, p, or s
        print("please enter a valid response.") # Prints what is in quotes
    else: # Everything else
        if u_play[0] == bot_play[0]: # If the user's response is equal to bots response
            print("it's a tie.") # Prints what is in quotes
        elif u_play[0] == "r": # If the user selects r
            if bot_play == "s": # If the bot selects s
                print("i choose scissors. you win!") # Prints what is in quotes
                u_score +=1 # Adds a point to the users score
            elif bot_play == "p": # If the bots selects p
                print("i choose paper. that's a point for me.") # Prints what is in quotes
                bot_score +=1 # Adds a point to the bot score
        elif u_play[0] == "p": # If the user selects p
            if bot_play == "s": # If the bot selects s
                print("i choose scissors. that's a point for me.") # Prints what is in quotes
                bot_score +=1 # Adds a point to the bots score
            elif bot_play == "r": # If the bot selects r
                print("i choose rock. you win!") # Prints what is in quotes
                u_score +=1 # Adds a point to the users score
        elif u_play[0] == "s": # If the user selects s
            if bot_play == "p": # If the bot selects p
                print("i choose paper. you win!") # Prints what is in quotes
                u_score +=1 # Adds a point to the users score
            elif bot_play == "r": # If the bot selects r
                print("i choose rock. that's a point for me.") # Prints what is in quotes
                bot_score +=1 # Adds a point to the bots score
        print(f"score: you - {str(u_score)} score: computer - {str(bot_score)}") # Prints the users score and the bots score after every round
        while True: # Creates a loop
            resp_again = input("would you like to play again? (y/n): ") # Asks the user if they want to play again
            resp_again = resp_again.lower() # If the response is lowercase it is still valid
            if resp_again.lower() == "y" or resp_again.lower() == "yes": # If the users response starts with y
                break # End the loop and return to the start
            elif resp_again.lower() == "n" or resp_again.lower() == "no": # If the users response starts with n
                quit() # Ends the code
            else: # Anything else
                print("invalid response") # Print this message
    