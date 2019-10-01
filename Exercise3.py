# Ryan Smith
# Python for Everybody Coursera

# Exercise 3: Write a program to prompt the user for hours and rate per
# hour to compute gross pay.

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
print("Pay: ${:.2f}".format(hours * rate))