# Name: Lucas Hochberg
# Log: 1.0
# Bonus Features: Has a menu built in, Can return a sorted array of characters, Can return boolean if name contains title/distinction, Can return whether amount of letters in input is even or odd
# Bugs: None
# Description: Constructs a set of methods to manipulate and interrogate an input without using string functions


def vowel_count(user_input):                                                                                            # creates a function for number 2
    '''
    Counts and prints the amount of vowels in the input

    Args:
        user_input: What the user puts as their name

    Returns:
        vcount: The amount of vowels in the input

    Raises:
        None
    '''
    vcount = 0 
    vowel = list("aeiouAEIOU") 
    for alphabet in user_input: 
        if alphabet in vowel: 
            vcount = vcount + 1 
    return vcount 

def consonant_count(user_input):                                                                                        # creates a function for number 3
    '''
    Counts and prints the amount of consonants in the input

    Args:
        user_input: What the user puts as their name

    Returns:
        ccount: The amount of consonants in the input

    Raises:
        None
    '''
    ccount = 0 
    consonant = list("qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM") 
    for alphabet in user_input: 
        if alphabet in consonant: 
            ccount = ccount + 1 
    return ccount 

def lower_converter(user_input):                                                                                        # creates a function for number 8
    '''
    Converts and prints all characters in the input as lowercase

    Args:
        user_input: What the user puts as their name

    Returns:
        result: The input fully lowercase

    Raises:
        None
    '''
    result = ""
    for char in user_input:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

def upper_converter(user_input):                                                                                        # creates a function for number 9
    '''
    Converts and prints all characters in the input as uppercase

    Args:
        user_input: What the user puts as their name

    Returns:
        result: The input fully uppercase

    Raises:
        None
    '''
    result = ""
    for char in user_input:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

def shuffler(user_input):                                                                                               # creates a function for number 10
    '''
    Shuffles all characters in the input and prints a newly shuffled version of the input

    Args:
        user_input: What the user puts as their name

    Returns:
        result: The input fully shuffled

    Raises:
        None
    '''
    import random
    result = ""
    index = [i for i in range(len(user_input))]
    while index:
        random_index = random.randint(0, len(index) - 1)
        selected_index = index.pop(random_index)
        result += user_input[selected_index]
    return result

def first_palindrome(user_input):                                                                                       # creates a function for number 11
    '''
    Prints True or False depending on if the first word of the input is a palindrome

    Args:
        user_input: What the user puts as their name

    Returns:
        boolean : Whether or not the first word is a palindrome (True or False)

    Raises:
        None
    '''
    first = user_input.split(" ")
    first = user_input[0]
    if first == first[::-1]:
        return True
    else:
        return False

def sorted_name(user_input):                                                                                            # creates a function for number 12
    '''
    Prints a sorted list of all the characters in the input

    Args:
        user_input: What the user puts as their name

    Returns:
        char_list: A sorted list of all characters

    Raises:
        None
    '''
    char_list = []
    for char in user_input:
        if char != " ":
            char_list.append(char)
    for i in range(len(char_list)):
        for j in range(0, len(char_list) - i - 1):
            if char_list[j] > char_list[j + 1]:
                char_list[j], char_list[j + 1] = char_list[j + 1], char_list[j]
    joiner = ''.join(char_list)
    return joiner

def get_initials(user_input):                                                                                           # creates a function for number 13
    '''
    Prints the initials of the input

    Args:
        user_input: What the user puts as their name

    Returns:
        initials: The initials of the input

    Raises:
        None
    '''
    initials = ''
    start = True
    for char in user_input:
        if char == ' ':
            start = True
        elif start:
            initials += char
            start = False
    return initials

def contains_title(user_input):                                                                                         # creates a function for number 14
    '''
    Prints True or False depending on if the name contains a title

    Args:
        user_input: What the user puts as their name

    Returns:
        start: Whether or not the input contains a title (True or False)

    Raises:
        None
    '''
    titles = ["Mr.", "Ms.", "Mrs.", "Dr.", "Prof.", "Sir", "Lady", "Esq", "Duke", "Ph.d"]
    for title in titles:
        if title in user_input:
            return True
        else:
            return False

