'''
1 + 2 * 3 + 4 * 5 + 6 -> 71
1 + (2 * 3) + (4 * (5 + 6)) -> 51
'''
from typing import List, Tuple, Set, Union


def read_input_to_list(filepath: str) -> List[str]:
    output = []
    with open(filepath) as f:
        output = [line.strip() for line in f.readlines()]
    return output


def read_input_to_str(filepath: str) -> str:
    output = ""
    with open(filepath) as f:
        output = f.read()
    return output


def calculate_str(input_str: List[str]) -> int:
    ''' 1 + 2  -> 3
        1 + 2 * 3 -> 3 * 3 -> 9
        1 * 3 + 3 * 4 -> 3 + 3 * 4 -> 9 * 4 -> 36
        -> number operator number
    '''
    # 0. break condition:
    if len(input_str) <= 2:
        return input_str[0]

    # 1. calculate first three items
    if input_str[1] == '+':
        temp_val = int(input_str[0]) + int(input_str[2])
    elif input_str[1] == '*':
        temp_val = int(input_str[0]) * int(input_str[2])

    # 2. build new input_str
    temp_input_str = [temp_val] + input_str[3:]
    return calculate_str(temp_input_str)


assert calculate_str("1 + 2".split()) == 3
assert calculate_str("1 + 2 * 3".split()) == 9
assert calculate_str("1 * 3 + 3 * 4".split()) == 24
assert calculate_str("1 + 2 * 3 + 4 * 5 + 6".split()) == 71


def calculate_expression(input_str: str) -> int:
    '''
    1 + (2 * 3) + (4 * (5 + 6))
    1 +    6    + (4 * (5 + 6))
     7      + (4 * (5 + 6))
     7      + (4 *   11   )
     = 51
    '''
    # 1. find innermost parantheses index
    current_level = 0
    max_level = 0
    max_level_start = 0
    max_level_end = 0
    for i, char in enumerate(input_str):
        if char == '(':
            current_level += 1
            if current_level >= max_level:
                max_level = current_level
                max_level_start = i
        elif char == ')':
            if current_level == max_level:
                max_level_end = i
            current_level -= 1

    # print(current_level, max_level, max_level_start, max_level_end)

    # -> break condition: no paranthesis
    if max_level == 0:
        return calculate_str(input_str.split())

    innermost_str = input_str[max_level_start+1:max_level_end]

    # 2. calculate innermost parantheses
    innermost_value = calculate_str(innermost_str.split())

    # 3. replace innermost parantheses with its calculated value
    new_input_str = input_str[:max_level_start] + str(innermost_value) + input_str[max_level_end+1:] 
    # print(new_input_str)
    return calculate_expression(new_input_str)


assert calculate_expression("7 + (4 * 11)") == 51
assert calculate_expression("7 + (4 * (5 + 6))") == 51
assert calculate_expression("1 + (2 * 3) + (4 * 11)") == 51


def calculate_expressions(input_list: str) -> int:
    expression_sum = 0
    for input_str in input_list:
        expression_sum += calculate_expression(input_str)
    return expression_sum


##########
# Part 2 #
##########
def calculate_str2(input_str: List[str]) -> int:
    ''' + before *
        1 + 2  -> 3
        1 + 2 * 3 -> 3 * 3 -> 9
        1 * 3 + 3 * 4 -> 1 * 6 * 4 -> 24
        -> number operator number
    '''

    # 0. break condition:
    if not '+' in input_str:
        if len(input_str) <= 2:
            return input_str[0]
        else:
            return calculate_str(input_str)

    # 1. find '+'
    plus_index = input_str.index('+')

    # 2. calculate '+
    temp_val = int(input_str[plus_index-1]) + int(input_str[plus_index+1])

    # 3. build new input_str
    input_str[plus_index] = temp_val
    input_str.pop(plus_index-1)
    input_str.pop(plus_index)  # smaller list! -> no -1

    return calculate_str2(input_str)


assert calculate_str2("1 + 2".split()) == 3
assert calculate_str2("1 + 2 * 3".split()) == 9
assert calculate_str2("1 * 3 + 3 * 4".split()) == 24


def calculate_expression2(input_str: str) -> int:
    '''
    1 + (2 * 3) + (4 * (5 + 6))
    1 +    6    + (4 * (5 + 6))
     7      + (4 * (5 + 6))
     7      + (4 *   11   )
     = 51
    '''
    # 1. find innermost parantheses index
    current_level = 0
    max_level = 0
    max_level_start = 0
    max_level_end = 0
    for i, char in enumerate(input_str):
        if char == '(':
            current_level += 1
            if current_level >= max_level:
                max_level = current_level
                max_level_start = i
        elif char == ')':
            if current_level == max_level:
                max_level_end = i
            current_level -= 1

    # print(current_level, max_level, max_level_start, max_level_end)

    # -> break condition: no paranthesis
    if max_level == 0:
        return calculate_str2(input_str.split())

    innermost_str = input_str[max_level_start+1:max_level_end]

    # 2. calculate innermost parantheses
    innermost_value = calculate_str2(innermost_str.split())

    # 3. replace innermost parantheses with its calculated value
    new_input_str = input_str[:max_level_start] + str(innermost_value) + input_str[max_level_end+1:] 
    # print(new_input_str)
    return calculate_expression2(new_input_str)


def calculate_expressions2(input_list: str) -> int:
    expression_sum = 0
    for input_str in input_list:
        expression_sum += calculate_expression2(input_str)
    return expression_sum


if __name__ == '__main__':
    example_inputs = read_input_to_list("Day_18/example_input.txt")
    inputs = read_input_to_list("Day_18/input.txt")

    print(calculate_expressions(example_inputs))
    print(calculate_expressions(inputs))

    print(calculate_expressions2(example_inputs))
    print(calculate_expressions2(inputs))
