# Ryan Smith
# Python for Everybody Coursera

# Exercise 4: Add code to the above program (Ch 9 Exercise 3) to figure out who has the # most messages in the file.
# After all the data has been read and the dictionary has been created, look through the dictionary using a maximum #
# loop (see Chapter 5: Maximum and minimum loops) to find who has # the most messages and print how many messages the
# person has.

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

largestCount = None
largestEmailAddress = None

for key, value in emailAddresses.items():
    if (largestCount == None) or (value > largestCount):
        largestCount = value
        largestEmailAddress = key

print(largestEmailAddress, largestCount)

f.close()