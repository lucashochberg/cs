from random_word import RandomWords                                         # Imports a list of random words from the terminal
import random                                       # Chooses a random word from that list

def main():                                      # Creates the main function
    while True:                                      # Loop to allow replaying
        rw = RandomWords()                                      # sets rw = to the list of random words
        random_word = rw.get_random_word()                                       # Get a random word from the API

        # Print the random word hidden as underscores
        display = "_" * len(random_word)                                         # Create a string with underscores for each letter
        print(f"Random word: {display}")                                         # Show the underscores for the word

        lives = 5                                       # Sets lives = 5
        display_hangman(lives)                                      # Displays the hangman without any lives taken

        guessed_letters = []                                        # List to store the guessed letters

        while lives > 0:                                        # While lives is greater than 0
            user_guess = input("What letter do you want to guess?: ").lower()                                       # Asks the user what letter they want to guess and allows lowercase letters in response

            # Ensure valid input (only one letter and alphabetic)
            if not user_guess.isalpha() or len(user_guess) != 1:                                        # If the guess is not a letter or is multiple character long
                print("please enter a single letter.")                                      # Print the message
                continue                                        # Ask the user the question again

            if user_guess in guessed_letters:                                       # If the guess has already been guessed
                print(f"you already guessed {user_guess}. try a different letter.")                                         # Print the message
                continue                                        # Ask the user the question again

            guessed_letters.append(user_guess)                                       # Add the guessed letter to the list

            if user_guess not in random_word:                                        # if the guess is not in the random word
                lives -= 1                                      # Take a life away
                display_hangman(lives)                                       # Display the new hangman
                print(f"incorrect guess. you have {lives} lives left.")                                         # Print the message
            else:                                       # If the guess is in the word
                display = display_board(random_word, user_guess, display)                                        # Display the new board
                print(display)                                      # Display the word with the letter guessed uncovered

            # Check win condition
            if "_" not in display:                                      # If the display does not have a blank
                print("you win! the word was:", random_word)                                        # Print the message
                break                                       # Exit the loop
            # Check lose condition
            if lives == 0:                                      # If lives = 0
                print("you lose! the word was:", random_word)                                       # Print the message
                break                                       # Exit the loop
        
        
        while True:                                         # Creates a loop
            play_again = input("do you want to play again? (y/n): ")                                        # Asks if the user wants to play again
            play_again = play_again.lower()                                         # Allows lowecase in response
            play_again = play_again[0]                                      # Only takes the first letter of the response
            if play_again == 'y':                                       # If the first letter = y
                main()                                      # Returns to the beginning of the main function
                break                                       # Exits the loop
            elif play_again == 'n':                                         # If the first letter = n
                print("thanks for playing!")                                        # Print the message
                quit()                                      # End the code
            else:                                        # If the first letter is anything else
                print("invalid response")                                       # Print the message and ask the user the question again


def display_board(random_word, user_guess, display):                                        # Creates a display board function
    '''
    Update the display string with correctly guessed letters

    Args:
        random_word: The word chosen from the list RandomWords
        user_guess: # A letter that is being guessed by the user
        display: The display of the word

    Returns:
        display: The updated display depending on the user's correct guesses

    Raises:
        None
    '''
    display = list(display)                                         # Convert display string to a list for mutability
    for i in range(len(random_word)):
        if random_word[i] == user_guess:
            display[i] = user_guess
    return "".join(display)                                         # Convert back to string after updating


def display_hangman(lives):                                         # Creates a function for the display of the hangman
    '''
    Displays the hangman graphic based on the number of tries left.

    Args:
        lives (int): The amount of lives left

    Returns:
        int: The desplay based on the number of lives left

    Raises:
        None
    '''
    stages = [                                      # Creates a list for the stages of lives
        """
          --------
          |      |
          |      
          |     
          |      
          |     
          -
        """,
        """
          --------
          |      |
          |      O
          |      
          |      
          |     
          -
        """,
        """
          --------
          |      |
          |      O
          |     \|
          |      
          |      
          -
        """,
        """
          --------
          |      |
          |      O
          |     \|/
          |      
          |     
          -
        """,
        """
          --------
          |      |
          |      O
          |     \|/
          |      |
          |     /
          -
        """,
        """
          --------
          |      |
          |      O
          |     \|/
          |      |
          |     / \\
          -
        """
    ]
    print(stages[5 - lives])                                        # Display the correct hangman stage based on remaining lives

main()                                      # Calls the main function
