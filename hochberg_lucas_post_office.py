# Name: Lucas Hochberg
# Log: 1.1
# Bonus Features: None
# Bugs: When something unmailable is entered into the data, instead of printing "unmailable," it prints "invalid response." When an invalid zipcode is entered, the code states the zipcode is invalid and ends but is not clear.
# Description: Determines the price of mailing something based on its length, height, and thickness. Also adds extra cost based on how many zones it needs to pass through.


def get_zone(zipcode): # creates the function "get_zone" and creates the variable "zipcode"
    '''
    Creates a way to find the zone by finding the zipcode

    Args:
        zipcode (int): The starting and ending number for which the mail is being delivered or sent

    Returns:
        int: The zone in which the the mail is being sent and delivered

    Raises:
        ValueError: If the number has a decimal, is negative, or contains more than 6 numbers 
    '''
    # the code below creates and stores the variables that are apart of the function above
    if 1 <= zipcode <= 6999: 
        return 1 
    elif 7000 <= zipcode <= 19999: 
        return 2 
    elif 20000 <= zipcode <= 35999: 
        return 3 
    elif 36000 <= zipcode <= 62999: 
        return 4 
    elif 63000 <= zipcode <= 84999: 
        return 5 
    elif 85000 <= zipcode <= 99999: 
        return 6 
    elif 99999 < zipcode: 
        return None 

def get_type(length, height, thickness): # creates he function "get_type" and creates the variable "length," "height," and "thickness"
    '''
    Creates a way to figure out the mail type based on the length, height, and thickness

    Args:
        length (var): The length of the mail being sent
        height (var): The height of the mail being sent
        thickness (var): The thickness of the mail being sent

    Returns:
        var: The category in which the mail falls under

    Raises:
        Error: If the three variables don't fall under any of the mail categories
    '''
    # the code below stores the variables and mail categories that are defined above
    if length>=3.5 and length<=4.25 and height>=3.5 and height<=6 and thickness>=.007 and thickness<=.016: 
        return "postcard"
    elif length>4.25 and length<6 and height>6 and height<11.5 and thickness>=.007 and thickness<=.015: 
        return "large postcard" 
    elif length>=3.5 and length<=6.125 and height>=5 and height<=11.5 and thickness>.016 and thickness<.25: 
        return "envelope" 
    elif length>6.125 and length<24 and height>=11 and height<=18 and thickness>=.25 and thickness<=.5:
        return "large envelope" 
    elif length>=24 and height>18 and thickness>.5 and length+2*(height+thickness)<=84: 
        return "package" 
    elif length+2*(height+thickness)>=84 and length+2*(height+thickness)<=130: 
        return "large package"
    else: 
        return "unmailable" 

def get_cost(mail_type, distance): # creates the function "get_cost" and the variables "mail_type" and "distance"
    '''
    Creates a way to calculate price based on the functions above which calculated the mail category plus the amount of zones being crossed

    Args:
        mail_type (var): The category in which the mail falls under
        distance (var): The distance in which the mail travels (abs(zip1-zip2))

    Returns:
        var: The price to send the mail
    '''
    # the code below stores the variables and calculations used to find price, which is defined above
    if mail_type=="postcard": 
        return .20 + .03*(distance)
    elif mail_type=="large postcard": 
        return .37 + .03*(distance) 
    elif mail_type=="envelope": 
        return .37 + .04*(distance) 
    elif mail_type=="large envelope":
        return .6 + .05*(distance) 
    elif mail_type=="package": 
        return 2.95 + .25*(distance) 
    elif mail_type=="large package": 
        return 3.95 + .35*(distance) 

def main():                                         # creates the function "main" which serves as the starting point for the code
    while True:                                         # creates a loop
        print("welcome to the post office")                                         # prints the message inside the quotes
        data = input("enter data (length, height, thickness, zip1, zip2): ")                                        # prints the message inside the quotes and allows the user to respond
        dimensions = data.split(",")                                        # adds a comma in between each value printed

        length = float(dimensions[0])                                       # length is equal to the first variable in the list and turns it into a number
        height = float(dimensions[1])                                       # height is equal to the second variable in the list and turns it into a number
        thickness = float(dimensions[2])                                        # thickness is equal to the third variable in the list and turns it into a number
        zip1 = int(dimensions[3])                                       # zipcode 1 is equal to the fourth variable in the list and turns it into a number without a decimal
        zip2 = int(dimensions[4])                                       # zipcode 2 is equal to the fifth variable in the list ans turns it into a number without a decimal

        mail_type=get_type(length, height, thickness)                                       # in order to get the mail type, get length, height, and thickness
        distance = abs(get_zone(zip1) - get_zone(zip2))                                         # distance is equal to the absolute value of zipcode 1 minus zipcode 2
        price = get_cost(mail_type, distance)                                       # in order to get the cost, add the mail type plus the amount of zones crossed

        print("The total cost is: " + str("%.2f" %price).lstrip('0'))                                       # prints the message inside the quotes and shows the total price

        while True:                                         # creates a loop inside the first loop
            resp_again = input(" do you want to send another package? y/n: ")                                       # prints the message inside the quotes and allows the user to respond
            resp_again = resp_again.lower()                                         # makes it so lowercase letters are acceptable
            resp_again = resp_again[0]                                      # only takes the first letter of the response
            if resp_again == "y":                                       # if the first letter of the response is a y
                break                                       # goes to the beginning of the code
            elif resp_again == "n":                                         # if the first letter of the response is a n
                quit()                                      # end the code
            else:                                       # if it is not a y or a n
                print("invalid response")                                       # print the message inside the quotes
main()                                      # calls the function "main"
