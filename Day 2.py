EXP_OUT = 19690720

def compute(input):
    idx = 0
    curr = input[idx]

    while curr != 99:
        if curr == 1:
            input[input[idx+3]] = input[input[idx+1]] + input[input[idx+2]]
        elif curr == 2:
            input[input[idx+3]] = input[input[idx+1]] * input[input[idx+2]]
        else:
            print("Something went wrong")
            break
        idx += 4
        curr = input[idx]
    return input


with open("inputs/Gravity Assist Program", "r") as f:
    program = f.read()

program = list(map(int, program.split(",")))

for i in range(100):
    input = program.copy()
    input[1] = i
    for j in range(100):
        input[2] = j
        output = compute(input)
        if output[0] == EXP_OUT:
            print(output)
            break
        input = program.copy()
        input[1] = i

