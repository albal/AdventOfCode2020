import re

with open('input16.txt', 'r') as file:
    data = file.read().split("\n\n")

rules = data[0].split("\n")
myticket = data[1].split("\n")[1]
othertickets = data[2].split("\n")[1:]
invalidvalues = []
validvalues = []
validtickets = []

for ticket in othertickets:
    invalid = False
    for value in ticket.split(","):
        for rule in rules:
            min1, max1, min2, max2 = re.findall(r".(\d+)-(\d+) or (\d+)-(\d+)", rule)[0]
            val = int(value)
            if int(min1) <= val <= int(max1) or int(min2) <= val <= int(max2):
                validvalues.append(val)
                invalid = False
                break
            else:
                invalid = True
        if invalid:
            invalidvalues.append(val)
    if not invalid:
        validtickets.append(ticket)

print("Valid Tickets:", len(validtickets), "/", len(othertickets), " Invalid Sum:", sum(invalidvalues))
