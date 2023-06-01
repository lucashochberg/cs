# Name: Lucas Hochberg
# Date: 5/19/23
# Description: Acts as a calculator that has 9 function: add, subtract, multiply, divide, exponent, sum, max, linear line, and quit
# Bugs: 
# Challenges: Create an "exponent" function / Create a "max" function / Create a "function" function / Ad to a "main" function
# Sources: Ms. Marciano, Henry Santangelo, Google

def add(a, b): # Creates an add function for 2 variables
    return (a + b) # Sends the function back to the user and adds the 2 variables

def subtract(a, b): # Creates a subtract function for 2 variables
    return a - b # Sends the function back to the user and subtracts the 2 variables

def multiply(a, b): # Creates a multiply function for 2 variables
    return a*b # Sends the function back to the user and multiplies the 2 variables

def div(a, b): # Creates a divide function for 2 variables
    if b == 0: # If the 2nd variable is 0
        return "cannot divide by zero" # Sends the function back to the user and tells them you cannot divide by 0
    return a / b # Sends the function back to the user and divides the 2 variables

def exponent(a, b): # Creates an exponent function for 2 variables
    return a ** b # Sends the function back to the user and multiples the variable the amount of times that is chosen for the exponent

def sum(l): # Creates a sum function
    s = 0 # Sets the sum = to 0
    for i in l: # Go through each item  in the list
        s += i #  Add the item to the sum
    return # Sends the function back to the user and creates a sum for the numbers

def max(l): # Creates a max function
    m = None # Sets m = to no value
    for i in l: # Go through each item in the list
        if m == None or i > m: # If the current max is None or if it is less than the item
            m = i # Set the max to the current item
    return m # Sends the function back to the user and creates a max based on all the numbers

def linear_line(m, b, x): # Creates a linear line function
    return m*x + b # Sends the function back to the user and creates a linear line based on the numbers they chose

def check_list(): # Creates a checklist function
    l = [] # Creates the list
    while True: # Creates a loop
        print(f"current list is {l}") # Prints what the current list is
        new_number = input("enter another number in the list or 'stop' to stop entering: ") # Asks the user to enter number or stop
        if new_number == 'stop': # If the user enters stop
            break # Terminates the loop
        try: # Allows for testing code for errors
            l.append(int(new_number)) # Add the new number to the list
        except ValueError: # If there is an error converting it to an integer
            print("invalid response") # Prints this message
    return l # return the final list with all integers
            

def check_int(): # Creates a check integer function
    while True: # Creates a loop
        num = input("enter an integer: ") # Asks the user to enter an integer

        try: # ALlows for testing code for errors
            return int(num) # return the number as an integer
        except ValueError: # If there was an issue converting the input to an integer
            print("please enter an integer") # Prints this message



def main(): # Creates a main function
    while True: # Creates a loop
        mode = input("what would you like to do 1. Add, 2 Subtract, 3 Multiply, 4 Divide, 5 Exponent, 6 Sum, 7 Max, 8 Linear Line, 9 Quit \n: ") # Asks the user what they would like to do
        
        if mode == "6": # If the user chooses 6
            l = check_list() # Create the list to sum
            print(sum(l)) # Prints the sum of the integers
            continue # Ends this part of the loop and continues to the next

        elif mode == "7": # If the user chooses 7
            l = check_list() # Creates the list to find the max of 
            print(max(l)) # Prints the max of the integers
            continue # Ends this part of the loop and continues to the next

        elif mode == "8": # If the user chooses 8
            print("the form of a linear line is y = mx + b") # Prints this message
            print("m value is ") # Prints this message
            m = check_int() # Creates the list to m
            print("b value is ") # Prints this message
            b = check_int() # Creates the list to b
            print("x point is ") # Prints this message
            x = check_int() # Creates the list to x
            print(linear_line(m, b, x)) # Prints the linear line
            continue # Ends this part of the loop and continues to the next

        elif mode == "9": # if the user chooses 9
            break # Terminates the loop

        a = check_int() # Get the first number of the operation
        b = check_int() # Get the second number of the operation

        if mode == "1": # If the user chooses 1
            print(add(a,b)) # Prints the integers added together
        elif mode == "2": # If the user chooses 2
            print(subtract(a, b)) # Prints the integers subtracted from eachother
        elif mode == "3": # if the user chooses 3
            print(multiply(a, b)) # Prints the ingeters multiplied together
        elif mode == "4": # If the user chooses 4
            print(div(a, b)) # Prints the integers divided from eachother
        elif mode == "5": # If the user chooses 5
            print(exponent(a, b)) # Prints the first integer to the power of the second integer
        
main() # Acts as a point of execution for any function