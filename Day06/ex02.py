with open('input06.txt', 'r') as file:
    data = file.read().split('\n\n')

answers = 0

for group in data:
    sets = []
    lines = group.split('\n')
    for answer in lines:
        sets.append(set(answer))
    answers += len(set.intersection(*sets))

print("Answers: ", answers)


