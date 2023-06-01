# Name: Lucas Hochberg
# Date: 3/1/2023
# Description: Once you ask a question, the program will give you a response saying either Yes, No, Maybe, or Ask again later. If you tell the program to stop then it will end.
# Bugs: I put both stop and STOP as an end program response and it crashed the code.
# Challenges: Getting a random response from the question because everytime I would ask the program a question it would crash.
# Sources: Zach Bostock

import random
responses = ["Yes", "No", "Maybe", "Ask again later"]
print ("Welcome to the magic 8 ball. Type 'quit' to exit")
while True:
    question = input("Please Input your question (type STOP to end program): ")
    if question.upper() == "STOP":
        print("Program has now ended")
        break
    else:
        print(random.choice(responses))
