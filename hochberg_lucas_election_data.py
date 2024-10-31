# Name: Lucas Hochberg
# Description: A program that prints all of the words, as well as their frequency, of the kamala/trump acceptance speeches. Also gets rid of punctuation, as well as all of the useless words, so the code only prints words that will help you understand what he is saying.
# Bugs: If you run the code more than once, the words add up onto each other in the csv
# Features: None
# Sources: Python for Everybody
# Log: 1.0

import string                                       # gives access to the string function

uwords = ["for", "as", "to", "my", "you", "an,", "me", "and", "i", "when", "the", "we", "an", "have", "with", "is", "will", "are", "be", "who", "has", "in", "our", "that", "was", "but", "of", "know", "she", "would", "a", "it", "they", "us", "he", "not", "their", "on", "this", "his", "one", "all", "so", "about", "together", "your", "going", "everyone", "had", "her", "own", "now", "from", "up", "always", "at", "let", "like", "them", "by", "how", "make", "do", "never", "those", "there", "were", "because", "behalf", "out", "back", "what", "where", "its", "more", "than", "ever", "new", "vox", "also", "last", "year", "say", "most", "trumps", "percent", "years", "other", "very", "way", "any", "life", "does", "tonight", "many", "even", "been", "time", "if", "want", "no", "made", "down", "being", "into", "or", "after", "just", "again", "which", "put", "am", "bad", "same", "first", "can", "these", "every", "right", "greatest", "take", "must", "stop", "dont", "much", "im", "american", "americas", "laws", "supported", "stop", "countries", "start"]                                         # creates a list of all the words I don't wan't to be printed

fhand = open("trump_new.txt", "r")
counts = dict()
for line in fhand:
    # iterates through every word in the text and gets rid of all punctuation, all capitalization, all words in the list, and measures the frequency of all the words
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
    # skips the word if it is inside the list, and if it is not part of the list, it gets its frequency tallies
        if word in uwords:
            continue
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

file = open("election_words.csv", "w")                                      # opens a new csv file to store all of the words that match the criteria
for key, value in counts.items():
# if the frequency of a word is less than 5, gets rid of it
    if value > 5:
        file.write(key + ", " + str(value) + "\n")

print(counts)                                       # prints all words plus its frequency in the csv
