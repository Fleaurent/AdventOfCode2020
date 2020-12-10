from typing import List, Tuple, Set, Union


def read_input_to_list(filepath: str) -> List[int]:
    output = []
    with open(filepath) as f:
        output = [int(i) for i in f.readlines()]
    return output


def diff_adapters(adapters: List[int]) -> List[int]:
    # add input + output adapters
    adapters.append(0)
    adapters.append(max(adapters)+3)

    adapters_sorted = sorted(adapters)

    return [j - k for j, k in zip(adapters_sorted[1:], adapters_sorted[:-1])]


def chain_adapters(adapters: List[int]) -> int:
    '''
     list = [1, 2, 4] 
     list[:-1] = [1, 2]
     list[1:]  = [2, 4]
     -> list_diff = [1, 2]
    '''
    adapters_diff = diff_adapters(adapters)

    diff_1 = adapters_diff.count(1)
    diff_3 = adapters_diff.count(3)

    return diff_1 * diff_3


def adapter_arrangements(adapters: List[int]) -> int:
    adapters_diff = diff_adapters(adapters)

    count_1 = 0
    n_arrangements = 1
    arrangements = [1, 1, 2, 4, 7]

    for diff in adapters_diff:
        if diff == 1:
            count_1 += 1
        elif diff == 3:
            n_arrangements *= arrangements[count_1]
            count_1 = 0

    return n_arrangements


if __name__ == '__main__':
    example_input = read_input_to_list("Day_10/example_input.txt")
    inputs = read_input_to_list("Day_10/input.txt")

    example_input_test = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    print(chain_adapters(example_input_test))
    print(chain_adapters(example_input))
    print(chain_adapters(inputs))

    # Part 2: distinct arrangements diff
    # a: sum([1, 1]) = 2 -> [1, 1], [2]: 2 combinations
    # b: sum([1, 1, 1]) = 3 -> [1, 1, 1], [ 2, 1], [ 1, 2], [3]: 4 Combinations
    # c: sum([1, 1, 1, 1]) = 4 -> [1, 1, 1, 1], [ 2, 1, 1], [ 1, 2, 1], [ 1, 1, 2], [ 2, 2], [1, 3], [3, 1]: 7 Combinations

    # 1. example_input_test
    # diff = [1, 3, 1, 1, 1, 3, 1, 1, 3, 1, 3, 3]
    # -> b, a -> 4*2 -> 8 Combinations

    # 2. example_input
    # diff = [1, 1, 1, 1, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 3, 1, 1, 3, 3, 1, 1, 1, 1, 3, 1, 3, 3, 1, 1, 1, 1, 3]
    # -> c, c, b, a, c, c -> 7*7*4*2*7*7 -> 19208 Combinations

    # 3. input
    # diff = [1, 1, 1, 1, 3, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 3, 1, 1, 1, 3, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 1, 3, 1, 3, 3, 1, 1, 1, 1, 3, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 3, 1, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 3, 3, 1, 1, 1, 1, 3, 1, 3, 3, 1, 1, 1, 3, 1, 1, 1, 1, 3, 1, 1, 1, 1, 3, 1, 1, 3, 3]
    # -> c,b,c,b,b,b,c,c,c,a,c,c,b,a,c,b,c,c,b 
    print(adapter_arrangements(example_input_test))
    print(adapter_arrangements(example_input))
    print(adapter_arrangements(inputs))