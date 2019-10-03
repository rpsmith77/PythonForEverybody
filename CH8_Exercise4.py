# Ryan Smith
# Python for Everybody Coursera

# Exercise 4: Download a copy of the file www.py4e.com/code3/romeo.txt.
# Write a program to open the file romeo.txt and read it line by line. For
# each line, split the line into a list of words using the split function.
# For each word, check to see if the word is already in a list. If the word
# is not in the list, add it to the list. When the program completes, sort
# and print the resulting words in alphabetical order.

f = open(input("Enter file name: "))

result = []

for line in f:
    words = line.split()

    for word in words:
        if word in result:
            continue
        else:
            result.append(word)

result.sort()
for i in result:
    print(i, end=", ")
print(result)

f.close()