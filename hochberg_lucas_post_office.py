# Name: Lucas Hochberg
# Log: 1.0
# Bonus Features: None
# Bugs: When something unmailable is entered into the data, instead of printing "unmailable," it prints "invalid response." When an invalid zipcode is entered, the code states the zipcode is invalid and ends but is not clear.
# Description: Determines the price of mailing something based on its length, height, and thickness. Also adds extra cost based on how many zones it needs to pass through.

def get_zone(zipcode): # creates the function "get_zone" and creates the variable "zipcode"
    if 1 <= zipcode <= 6999: # if the zipcode is greater than or equal to 1 and less than or equal to 6999
        return 1 # set the output equal to 1
    elif 7000 <= zipcode <= 19999: # if the zipcode is greater than or equal to 7000 and less than or equal to 19999
        return 2 # set the output equal to 2
    elif 20000 <= zipcode <= 35999: # if the zipcode is greater than or equal to 20000 and less than or equal to 35999
        return 3 # set the output equal to 3
    elif 36000 <= zipcode <= 62999: # if the zipcode is greater than or equal to 36000 and less than or equal to 62999
        return 4 # set the output equal to 4
    elif 63000 <= zipcode <= 84999: # if the zipcode is greater than or equal to 63000 and less than or equal to 84999
        return 5 # set the output equal to 5
    elif 85000 <= zipcode <= 99999: # if the zipcode is greater than or equal to 85000 and less than or equal to 99999
        return 6 # set the output equal to 6
    elif 99999 < zipcode: # if the zipcode is greater than 99999
        return None # set the output equal to nothing

def get_type(length, height, thickness): # creates he function "get_type" and creates the variable "length," "height," and "thickness"
    if length>=3.5 and length<=4.25 and height>=3.5 and height<=6 and thickness>=.007 and thickness<=.016: # if the length is greater than or equal to 3.5 and less than or equal to 4.25, and the height is greater than or equal to 3.5 and less than or equal to 6, and the thickness is greater than or equal to .007 and less than or equal to .016
        return "postcard" # set the output equal to "postcard"
    elif length>4.25 and length<6 and height>6 and height<11.5 and thickness>=.007 and thickness<=.015: # if the length is greater than 4.25 and less than 6, and the height is greater than 6 and less than 11.5, and the thickness is greater than or equal to .007 and less than or equal to .015
        return "large postcard" # set the output equal to "large postcard"
    elif length>=3.5 and length<=6.125 and height>=5 and height<=11.5 and thickness>.016 and thickness<.25: # if the length is greater than or equal to 3.5 and less than or equal to 6.125, and the height is greater than or equal to 5 and less than or equal to 11.5, and the thickness is greater than .016 and less than .25
        return "envelope" # set the output equal to "envelope"
    elif length>6.125 and length<24 and height>=11 and height<=18 and thickness>=.25 and thickness<=.5: # if the length is greater than 6.125 and less than 24, and the height is greater than or equal to 11 and less than or equal to 18, and the thickness is greater than or equal to .25 and less than or equal to .5
        return "large envelope" # set the output equal to "large envelope"
    elif length>=24 and height>18 and thickness>.5 and length+2*(height+thickness)<=84: # if the length is greater than or equal to 24, and the height is greater than 18, and the length plus 2 times the height plus thickness is less than or equal to 84
        return "package" # set the output equal to "package"
    elif length+2*(height+thickness)>=84 and length+2*(height+thickness)<=130: # if the length plus 2 times the height plus thickess is greater than or equal to 84 and less than or equal to 130
        return "large package" # set the output equal to "large package"
    else: # if the variable do not conform with any of the outputs
        return "unmailable" # set the output equal to nothing and print "unmailable"

def get_cost(mail_type, distance): # creates the function "get_cost" and the variables "mail_type" and "distance"
    if mail_type=="postcard": # if the mail type is equal to the output "postcard"
        return 0.20 + 0.03*(distance) # sets the price equal to .20 +.03 for every zone it passes
    elif mail_type=="large postcard": # if the mail type is equal to the output "large postcard"
        return 0.37 + 0.03*(distance) # sets the price equal to .37 +.03 for every zone it passes
    elif mail_type=="envelope": # if the mail type is equal to the output "envelope"
        return 0.37 + 0.04*(distance) # sets the price equal to .37 +.04 for every zone it passes
    elif mail_type=="large envelope": # if the mail type is equal to the output "large envelope"
        return 0.60 + 0.05*(distance) # sets the price equal to .60 +.05 for every zone it passes
    elif mail_type=="package": # if the mail type is equal to the output "package"
        return 2.95 + 0.25*(distance) # sets the price equal to 2.95 +.25 for every zone it passes
    elif mail_type=="large package": # if the mail type is equal to the output "large package"
        return 3.95 + 0.35*(distance) # sets the price equal to 3.95 +.35 for every zone it passes

def main(): # creates the function "main"
    while True: # creates a loop
        print("welcome to the post office") # prints the message inside the quotes
        data = input("enter data (length, height, thickness, zip1, zip2): ") # prints the message inside the quotes and allows the user to respond
        dimensions = data.split(",") # adds a comma in between each value printed

        length = float(dimensions[0]) # length is equal to the first variable in the list and turns it into a number
        height = float(dimensions[1]) # height is equal to the second variable in the list and turns it into a number
        thickness = float(dimensions[2]) # thickness is equal to the third variable in the list and turns it into a number
        zip1 = int(dimensions[3]) # zipcode 1 is equal to the fourth variable in the list and turns it into a number without a decimal
        zip2 = int(dimensions[4]) # zipcode 2 is equal to the fifth variable in the list ans turns it into a number without a decimal

        mail_type=get_type(length, height, thickness) # in order to get the mail type, get length, height, and thickness
        distance = abs(get_zone(zip1) - get_zone(zip2)) # distance is equal to the absolute value of zipcode 1 minus zipcode 2
        price = get_cost(mail_type, distance) # in order to get the cost, add the mail type plus the amount of zones crossed

        print("The total cost is: " + str(price)) # prints the message inside the quotes and shows the total price

        while True: # creates a loop
            resp_again = input(" do you want to send another package? y/n: ") # prints the message inside the quotes and allows the user to respond
            resp_again = resp_again.lower() # makes it so lowercase letters are acceptable
            resp_again = resp_again[0] # only takes the first letter of the response
            if resp_again == "y": # if the first letter of the response is a y
                break # goes to the beginning of the code
            elif resp_again == "n": # if the first letter of the response is a n
                quit() # end the code
            else: # if it is not a y or a n
                print("invalid response") # print the message inside the quotes

main() # calls the function "main"

