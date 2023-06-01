# Name: Lucas Hochberg
# Date: 4/15/2023
# Description: Creates a password keeper for any website, username and password and stores them for later use
# Bugs: I can't figure out how to add a space between the different entries in the spreadsheet/It was hard to consistently get the spreadsheet to work/Whenever I added a new option to the code, it was hard to stop the entire code from breaking
# Challenges: Allows the user to access a specific website, username, and password/Allows the user the change usernames and passwords/Stores the list of websites with their username and password into a spreadsheet
# Sources: Ms. Marciano, Zach Bostock, Noah Sokol, Henry Santangelo

websites = [] # Creates an index for websites
usernames = [] # Creates an index for usernames
passwords = [] # Creates an index for passwords

website_data_file = open("websites.csv") # Opens the index
for line in website_data_file.readlines(): # load the data
    line = line.rstrip() # Removes unnecessary characters
    data = line.split(",") # # Splits the line
    websites.append(data[0]) # Adds the data of the websites to the index
    usernames.append(data[1]) # Adds the data of the usernames to the index
    passwords.append(data[2]) # Adds the data of the password to the list
website_data_file.close() # Closes the index

while True: # Creates a loop
    mode = input("what would you like to do? add entry/see history/see one entry/change entry/exit: ") # Asks the user what they would like to do
    if mode.lower() == "exit": # The user can use lowercase or uppercase when typing exit
        website_data_file = open("websites.csv", "w") # Open the website spreadsheet
        lines = [] # Shows the items that were added to the index
        for index in range(len(websites)): # Generates an index
            lines.append(f"{websites[index]},{usernames[index]},{passwords[index]}") #Adds website, username, and pasword to index
        website_data_file.writelines(lines) # Adds the items in the index to a list
        break # End
    elif mode.lower() == "add entry": # User can use lowercase or uppercase when typing add entry
        web = input("website:") # Asks the user what the name of the website is
        if web in websites: # If the website is in the index
            print("website already in index please change it instead: ") # Print the message
            continue # Keeps going on in the code
        user = input("username: ") # Asks the user to add a username for the website
        pwd = input("password: ") # Asks the user to add a password for the website
        websites.append(web) # Adds the website to the index
        usernames.append(user) # Adds the username to the index
        passwords.append(pwd) # Adds the password to the index
    elif mode.lower() == "see history": # User case use lowercase or uppercase when typing see history
        if len(websites) == 0: # If the user has not typed a website yet
            print("no history available") # Print the message
        else: # Other
            for index in range(len(websites)): # Generates the index
                print(f"website: {websites[index]}") # Shows the history of websites
                print(f"username: {usernames[index]}") # Shows the history of usernames
                print(f"password: {passwords[index]}") # Shows the history of passwords
    elif mode.lower() == "change entry": # User can use lowercase or uppercase when typing change entry
        web = input("website: ") # Asks the user when website they want to change
        if web not in websites: # If website is not in the index
            print("website not in websites") # Print the message
        else: # Anything else
            index = websites.index(web) # If the website is in the index
            user = input("new username: ") # User types a new username
            pwd = input("new password: ") # User types a new password
            usernames[index] = user # Adds new username to the index
            passwords[index] = pwd # Adds new password to the index
            print("changed entry successfully") # Print the message
            print(f"website: {websites[index]}") # Shows the website
            print(f"username: {usernames[index]}") # Shows the new username to the website
            print(f"password: {passwords[index]}") # Shows the new password to the website
    elif mode.lower() == "see one entry": # User can use lowercase or uppercase when typing see one entry
        web = input("website: ") # Asks the user what website they want to see
        if web not in websites: # If website is not in the index
            print("website not in websites") # Print the message
        else: # Other
            index = websites.index(web) # Shows the index to the website
            print(f"website: {websites[index]}") # Shows the website
            print(f"username: {usernames[index]}") # Shows the username to the website
            print(f"password: {passwords[index]}") # Shows the password to the website
    else: # Other
        print("invalid") # Print the message