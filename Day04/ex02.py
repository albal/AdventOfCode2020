import re

with open('input04.txt', 'r') as file:
    data = file.readlines()

passports = []
# fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
temp = ""
valid = 0

rules = {
    'byr': lambda r: 1920 <= int(r) <= 2002,
    'iyr': lambda r: 2010 <= int(r) <= 2020,
    'eyr': lambda r: 2020 <= int(r) <= 2030,
    'hcl': lambda r: re.match(r'^#[\da-f]{6}$', r),
    'ecl': lambda r: r in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda r: re.match(r'^\d{9}$', r),
    'hgt': lambda r: (r[-2:] == 'in' and 59 <= int(r[:-2]) <= 76) or (r[-2:] == 'cm' and 150 <= int(r[:-2]) <= 193)
}

for line in data:
    temp += line.strip('\n') + " "
    if line == '\n':
        passports.append(temp.strip())
        temp = ""

passports.append(temp.strip())

for passport in passports:
    print(passport + "    ", end='')
    items = dict(entry.split(':') for entry in passport.split(' '))
    if all(field in items for field in rules.keys()) and all(rules[field](items[field]) for field in rules.keys()):
        valid += 1
        print("********* VALID *********")
    else:
        print("XXXXXXXX INVALID XXXXXXXX")


print("Valid passports:", valid)

