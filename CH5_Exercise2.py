# Ryan Smith
# Python for Everybody Coursera

# Exercise 2: Write another program that prompts for a list of numbers
# as in exercise 1 and at the end prints out both the maximum and minimum of
# the numbers instead of the average.

total = 0
count = 0
i = 0
n = ""
sortList = []

while i == 0:
    n = input("Enter a number: ")

    if n.isdigit():
        total += int(n)
        sortList.append(n)
        count += 1
    elif n == "done":
        sortList.sort()
        print(str(total), str(count), sortList[0], sortList[count-1])
        i = 1
    else:
        print("Invalid input")

