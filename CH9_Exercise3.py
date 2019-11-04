# Ryan Smith
# Python for Everybody Coursera

# Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many
# messages have come from each email address, and print the dictionary.

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

print(emailAddresses)

f.close()
