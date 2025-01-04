# Name: Lucas Hochberg
# Log: 1.0
# Bonus Features: Allows the user to play again if preferred, Allows the user to play with 2 people
# Bugs: None
# Description: A two player tic-tac-toe simulator



import random                                       # allows the choice between who goes first to be random between x and o    

def print_board(tttboard):                                      # creates the function "print_board" and the integer "tttboard"
    '''
    Creates a way to print the board with only the numbers and none of the brackets, etc...

    Args:
        tttboard: The original tic-tac-toe board

    Returns:
        tttboard: The improvised and easier to look at tic-tac-toe board

    Raises:
        None
    '''
    for row in range(len(tttboard)):
        for col in range(len(tttboard[row])):
            print(tttboard[row][col], end = " ")
        print("")

def take_turn(tttboard, turn):                                      # decide whos turn is up
    '''
    Allows the game to switch between players after each turn is taken

    Args:
        turn: Whos turn it is originally

    Returns:
        turn: Who is up next

    Raises:
        Error: If turn does not = x or o
     '''  
    if turn == 'x':
        get_spot(tttboard, 'x')
        turn = 'o'
    else:
        get_spot(tttboard, 'o')
        turn = 'x'

def get_spot(tttboard, x_or_o):                                         # creates the function "get_spot" as well as the variable "x_or_o"
    '''
    Allows the user to take a spot on the board when it is their turn

    Args:
        x_or_o (int): Whos turn it is

    Returns:
        int: Where the player wants to go on the board

    Raises:
        Error: If the spot is taken
    '''
    while True:                                         # creates a loop
        spot = input("where do you want to go '" + x_or_o + "'? (1-9): ")
        if spot == "1" and tttboard[0][0] == 1:
            tttboard[0][0] = x_or_o
            break
        elif spot == "2" and tttboard[0][1] == 2:
            tttboard[0][1] = x_or_o
            break
        elif spot == "3" and tttboard[0][2] == 3:
            tttboard[0][2] = x_or_o
            break
        elif spot == "4" and tttboard[1][0] == 4:
            tttboard[1][0] = x_or_o
            break
        elif spot == "5" and tttboard[1][1] == 5:
            tttboard[1][1] = x_or_o
            break
        elif spot == "6" and tttboard[1][2] == 6:
            tttboard[1][2] = x_or_o
            break
        elif spot == "7" and tttboard[2][0] == 7:
            tttboard[2][0] = x_or_o
            break
        elif spot == "8" and tttboard[2][1] == 8:
            tttboard[2][1] = x_or_o
            break
        elif spot == "9" and tttboard[2][2] == 9:
            tttboard[2][2] = x_or_o
            break
        else:
            print("invalid response")

def check_winner(tttboard, player):                                         # check if there is a winner
    '''
    Creates a win condition

    Args:
        player: Whos turn it is
    
    Returns:
        player status: If player has made a win pattern

    Raises:
        None
    '''
    status = "go"    
    if tttboard[0][0] == player and tttboard[0][1] == player and tttboard[0][2] == player:
        print(f"{player} wins")
        status = "stop"
    elif tttboard[1][0] == player and tttboard[1][1] == player and tttboard[1][2] == player:
        print(f"{player} wins")
        status = "stop"
    elif tttboard[2][0] == player and tttboard[2][1] == player and tttboard[2][2] == player:
        print(f"{player} wins")
        status = "stop"
    elif tttboard[0][0] == player and tttboard[1][0] == player and tttboard[2][0] == player:
        print(f"{player} wins")
        status = "stop"
    elif tttboard[0][1] == player and tttboard[1][1] == player and tttboard[2][1] == player:
        print(f"{player} wins")
        status = "stop"
    elif tttboard[0][2] == player and tttboard[1][2] == player and tttboard[2][2] == player:
        print(f"{player} wins")
        status = "stop"
    elif tttboard[0][0] == player and tttboard[1][1] == player and tttboard[2][2] == player:
        print(f"{player} wins")
        status = "stop"
    elif tttboard[0][2] == player and tttboard[1][1] == player and tttboard[2][0] == player:
        print(f"{player} wins")
        status = "stop"
    elif all(isinstance(tttboard[i][j], str) for i in range(3) for j in range(3)):
        print("you tied")
        return "stop"
    return status
    

def main():                                         # creates a main function
    print("welcome to your tic-tac-toe simulator")                                      # prints the message

    tttboard = [                                        # creates the board
        [1, 2, 3], 
        [4, 5, 6],
        [7, 8, 9]]

    players = []                                        # creates an empty list for player names
    players.append(input("enter player 1 name: "))                                      # asks the user what player 1's name is
    players.append(input("enter player 2 name: "))                                      # asks the user what player 2's name is
    
    current_player = random.choice(["x", "o"])                                      #randomly choose the player to start the game
    player1 = random.choice(players)                                        # picks a player from the list
    
    print(f"{player1} will start the game as {current_player}")                                         # prints the message
    
    counter = 0                                         # sets the move counter to zero
    
    
    while counter <= 9:                                         # if the amount of turns that have gone is less than or equal to 0

        go = True                                       # set status to True

         
        if current_player == "x":                                       # if turn = x
            take_turn(tttboard, "x")                                        # choose where they want to go
            current_player = "o"                                        # set turn to o
            print_board(tttboard)                                       # print the new board
            result = check_winner(tttboard, "x")                                        # check if x has won the game
            if result == "stop":                                        # if there's a winner or a tie
                while go:                                       # if there is a winner
                    resp = input("would you like to play again? (y/n): ")                                       # ask the user if they want to play again
                    resp = resp.lower()                                         # ask the user if they want to play again
                    resp = resp[0]                                      # only care about first letter in response
                    if resp == 'y':                                         # if response starts with y
                        main()                                      # restart the game
                        break                                       # go back to the beginning of the code
                    elif resp == 'n':                                        # if response starts with n
                        print("thanks for playing")                                         # print the message
                        quit()                                          # end code
                    else:                                       # if response starts with anything else
                        print("invalid response")                                       # print the message and ask the user the question again

        counter += 1                                        # add 1 to turn counter
        
        if current_player == "o":                                       # if turn = o
            take_turn(tttboard, "o")                                        # choose where they want to go
            current_player = "x"                                        # set turn to x
            print_board(tttboard)                                       # print the new board
            result = check_winner(tttboard, "o")                                        # check if o has won the game
            if result == "stop":                                        # if there's a winner or a tie
                while go:                                       # if there is a winner
                    resp = input("would you like to play again? (y/n): ")                                       # ask the user if they want to play again
                    resp = resp.lower()                                         # ask the user if they want to play again
                    resp = resp[0]                                      # only care about first letter in response
                    if resp == 'y':                                             # if response starts with y
                        main()                                      # restart the game
                        break                                       # go back to the beginning of the code
                    elif resp == 'n':                                       # if response starts with n
                        print("thanks for playing")                                         # print the message
                        quit()                                      # end code
                    else:                                       # if response starts with anything else
                        print("invalid response")                                       # print the message and ask the user the question again
                        
        
        counter += 1                                        # add 1 to the turn counter

main()                                      # call the main function
