from copy import deepcopy

with open('input11.txt', 'r') as file:
    data = [list(line.strip()) for line in file]

padding = 1


# Pad data so we don't have to worry about edges and corners
def pad(seats):
    new_data = []
    for line in seats:
        chars = ["."] * padding
        new_data.append(chars + line + chars)  # Pad either side
    width = len(data[0]) + (padding * 2)
    padded_line = ['.'] * width
    for line in range(padding):
        new_data.insert(0, padded_line)  # Pad at beginning
        new_data.append(padded_line)  # Pad at end
    return new_data


# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
def check_seat_empty(seats):
    new_data = deepcopy(seats)
    for r, row in enumerate(seats):
        for c, seat in enumerate(row):
            if seat == 'L':
                if seats[r][c - 1] != '#' and seats[r][c + 1] != '#' and \
                        seats[r + 1][c - 1] != '#' and seats[r + 1][c + 1] != '#' and \
                        seats[r - 1][c - 1] != '#' and seats[r - 1][c + 1] != '#' and \
                        seats[r - 1][c] != '#' and seats[r + 1][c] != '#':
                    new_data[r][c] = '#'
    return new_data


def check_left(s, r, c):
    #    if s[r - 1][c] == s[r - 2][c] == s[r - 3][c] == s[r - 4][c] == '#':
    if s[r - 1][c] == '#':
        return 1
    return 0


def check_right(s, r, c):
    #    if s[r + 1][c] == s[r + 2][c] == s[r + 3][c] == s[r + 4][c] == '#':
    if s[r + 1][c] == '#':
        return 1
    return 0


def check_down(s, r, c):
    #    if s[r][c + 1] == s[r][c + 2] == s[r][c + 3] == s[r][c + 4] == '#':
    if s[r][c + 1] == '#':
        return 1
    return 0


def check_up(s, r, c):
    #    if s[r][c - 1] == s[r][c - 2] == s[r][c - 3] == s[r][c - 4] == '#':
    if s[r][c - 1] == '#':
        return 1
    return 0


def check_downleft(s, r, c):
    #    if s[r - 1][c + 1] == s[r - 2][c + 2] == s[r - 3][c + 3] == s[r - 4][c + 4] == '#':
    if s[r - 1][c + 1] == '#':
        return 1
    return 0


def check_downright(s, r, c):
    #    if s[r + 1][c + 1] == s[r + 2][c + 2] == s[r + 3][c + 3] == s[r + 4][c + 4] == '#':
    if s[r + 1][c + 1] == '#':
        return 1
    return 0


def check_upleft(s, r, c):
    #    if s[r - 1][c - 1] == s[r - 2][c - 2] == s[r - 3][c - 3] == s[r - 4][c - 4] == '#':
    if s[r - 1][c - 1] == '#':
        return 1
    return 0


def check_upright(s, r, c):
    #    if s[r + 1][c - 1] == s[r + 2][c - 2] == s[r + 3][c - 3] == s[r + 4][c - 4] == '#':
    if s[r + 1][c - 1] == '#':
        return 1
    return 0


# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
def check_seat_occupied(seats):
    new_data = deepcopy(seats)
    for r, row in enumerate(seats):
        for c, seat in enumerate(row):
            if seat == '#':
                if (check_left(seats, r, c) + check_right(seats, r, c) + check_up(seats, r, c) + check_down(seats, r, c) + check_downright(seats, r, c) + check_downleft(seats, r, c) + check_upright(seats, r, c) + check_upleft(seats, r, c)) >= 4:
                    new_data[r][c] = 'L'
    return new_data


def print_seats(seats):
    for row in seats:
        for col in row:
            print(col, end='', sep='')
        print()


def count_seat(seats):
    count = 0
    for row in data:
        for seat in row:
            if seat == '#':
                count += 1
    return count


last_count = 0
data = pad(data)
while 1:
    data = check_seat_empty(data)
    data = check_seat_occupied(data)
    counted = count_seat(data)
    if last_count == counted:
        break
    last_count = counted
print(counted)
