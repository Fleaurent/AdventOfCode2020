'''
transmitting a preamble of 25 numbers
each number you receive should be the sum of any two of the 25 immediately previous numbers
'''
from typing import List, Set


def read_input(filepath: str) -> List[int]:
    output = []
    with open(filepath) as f:
        output = [int(i) for i in f.readlines()]
    return output


def get_valid_numbers(preamble: List[int]) -> Set[int]:
    valid_numbers = set()
    for j in preamble:
        for k in preamble:
            valid_numbers.add(j+k)

    return valid_numbers


def find_encoding_error(inputs: List[int], preample_length: int = 25) -> int:
    for i in range(preample_length, len(inputs)):
        preamble_i = inputs[i - preample_length:i]
        valid_numbers_i = get_valid_numbers(preamble=preamble_i)
        if inputs[i] not in valid_numbers_i:
            return inputs[i]

    return 0


def find_contiguous_set(numbers: List[int], target_value: int) -> List[int]:
    # 1. iterate all window lenghts
    # 2. iterate temp window size over all numbers
    # 3. sum window == target_value -> return window
    for window_size in range(2, len(numbers)):
        for i in range(len(numbers) - window_size):
            temp_window = numbers[i:i+window_size]
            if sum(temp_window) == target_value:
                return temp_window
    return []


def encryption_weakness(numbers: List[int], target_value: int) -> int:
    window = find_contiguous_set(numbers, target_value)
    return min(window) + max(window)


if __name__ == '__main__':
    example_input = read_input("Day_9/example_input.txt")
    inputs = read_input("Day_9/input.txt")

    print(find_encoding_error(example_input, preample_length=5))
    print(find_encoding_error(inputs, preample_length=25))

    print(encryption_weakness(example_input, 127))
    print(encryption_weakness(inputs, 177777905))