def main():                                                                             
    user_input = input("type out your name (first, middle, and last): ")                
    
    while True: 
        print("1. Reverse and display")                                                                                 # print the statement (same for all 16 print statements)                                                
        print("2. Determine the number of vowels")                                      
        print("3. Consonant frequency")                                                 
        print("4. Return first name")                                                   
        print("5. Return last name")                                                    
        print("6. Return middle name(s)")                                              
        print("7. Return boolean if last name contains a hyphen")                      
        print("8. Function to convert to lowercase")                             
        print("9. Function to convert to uppercase")                                 
        print("10. Modify array to create a random name (mix up letters)")           
        print("11. Return boolean if first name is a palindrome")                  
        print("12. Return full-name as a sorted array of characters")                  
        print("13. Make initials from name")                                           
        print("14. Return boolean if name contains a title/distinction")           
        print("15. Determine whether amount of letters is odd or even")            
        print("16. Exit")                                                     

        user_pick = input("now pick a number (1-16): ")                                                                 # creates the variable "user_pick" and tells the user the statement

        while True:                                                                                                     # creates a loop
            numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]                                    
            if user_pick not in numbers:                                                                                # if user inputs something that isn't a number 1-16
                print("invalid response")                                     
                user_pick = input("pick a valid number (1-16): ")                                                       # ask the user to pick a valid input
                continue                                                                                                # go back to beginning of loop 
            else:                                                                                                       # if the input is a number 1-16
                break                                                                                                   # ends the loop

        if user_pick == "1":                                                                                            # if user picks 1
            reverse = user_input[::-1]                                      
            print(reverse)                                                                                              # print the input reversed

        elif user_pick == "2":                                                                                          # if user picks 2
            vcount = vowel_count(user_input)                                      
            print("number of vowels: ", vcount)                                                                         # print the vowel count

        elif user_pick == "3":                                                                                          # if user picks 3
            ccount = consonant_count(user_input)                                       
            print("number of consonants: ", ccount)                                                                     # print the consonant count

        elif user_pick == "4":                                                                                          # if user picks 4
            first = user_input.split(" ")                                                                               # split the input into seperate words
            print(first[0])                                                                                             # print the first word of the input

        elif user_pick == "5":                                                                                          # if user picks 5
            last = user_input.split(" ")                                                                                
            print(last[-1])                                                                                             # print the last word of the input

        elif user_pick == "6":                                                                                          # if user picks 6
            middle = user_input.split(" ")                                   
            print(' '.join(middle[1:-1]))                                                                               # print everything but the first and last word of the input

        elif user_pick == "7":                                                                                          # if user picks 7
            boolean = False                                                                                             # set the variable boolean to false
            last_name = user_input.split(" ")                                      
            last_hyphen = last_name[-1]                                                                                 # take the last word of the input
            for i in range(len(last_hyphen)):                                                                           # loop through each index in the last word of the input
                hyphen = list(last_hyphen)                                                                              # convert "last_hyphen" into a list and assign it the variable "hyphen"
                if hyphen[i] == "-":                                                                                    # if there is a hyphen
                    boolean = True                                                                                      # change the variable boolean to true
                    break                                                                                               # exit the for loop
            print(boolean)                                                                                              # print the variable boolean (true or false)

        elif user_pick == "8":                                                                                          # if user picks 8
            input_string = user_input                                                                                   # store the input into a variable to be processed
            lowercase_string = lower_converter(input_string)                                                            # convert the input to lowercase using the "lower_converter" function
            print(lowercase_string)                                                                                     # print the input as lowercase
        
        elif user_pick == "9":                                                                                          # if user picks 9
            input_string = user_input                                     
            uppercase_string = upper_converter(input_string)                                       
            print(uppercase_string)                                                                                     # print the input as uppercase

        elif user_pick == "10":                                                                                         # if user picks 10
            input_string = user_input                                  
            shuffled_input = shuffler(input_string)                                       
            print(shuffled_input)                                                                                       # print the shuffled input

        elif user_pick == "11":                                                                                         # if user picks 11
            input_string = user_input                                  
            result = first_palindrome(input_string)                                 
            print(result)                                                                                               # print whether or not the first word in the input is a palindrome
        
        elif user_pick == "12":                                                                                         # if user picks 12
            input_string = user_input                                 
            sorted_charlist = sorted_name(input_string)                                        
            print(sorted_charlist)                                                                                      # print the sorted list

        elif user_pick == "13":                                                                                         # if user picks 13
            print("initials:", get_initials(user_input))                                                                # print the initials

        elif user_pick == "14":                                                                                         # if user picks 14
            input_string = user_input                        
            result = contains_title(input_string)                       
            print(result)                                                                                               # print whether or not the input contains a title

        elif user_pick == "15":                                                                                         # if user picks 15
            count = 0                                                                                                   # set count to 0
            for char in user_input:                                                                                     # loops through every character in the input
                if char != ' ':                                                                                         # if the character is not a space
                    count += 1                                                                                          # add 1 to count
            if count % 2 == 0:                                                                                          # check if the total number is even
                print("the amount of letters is even")                                  
            else:                                                                                                       # if odd
                print("the amount of letters is odd")                                  
        
        elif user_pick == "16":                                                                                         # if user picks 16
            quit()                                                                                                      # end the code
        
        while True:                                                                                                     # creates a loop                                     
            change_name = input("do you want to change your name?: ")                                                   # asks user if they want to change name                             
            change_name = change_name[0]                                                                                # only takes first letter of input                                
            if change_name == "Y" or change_name == "y":                                                                # if input starts with uppercase or lowercase y                                   
                main()                                                                                                  # go to start of main function                
            elif change_name == "N" or change_name == "n":                                                              # if input starts with uppercase or lowercase n                         
                break                                                                                                   # end loop                  
            else:                                                                                                       # anything else
                print("invalid response")                                                                               # print the statement
                continue                                                                                                # goes to start of loop

main()                                                                                                                  # calls the main function
