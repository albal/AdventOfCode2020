with open('input04.txt', 'r') as file:
    data = file.readlines()

passports = []
# fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
temp = ""
valid = 0

for line in data:
    temp += line.strip('\n')
    if line == '\n':
        passports.append(temp + " ")
        temp = ""

passports.append(temp + " ")

for passport in passports:
    count = 0
    for field in fields:
        if field in passport:
            count += 1
    if count == 7:
        valid += 1

print("Valid passports:", valid)

