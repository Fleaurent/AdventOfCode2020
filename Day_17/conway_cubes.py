'''
infinite 3-dimensional grid
At every coordinate (x,y,z) exists a single cube (active/inactive)
initial state: almost all cubes start inactive
input = flat region of cubes: active # vs inactive .

energy source proceeds to boot up by executing six cycles:
- each cube considers its 28 neighbors cubes
- all cubes simultaneously change their state
a) cube is active: 2 or 3 neighbors active -> remain active otherwise inactive
b) cube is inactive: 3 neighbors active -> become active otherwise inactive
'''
from typing import List, Tuple, Set, Union


def read_input_to_list(filepath: str) -> List[int]:
    output = []
    with open(filepath) as f:
        output = [int(i) for i in f.readlines()]
    return output


def read_input_to_str(filepath: str) -> str:
    output = ""
    with open(filepath) as f:
        output = f.read()
    return output


if __name__ == '__main__':
    example_inputs = read_input_to_str("Day_17/example_input.txt")
    inputs = read_input_to_str("Day_17/input.txt")
