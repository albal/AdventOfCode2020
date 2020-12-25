with open('input22.txt', 'r') as file:
    data = file.read().split("\n\n")


def read_data(input_data):
    output = []
    for c, val in enumerate(input_data.split()):
        if c > 1:
            output.append(int(val))
    return output


def calc_score(scores):
    multi = len(scores)
    total = 0
    for val in scores:
        total += val * multi
        multi -= 1
    return total


player1 = read_data(data[0])
player2 = read_data(data[1])

while len(player1) > 0 and len(player2) > 0:
    p1 = player1.pop(0)
    p2 = player2.pop(0)

    if p1 > p2:
        player1.append(p1)
        player1.append(p2)
    else:
        player2.append(p2)
        player2.append(p1)

if len(player1) > len(player2):
    print("Score:", calc_score(player1))
else:
    print("Score:", calc_score(player2))
