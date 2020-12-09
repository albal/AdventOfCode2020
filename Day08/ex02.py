input_file = "input08.txt"

with open(input_file, 'r') as file:
    data = file.read().split('\n')

ops_to_flip = []
loc = 0


def new_code(codes, pos, new_val):
    new_codes = []
    i = 0
    for code in codes:
        if pos == i:
            new_codes.append(new_val)
        else:
            new_codes.append(code)
        i += 1
    return new_codes


# build list of nop or jmp locations
for line in data:
    opcode, val = line.strip().split(" ")
    if opcode == "nop" or opcode == "jmp":
        ops_to_flip.append(loc)
    loc += 1

for op in ops_to_flip:
    # reload the data
    with open(input_file, 'r') as file:
        data = file.read().split('\n')

    opcode, val = data[op].strip().split(" ")
    if opcode == "jmp":
        data = new_code(data, op, "nop" + " " + val)
    elif opcode == "nop":
        data = new_code(data, op, "jmp" + " " + val)

    ran = []
    pc = acc = 0

    while True:
        opcode, val = data[pc].strip().split(" ")
        if opcode == "nop":
            pc += 1
        elif opcode == "acc":
            acc += int(val)
            pc += 1
        elif opcode == "jmp":
            pc += int(val)
        if pc in ran:
            break
        ran.append(pc)

        if pc == len(data):
            print("Found correction. PC: ", pc, "  ACC: ", acc, "  OP: ", op, " which is \"", data[op], "\"",sep="")
            exit(0)
