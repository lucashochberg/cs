import string

uwords = ["for", "as", "to", "my", "you", "an,", "me", "and", "i", "when", "the", "we", "an", "have", "with", "is", "will", "are", "be", "who", "has", "in", "our", "that", "was", "but", "of", "know", "she", "would", "a", "it", "they", "us", "he", "not", "their", "on", "this", "his", "one", "all", "so", "about", "together", "your", "going", "everyone", "had", "her", "own", "now", "from", "up", "always", "at", "let", "like", "them", "by", "how", "make", "do", "never", "those", "there", "were", "because", "behalf", "out", "back", "what", "where", "its", "more", "than", "ever", "new", "vox", "also", "last", "year", "say", "most", "trumps", "percent", "years", "other", "very", "way", "any", "life", "does", "tonight", "many", "even", "been", "time", "if", "want", "no", "made", "down", "being", "into", "or", "after", "just", "again", "which", "put", "am", "bad", "same", "first", "can", "these", "every", "right", "greatest", "take", "must", "stop", "dont", "much", "im", "american", "americas", "laws", "supported", "stop", "countries", "start"]

fhand = open("trump_new.txt", "r")
counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word in uwords:
            continue
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

file = open("election_words.csv", "w")
for key, value in counts.items():
    if value > 5:
        file.write(key + ", " + str(value) + "\n")

print(counts)