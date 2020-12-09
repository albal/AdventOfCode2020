with open('input08.txt', 'r') as file:
    data = file.read().split('\n')

ran = []
pc = acc = 0

while 1:
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

print("PC:", pc, "ACC:", acc)
