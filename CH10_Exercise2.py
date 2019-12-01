# Ryan Smith
# Python for Everybody Coursera

# Exercise 2: This program counts the distribution of the hour of the day
# for each of the messages. You can pull the hour from the “From” line
# by finding the time string and then splitting that string into parts using
# the colon character. Once you have accumulated the counts for each
# hour, print out the counts, one per line, sorted by hour as shown below.

f = open(input("Enter file name: "))

counts = {}

for line in f:
    if line.startswith("From"):
        words = line.split()
        if len(words) >= 6:
            time = words[5].split(":")
            counts[time[0]] = counts.get(time[0], 0) + 1
        else:
            continue

hourList = []

for key, value in counts.items():
    hourList.append((key, value))

hourList.sort()

for hour, count in hourList:
    print(hour, count)

f.close()
