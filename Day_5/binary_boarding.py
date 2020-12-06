from typing import List


def decode_seat(input: str) -> int:
    row_str = input[:7]
    column_str = input[7:]

    row = decode_row(row_str)
    column = decode_column(column_str)

    return seat_ID(row, column)


def decode_row(row: str) -> int:
    '''
    The first 7 characters will either be F or B;
    these specify exactly one of the 128 rows
    Start by considering the whole range, rows 0 through 127.
    F means to take the lower half, keeping rows 0 through 63.
    B means to take the upper half, keeping rows 32 through 63.
    F means to take the lower half, keeping rows 32 through 47.
    B means to take the upper half, keeping rows 40 through 47.
    B keeps rows 44 through 47.
    F keeps rows 44 through 45.
    The final F keeps the lower of the two, row 44
    '''
    row_min = 0
    row_max = 127
    for i in row.strip():
        if i == "F":
            row_max -= ((row_max - row_min + 1) // 2)
        elif i == "B":
            row_min += (row_max - row_min + 1) // 2

    return row_min


def decode_column(column: str) -> int:
    '''The last three characters will be either L or R;
    these specify exactly one of the 8 columns of seats on the plane
    L == Lower half
    R == Upper half'''
    column_min = 0
    column_max = 7
    for i in column.strip():
        if i == "L":
            column_max -= ((column_max - column_min + 1) // 2)
        elif i == "R":
            column_min += (column_max - column_min + 1) // 2
    return column_min


def seat_ID(row: int, column: int) -> int:
    '''seat ID: multiply the row by 8, then add the column'''
    return (row * 8) + column


assert seat_ID(1, 1) == 9


def highest_seat_ID(filepath: str) -> int:
    input_str = ""
    highest_ID = 0

    with open(filepath) as f:
        input_str = f.read()

    for input_seat in input_str.split('\n'):
        temp_ID = decode_seat(input_seat)
        if temp_ID > highest_ID:
            highest_ID = temp_ID

    return highest_ID


def flight_IDs(filepath: str) -> List[int]:
    input_str = ""
    seat_IDs = []

    with open(filepath) as f:
        input_str = f.read()

    for input_seat in input_str.split('\n'):
        temp_ID = decode_seat(input_seat)
        seat_IDs.append(temp_ID)

    return sorted(seat_IDs)


def find_skipped_value(values: List[int]) -> int:
    skipped_values = []
    for i, value in enumerate(values):
        if(i == len(values) - 1):
            break
        elif(values[i+1] - value > 1):
            skipped_values.append(value+1)

    return skipped_values


if __name__ == '__main__':
    print(highest_seat_ID('Day_5/example_input.txt'))
    print(highest_seat_ID('Day_5/input.txt'))

    print(flight_IDs('Day_5/example_input.txt'))
    IDs = flight_IDs('Day_5/input.txt')
    # print(IDs)
    print(find_skipped_value(IDs))
