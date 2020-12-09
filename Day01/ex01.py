import io


with open('input01.txt', 'r') as file:
    data = file.readlines()

for line1 in data:
    for line2 in data:
        if int(line1) + int(line2) == 2020:
            print(int(line1), "+", int(line2), "=", int(line1) + int(line2))
            print(int(line1) * int(line2))
            exit()
