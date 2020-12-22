import re

with open('input19.txt', 'r') as file:
    data = file.read().split("\n\n")

rules_input = data[0].split("\n")
lines = data[1].split("\n")

rules = {}
for rule in rules_input:
    k, v = rule.split(": ")
    rules[int(k)] = v


def makerule(rule):
    if '"' in rules[rule]:
        return '(' + eval(rules[rule]) + ')'

    result = []

    for part in rules[rule].split(' | '):
        inner = ""
        for val in part.split():
            inner += ''.join(makerule(int(val)))
        result.append(inner)

    return "(" + "|".join(result) + ")"


full_rule = "^" + makerule(0) + "$"
print("Full rule:", full_rule)

count = 0
for line in lines:
    if re.match(full_rule, line):
        count += 1

print("Answer:", count)
