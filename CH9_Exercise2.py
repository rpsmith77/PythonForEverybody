# Ryan Smith
# Python for Everybody Coursera

# Exercise 2: Write a program that categorizes each mail message by
# which day of the week the commit was done. To do this look for lines
# that start with “From”, then look for the third word and keep a running
# count of each of the days of the week. At the end of the program print
# out the contents of your dictionary (order does not matter).

f = open(input("Enter file name: "))

week = {}

for line in f:
    if line.startswith("From"):
        splitLine = line.split()
        day = splitLine[2]
        if day in week:
            week[day] += 1
        else:
            week[day] = 1

print(week)

f.close()
