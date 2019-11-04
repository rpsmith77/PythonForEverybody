# Ryan Smith
# Python for Everybody Coursera

# Exercise 5: This program records the domain name (instead of the
# address) where the message was sent from instead of who the mail came
# from (i.e., the whole email address). At the end of the program, print
# out the contents of your dictionary.

f = open(input("Enter file name: "))

domains = {}

for line in f:
    if line.startswith("From"):
        splitLine = line.split()
        emailAddress = splitLine[1]
        emailAddress = emailAddress.split("@")
        domain = emailAddress[1]
        if domain in domains:
            domains[domain] += 1
        else:
            domains[domain] = 1

print(domains)

f.close()
