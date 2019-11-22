# Ryan Smith
# Python for Everybody Coursera

# Exercise 1: Revise a previous program as follows: Read and parse the
# “From” lines and pull out the addresses from the line. Count the number of
# messages from each person using a dictionary. After all the data has been
# read, print the person with the most commits by creating a list of (count,
# email) tuples from the dictionary. Then sort the list in reverse order and
# print out the person who has the most commits.

f = open(input("Enter file name: "))

emailAddresses = {}

for line in f:
    if line.startswith("From"):
        splitLine = line.split()
        emailAddress = splitLine[1]
        if emailAddress in emailAddresses:
            emailAddresses[emailAddress] += 1
        else:
            emailAddresses[emailAddress] = 1

listOfTuples = []

for key, value in emailAddresses.items():
    listOfTuples.append((key, value))
# cite: https://www.geeksforgeeks.org/python-program-to-sort-a-list-of
# -tuples-by-second-item/ For showing me how to sort a list of tuples by the
# second item in the tuple
listOfTuples.sort(key=lambda x: x[1], reverse=True)

print(*listOfTuples[0])

f.close()
