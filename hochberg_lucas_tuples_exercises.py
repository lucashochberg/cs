# Name: Lucas Hochberg
# Log: 1.0
# Bonus Features: None
# Bugs: None
# Description: Outputs the three tuples exercises

user_pick = input("which exercise do you want to output (1/2/3): ")

if user_pick == "1":
    from collections import defaultdict
    file_name = (r"c:\Users\lhochberg26\Documents\CS Stuff\Computer Science\CS2\tuple_file_short.txt")
    email_counts = defaultdict(int)                                                             # creates a dictionary to store the email count

    with open(file_name, 'r') as file:                                                          # opens the file and processes each line
        for line in file:
            if line.startswith("From "):                                                        # looks for lines starting with "From " to extract
                parts = line.split()
                email = parts[1]                                                                # email is the second word in the line
                email_counts[email] += 1

    most_common_email = None                                                                    # finds the email with the highest count
    highest_count = 0                                                                           # starts the highest count at 0

    for email, count in email_counts.items():
        if count > highest_count:
            most_common_email = email
            highest_count = count

    print(f"{most_common_email} {highest_count}")                                               # prints the email and its count

if user_pick == "2":
    file_name = r"c:\Users\lhochberg26\Documents\CS Stuff\Computer Science\CS2\tuple_file_short.txt"
    hour_counts = {}                                                                            # create an empty dictionary to store hour count

    with open(file_name) as f:
        for line in f:
            if line.startswith("From "):                                                        # only process lines that start with "From "
                words = line.split()                                                            # split the line into words
                if len(words) > 5:                                                              # ensure there is enough data to get time
                    time_str = words[5]                                                         # extract time
                    hour = time_str.split(":")[0]                                               # split time with colon to get the hour
                    if hour in hour_counts:                                                     # count occurences of each hour
                        hour_counts[hour] += 1
                    else:
                        hour_counts[hour] = 1

    if hour_counts:                                                                             # after processing, sort and print results
        for hour in sorted(hour_counts.keys()):
            print(hour, hour_counts[hour])

if user_pick == "3":
    import string

    letter_count = {letter: 0 for letter in string.ascii_lowercase}                             # create a dictionary to store letter count
    file_name = r"c:\Users\lhochberg26\Documents\CS Stuff\Computer Science\CS2\tuple_file_short.txt"

    with open(file_name, 'r') as f:                                                             # open and process each line of file
        for line in f:
            line = line.lower()
            for char in line:
                if char in string.ascii_lowercase:                                              # check if character is a letter
                    letter_count[char] += 1

    sorter_letters = sorted(letter_count.items(), key = lambda x: x[1], reverse = True)         # sort dictionary by frequency in descending order

    for letter, count in sorter_letters:
        if count > 0:
            print(f"{letter}: {count}")                                                         # print the letters and their frequencies