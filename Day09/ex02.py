data = []

with open('input09.txt', 'r') as file:
    for line in file:
        data.append(int(line.strip()))

target = 26134589
# target = 127


def test_seq(sequence):
    if sum(sequence) == target:
        print("Sequence:", sequence)
        print("Min:", min(sequence), "Max:", max(sequence), "Sum:", min(sequence) + max(sequence))
        exit(0)


for i in range(0, len(data)):
    for j in range(i + 1, len(data)):
        test_seq(data[i:j])

print("Nothing found")
