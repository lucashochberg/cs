# Name: Lucas Hochberg
# Log: 1.0
# Bonus Features: Emoji's on the board, Randomly selects who goes first
# Bugs: None
# Description: Outputs a BattleShip game against the computer

import random

def print_board(board, hide_ships = False):
    '''
    Creates cleaner format when printing the board

    Args:
        board: The original battleship board

    Returns:
        board: The new, cleaner board

    Raises:
        None
    '''
    for row in board:
        display_row = []
        for cell in row:
            if hide_ships and cell == '🚢':
                display_row.append('🌊')
            else:
                display_row.append(cell)
        print(" ".join(display_row))

def add_ships(board):
    '''
    Adds 4 ships randomly to the board

    Args:
    '''
    counter = 0
    while counter < 4:
        row = random.choice([1, 3, 5, 7, 9])
        col = random.choice([1, 3, 5, 7, 9])
        if board[row][col] != '🚢':
            board[row][col] = '🚢'
            counter += 1

def user_coordinate_converter(user_guess):
    '''
    Converts the user input into a valid coordinate on the board

    Args:
        user_guess: The user's coordinate input

    Returns:
        user_guess: The input with new coordinate values

    Raises:
        None
    '''
    rows = {'A': 1, 'B': 3, 'C': 5, 'D': 7, 'E': 9}
    cols = {'1': 1, '2': 3, '3': 5, '4': 7, '5': 9}
    return rows[user_guess[0]], cols[user_guess[1]]

def create_board(label):
    '''
    Creates the BattleShip board

    Args:
        label: The label that is under the board

    Returns:
        label: Converts the label depending on which board the label is assigned to

    Raises:
        None
    '''
    return [
    ['  --------------------------'],
    ['A |', '🌊', '|', '🌊', '|', '🌊', '|', '🌊', '|', '🌊', '| A'],
    ['  --------------------------'],
    ['B |', '🌊', '|', '🌊', '|', '🌊', '|', '🌊', '|', '🌊', '| B'],
    ['  --------------------------'],
    ['C |', '🌊', '|', '🌊', '|', '🌊', '|', '🌊', '|', '🌊', '| C'],
    ['  --------------------------'],
    ['D |', '🌊', '|', '🌊', '|', '🌊', '|', '🌊', '|', '🌊', '| D'],
    ['  --------------------------'],
    ['E |', '🌊', '|', '🌊', '|', '🌊', '|', '🌊', '|', '🌊', '| E'],
    ['  --------------------------'],
    ['     1    2    3    4    5  '],
    [f'          {label}           ']]

def main():

    user_attack = create_board("YOUR ATTACK")                                                           # print a board and replace the label with 'YOUR ATTACK'
    comp_attack = create_board("YOUR SHIPS")
    enemy_ships = create_board("ENEMY SHIPS")

    add_ships(enemy_ships)                                                                              # randomly place ships on the user attack board
    add_ships(comp_attack)

    valid_inputs = [f"{r}{c}" for r in "ABCDE" for c in "12345"]                                        # sets valid inputs to any combination of letters between A and E and numbers between 1 and 5
    used_guesses = set()                                                                                # creates a set for past guesses
    user_hits = 0
    computer_hits = 0
    turn = random.choice([True, False])

    print("welcome to battleship")
    print("first to sink all 4 ships wins")

    while user_hits < 4 and computer_hits < 4:
        print("here is your attack board")
        print_board(user_attack)

        print("here is the computer's attack board")
        print_board(comp_attack, hide_ships = True)

        if turn:
            print("it is your turn")
            user_guess = input("choose a coordinate (e.g. A1, B5): ").upper()

            if user_guess not in valid_inputs:
                print("invalid input. try again")
                continue

            if user_guess in used_guesses:
                print("you already guessed that. try again")
                continue

            used_guesses.add(user_guess)                                                                # add the previous guesses to the set
            row, col, = user_coordinate_converter(user_guess)

            if user_attack[row][col] in ['💥', '❌']:                                                  # if the spot has one of these emojis
                print("already targeted that spot. try again")                                          # print this statement
                continue

            if enemy_ships[row][col] == '🚢':                                                          # if the spot on the computer attack is this emoji
                user_attack[row][col] = '💥'                                                           # change it to this emoji
                user_hits += 1                                                                          # add a hit for the user
                print("💥 you hit a ship!")

                if user_hits == 4:
                    print_board(user_attack)
                    print("🎉 you win! you sank all 4 enemy ships")
                    break

            else:
                user_attack[row][col] = '❌'
                print("you missed")
                turn = False

        else:
            print("it is the computer's turn")
            while True:
                row = random.choice([1, 3, 5, 7, 9])                                                    # tells the computer to guess a number from these choices
                col = random.choice([1, 3, 5, 7, 9])
                if comp_attack[row][col] not in ['💥', '❌']:
                    break

            row_map = {1: 'A', 3: 'B', 5: 'C', 7: 'D', 9: 'E'}                                          # creates a row conversion for coordinates
            col_map = {1: '1', 3: '2', 5: '3', 7: '4', 9: '5'}                                          # creates a column conversion for coordinates
            print(f"computer guessed at {row_map[row]}{col_map[col]}")

            if comp_attack[row][col] == '🚢':
                comp_attack[row][col] = '💥'
                computer_hits += 1
                print("💥 the computer hit your ship")

                if computer_hits == 4:
                    print_board(comp_attack, hide_ships = False)
                    print("😢 WOMP WOMP. the computer sank all your ships.")
                    break

            else:
                comp_attack[row][col] = '❌'
                print("the computer missed")
                turn = True
            
main()