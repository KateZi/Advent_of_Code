from enum import Enum


class Operation(Enum):
    ADD = 1
    MULT = 2
    INPUT = 3
    OUTPUT = 4
    JTRUE = 5
    JFALSE = 6
    ISLESS = 7
    EQUALS = 8
    HALT = 99


class Computer:

    def __init__(self, memory):
        self.memory = memory
        self.pointer = 0

    def compute(self):
        op = 0
        while op != Operation.HALT:
            instruction = str(self.memory[self.pointer])
            length = len(instruction)

            op = self.get_op(instruction, length)
            modes = self.get_modes(instruction, length)

            self.perform_op(op, modes)

    def get_op(self, instruction, length):
        op = instruction[-2] + instruction[-1] if length > 1 else instruction[-1]
        return Operation(int((op)))

    def get_modes(self, instruction, length):
        modes = list()
        for i in range(1,4):
            mode = int(instruction[-2-i]) if length >= 2+i else 0
            modes.append(mode)

        return modes

    def get_param(self, pointer, mode):
        param = self.memory[pointer] if mode == 0 else pointer

        return param

    def perform_op(self, op, modes):
        result = 0
        if op == Operation.ADD:
            result = self.memory[self.get_param(self.pointer+1, modes[0])] + \
                     self.memory[self.get_param(self.pointer+2, modes[1])]
            self.memory[self.get_param(self.pointer+3, modes[2])] = result
            self.pointer += 4
        elif op == Operation.MULT:
            result = self.memory[self.get_param(self.pointer + 1, modes[0])] *\
                     self.memory[self.get_param(self.pointer + 2, modes[1])]
            self.memory[self.get_param(self.pointer + 3, modes[2])] = result
            self.pointer += 4
        elif op == Operation.INPUT:
            result = int(input("Please enter the value to store: "))
            self.memory[self.get_param(self.pointer+1, 0)] = result
            self.pointer += 2
        elif op == Operation.OUTPUT:
            param = self.memory[self.get_param(self.pointer+1, 0)]
            print(param)
            self.pointer += 2
        elif op == Operation.JTRUE:
            if self.memory[self.get_param(self.pointer+1, modes[0])] != 0:
                self.pointer = self.memory[self.get_param(self.pointer+2, modes[1])]
            else:
                self.pointer += 3
        elif op == Operation.JFALSE:
            if self.memory[self.get_param(self.pointer+1, modes[0])] == 0:
                self.pointer = self.memory[self.get_param(self.pointer+2, modes[1])]
            else:
                self.pointer += 3
        elif op == Operation.ISLESS:
            param_1 = self.memory[self.get_param(self.pointer+1, modes[0])]
            param_2 = self.memory[self.get_param(self.pointer+2, modes[1])]
            result = 1 if param_1 < param_2 else 0
            self.memory[self.get_param(self.pointer+3, modes[2])] = result
            self.pointer += 4
        elif op == Operation.EQUALS:
            param_1 = self.memory[self.get_param(self.pointer + 1, modes[0])]
            param_2 = self.memory[self.get_param(self.pointer + 2, modes[1])]
            result = 1 if param_1 == param_2 else 0
            self.memory[self.get_param(self.pointer + 3, modes[2])] = result
            self.pointer += 4
        elif op == Operation.HALT:
            print("Halting")

def test():
    tape_1 = [1002,4,3,4,33]
    tape_2 = [3,0,4,0,99]

    comp = Computer(tape_2)
    comp.compute()

    print(tape_2)

def main():
    with open("inputs/Day 5 - TEST", "r") as f:
        tape = list(map(int, f.read().split(',')))

    intCode_comp = Computer(tape)
    intCode_comp.compute()


if __name__=='__main__':
    main()
