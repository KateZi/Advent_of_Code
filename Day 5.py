from enum import Enum


class Operation(Enum):
    ADD = 1
    MULT = 2
    INPUT = 3
    OUTPUT = 4
    HALT = 99


class Instruction:

    def __init__(self, pointer, memory):
        self.memory = memory
        self.pointer = pointer

        self.inst = str(memory[pointer])
        self.num = len(self.inst)

        self.op = Operation(int((self.inst[-2] + self.inst[-1])))

    def get_params(self):
        mode_1 = int(self.inst[-3]) if self.num >= 3 else 0
        mode_2 = int(self.inst[-4]) if self.num >= 4 else 0

        param_1 = self.memory[self.memory[self.pointer+1]] if mode_1 == 0 else self.memory[self.pointer+1]
        param_2 = self.memory[self.memory[self.pointer+2]] if mode_2 == 0 else self.memory[self.pointer+2]

        return param_1, param_2

    def preform_op(self):
        result = 0
        if self.op == Operation.ADD:
            param_1, param_2 = self.get_params()
            result = param_1 + param_2
            self.pointer += 4
        elif self.op == Operation.MULT:
            param_1, param_2 = self.get_params()
            result = param_1 * param_2
            self.pointer += 4
        elif self.op == Operation.INPUT:
            result = int(input("Please enter the value to store: "))
            self.pointer += 2
        elif self.op == Operation.OUTPUT:
            param = self.memory[self.pointer+1]
            print(param)
            self.pointer += 2
        elif self.op == Operation.HALT:
            self.pointer = self.num
        return result


def compute(tape):
    pointer = 0
    while pointer < len(tape):
        i = Instruction(pointer, tape)
        if i.op == Operation.HALT:
            print("Finished")
            break
        result = i.preform_op()
        pointer = i.pointer
        tape[tape[i.pointer-1]] = result


def test():
    test_1 = [1002,4,3,4,33]
    test_2 = [1101,100,-1,4,0]
    compute(test_2)


def main():
    with open("inputs/Day 5 - TEST", "r") as f:
        test = f.read()
        tape = list(map(int, f.read().split(',')))

    compute(tape)


if __name__=='__main__':
    main()
