# Ryan Smith
# Python for Everybody Coursera

# Exercise 7: Rewrite the grade program from the previous chapter using
# a function called computegrade that takes a score as its parameter and
# returns a grade as a string.
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# Enter score: 0.95
# A
# Enter score: perfect
# Bad score
# Enter score: 10.0
# Bad score
# Enter score: 0.75
# C
# Enter score: 0.5
# F
# Run the program repeatedly to test the various different values for input.

def computeGrade(score):
    if score > 1 or score < 0:
        print("Bad score")
    elif score >= .9:
        print("A")
    elif score >= .8:
        print("B")
    elif score >= .7:
        print("C")
    elif score >= .6:
        print("D")
    else:
        print("F")


score = input("Enter Score: ")
try:
    score = float(score)
    computeGrade(score)

except:
    print("Bad Score")
