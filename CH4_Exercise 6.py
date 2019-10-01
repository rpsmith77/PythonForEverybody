# Ryan Smith
# Python for Everybody Coursera

# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay
# which takes two parameters
# (hours and rate).
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

def computePay(time, payRate):
    if time <= 40:
        print("Pay: ${:.2f}".format(time * payRate))
    else:
        pay = (40 * payRate) + ((time - 40) * (payRate * 1.5))
        print("Pay: ${:.2f}".format(pay))

try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    computePay(hours, rate)

except:
    print("Error, please enter numeric input")
