from typing import List, Tuple, Set, Union


def read_input_to_list(filepath: str) -> List[int]:
    output = []
    with open(filepath) as f:
        output = [int(i) for i in f.readlines()]
    return output


def chain_adapters(adapters: List[int]) -> List[int]:
    '''
     list = [1, 2, 4] 
     list[:-1] = [1, 2]
     list[1:]  = [2, 4]
     -> list_diff = [1, 2]
    '''
    # add input + output adapters
    adapters.append(0)
    adapters.append(max(adapters)+3)

    adapters_sorted = sorted(adapters)
    print(adapters_sorted)

    diff_adapters = [j - k for j, k in zip(adapters_sorted[1:], adapters_sorted[:-1])]
    print(diff_adapters)

    diff_1 = diff_adapters.count(1)
    diff_3 = diff_adapters.count(3)
    print(diff_1)
    print(diff_3)
    return diff_1 * diff_3


if __name__ == '__main__':
    example_input = read_input_to_list("Day_10/example_input.txt")
    inputs = read_input_to_list("Day_10/input.txt")

    example_input_test = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    print(chain_adapters(example_input_test))
    print(chain_adapters(example_input))
    print(chain_adapters(inputs))

    # Part 2 ?
    # [1, 2, 3, 4]
    # [1, 1, 1]
