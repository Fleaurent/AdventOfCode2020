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
    example_inputs = read_input_to_str("Template/example_input.txt")
    inputs = read_input_to_str("Template/input.txt")
