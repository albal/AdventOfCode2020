import io


with open('input02.txt', 'r') as file:
    data = file.readlines()

for line1 in data:
    for line2 in data:
        for line3 in data:
            if int(line1) + int(line2) + int(line3) == 2020:
                print(int(line1), "+", int(line2), "+", int(line3), "=", int(line1) + int(line2) + int(line3))
                print(int(line1) * int(line2) * int(line3))
                exit()
