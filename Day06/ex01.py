with open('input06.txt', 'r') as file:
    data = file.read().split('\n\n')

answers = 0

for group in data:
    group_answers = set()
    for line in group.strip():
        if line != '\n':
            group_answers.add(line)
    for item in group_answers:
        answers += 1

print("Yes answers:", answers)