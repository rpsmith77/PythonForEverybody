# Ryan Smith
# Python for Everybody Coursera

# Exercise 2: Rewrite your pay program using try and except so that your
# program handles non-numeric input gracefully by printing a message
# and exiting the program. The following shows two executions of the
# program:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input

# Enter Hours: forty
# Error, please enter numeric input

while True:
    try:
        hours = float(input("Enter Hours: "))
        rate =float(input("Enter Rate: "))
        if hours <= 40:
            pay = hours * rate
            print("Pay: ${:.2f}".format(pay))
        else:
            pay = 40 * rate
            pay += (hours - 40) * (rate * 1.5)
            print("Pay: ${:.2f}".format(pay))

    except:
        print("Error, please enter numeric input")
        break