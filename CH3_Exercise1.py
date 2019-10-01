# Ryan Smith
# Python for Everybody Coursera

# Exercise 1: Rewrite your pay computation to give the employee 1.5
# times the hourly rate for hours worked above 40 hours

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

if hours <= 40:
    pay = hours * rate
    print("Pay: ${:.2f}".format(pay))
else:
    pay = 40 * rate
    pay += (hours - 40) * (rate * 1.5)
    print("Pay: ${:.2f}".format(pay))
