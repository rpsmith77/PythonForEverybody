# Ryan Smith
# Python for Everybody Coursera

# Exercise 3: Write a program that reads a file and prints the letters
# in decreasing order of frequency. Your program should convert all the
# input to lower case and only count the letters a-z. Your program should
# not count spaces, digits, punctuation, or anything other than the letters
# a-z. Find text samples from several different languages and see how
# letter frequency varies between languages. Compare your results with
# the tables at https://wikipedia.org/wiki/Letter_frequencies.

f = open(input("Enter file name: "))

letter_map = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0,
              "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0,
              "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0,
              "w": 0, "x": 0, "y": 0, "z": 0, }

for lines in f:
    line = lines.split()
    for words in line:
        for letter in words:
            if letter.isalpha():
                letter = letter.lower()
                letter_map[letter] += 1

print(*letter_map.items())

f.close()
