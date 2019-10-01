# Ryan Smith
# Python for Everybody Coursera

# Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to
# Fahrenheit, and print out the converted temperature.

celsius = float(input("Enter temperature in celsius: "))
fahrenheit = celsius * (9 / 5) + 32
print("In fahrenheit that is {:.2f} degrees".format(fahrenheit))