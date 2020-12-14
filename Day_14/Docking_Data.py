'''
Values and memory addresses are both 36-bit unsigned integers
mem[8] = 11 would write the value 11 to memory address 8.
bitmask is always given as a string of 36 bits, MSB to LSB
a 0 or 1 overwrites the corresponding bit in the value, while an X leaves the bit in the value unchanged.
all registers are initialized with 0
return sum of all values left in memory after the initialization program completes
'''
from typing import List, Tuple, Set, Union


def read_input_to_list(filepath: str) -> List[int]:
    output = []
    with open(filepath) as f:
        output = [i.strip() for i in f.readlines()]
    return output


def read_input_to_str(filepath: str) -> str:
    output = ""
    with open(filepath) as f:
        output = f.read()
    return output


class Initialization:
    def __init__(self):
        self.set_bits = 0
        self.reset_bits = 0
        self.mem = dict()

    # a) set value at x: reg |= (1 << x)
    # b) reset value at x: reg &= ~(1 << x)
    def update_mask(self, mask_str: str):
        self.set_bits = 0
        self.reset_bits = 0

        # reverse mask: iterate from lsb to msb
        for i, bit_ch in enumerate(mask_str[::-1]):
            if(bit_ch == '1'):
                self.set_bits |= (1 << i)
            elif(bit_ch == '0'):
                self.reset_bits |= (1 << i)

    def update_mem(self, key: int, value: int):
        # 1. try to get value or initialize
        # try:
        #     old_val = self.mem[key]
        # except KeyError:
        #     old_val = 0 
        # 2. set and reset bits
        value |= self.set_bits
        value &= ~self.reset_bits 

        # 3. set value
        self.mem[key] = value

    def print_mem(self):
        for key, value in self.mem.items():
            print(key, value)
    
    def mem_sum(self) -> int:
        value_sum = 0
        for value in self.mem.values():
            value_sum += value
        return value_sum

    def initilialize(self, instructions: List[str]):
        for instruction in instructions:
            command, value = instruction.split(" = ")
            if command.startswith("mask"):
                self.update_mask(value)
            elif command.startswith("mem"):
                key = command[4:-1]  # using regex: re.search(r"[0-9]+", "[123]").group(0)
                self.update_mem(key, int(value))


def test_initializer():
    initializer = Initialization()

    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
    initializer.update_mask(mask)
    print(initializer.set_bits)
    print(initializer.reset_bits)

    initializer.update_mem(key=8, value=11)
    initializer.print_mem()
    initializer.update_mem(key=7, value=101)
    initializer.print_mem()
    initializer.update_mem(key=8, value=0)
    initializer.print_mem()

    
if __name__ == '__main__':
    example_inputs = read_input_to_list("Day_14/example_input.txt")
    inputs = read_input_to_list("Day_14/input.txt")
    # test_initializer()

    initializer = Initialization()
    initializer.initilialize(example_inputs)
    initializer.print_mem()
    print(initializer.mem_sum())

    initializer2 = Initialization()
    initializer2.initilialize(inputs)
    initializer2.print_mem()
    print(initializer2.mem_sum())
        
