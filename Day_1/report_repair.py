from typing import List, Tuple

example_data = [1721,
                979,
                366,
                299,
                675,
                1456]


def find_sum_number(data: List, number: int) -> Tuple[int, int]:
    # O(n) !!!
    # 1. create set with numbers needed for the sum
    number_needed = {number - i for i in data}

    # 2. search if given number is also a number needed
    for num in data:
        if num in number_needed:
            return num, number - num
    return None, None


def find_sum_number3(data: List, number: int) -> Tuple[int, int, int]:
    # Problem O(n^3)
    # search if given number is also a number needed
    for num1 in data:
        for num2 in data:
            for num3 in data:
                if num1 + num2 + num3 == number:
                    return num1, num2, num3
    return None, None, None


def find_sum_number32(data: List, number: int) -> Tuple[int, int, int]:
    # -> O(n^2)
    # search if given number is also a number needed
    # number_needed = {number - j + k for j,k in zip(data, data)}
    number_needed = {}
    for num1 in data:
        for num2 in data:
            num = number - num1 - num2
            number_needed[num] = [num1, num2]

    for num3 in data:
        if num3 in number_needed.keys():
            num1, num2 = number_needed[num3]
            return num1, num2, num3
    return None, None, None


if __name__ == '__main__':
    print("Hello World")

    data = []
    with open("input.txt") as f:
        lines = f.readlines()
        data = [int(i) for i in lines]
    print(data)

    num1, num2 = find_sum_number(data=example_data, number=2020)
    print(num1, num2)
    print(num1 * num2)

    num1, num2 = find_sum_number(data=data, number=2020)
    print(num1, num2)
    print(num1 * num2)

    num1, num2, num3 = find_sum_number3(data=example_data, number=2020)
    print(num1, num2, num3)
    print(num1 * num2 * num3)

    num1, num2, num3 = find_sum_number3(data=data, number=2020)
    print(num1, num2, num3)
    print(num1 * num2 * num3)

    num1, num2, num3 = find_sum_number32(data=example_data, number=2020)
    print(num1, num2, num3)
    print(num1 * num2 * num3)

    num1, num2, num3 = find_sum_number32(data=data, number=2020)
    print(num1, num2, num3)
    print(num1 * num2 * num3)
