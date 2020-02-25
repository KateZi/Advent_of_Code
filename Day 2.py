with open("Gravity Assist Program", "r") as f:
    program = f.read()

program = list(map(int, program.split(",")))

idx = 0
curr = program[idx]

while curr != 99:
    if curr == 1:
        program[program[idx+3]] = program[program[idx+1]] + program[program[idx+2]]
    elif curr == 2:
        program[program[idx+3]] = program[program[idx+1]] * program[program[idx+2]]
    else:
        print("Something went wrong")
        break
    idx += 4
    curr = program[idx]

print(program)