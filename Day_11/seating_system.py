from typing import List, Tuple, Set, Union

'''
Rules
If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.
'''

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


def read_input_to_lines(filepath: str) -> List[str]:
    output = []
    with open(filepath) as f:
        lines = f.readlines()
        for line in lines:
            output.append(line.strip())
    return output


def init_seats(seats: List[str]) -> List[List[str]]:
    n_rows = len(seats)
    n_cols = len(seats[0])

    updated_seats = [['.']*n_cols for _ in range(n_rows)]
    for row in range(n_rows):
        for col in range(n_cols):
            updated_seats[row][col] = seats[row][col]

    return updated_seats


def update_seats(seats: List[List[str]]) -> List[List[str]]:
    n_rows = len(seats)
    n_cols = len(seats[0])
    seat_changes = 0

    updated_seats = [['.']*n_cols for _ in range(n_rows)]

    for row in range(n_rows):
        for col in range(n_cols):
            seat = seats[row][col]
            n_seats_occupied = get_occupied_seats(seats, row, col)
            # print(n_seats_occupied)
            # print(seats[row][col])
            if seat == 'L':
                if n_seats_occupied > 0:
                    updated_seats[row][col] = 'L'
                else:
                    seat_changes += 1
                    updated_seats[row][col] = '#'
            elif seat == '#':
                if n_seats_occupied > 3:
                    seat_changes += 1
                    updated_seats[row][col] = 'L'
                else:
                    updated_seats[row][col] = '#'
            # print(updated_seats[row][col])

    return updated_seats


def get_occupied_seats(seats: List[List[str]], row: int, col: int) -> int:
    n_rows = len(seats)
    n_cols = len(seats[0])

    # row-1 : row+1
    # col-1 : row+1
    if row == 0:
        row_min = 0
    else:
        row_min = row - 1

    if row == n_rows:
        row_max = n_rows
    else:
        row_max = row + 1

    if col == 0:
        col_min = 0
    else:
        col_min = col - 1

    if col == n_cols:
        col_max = n_cols
    else:
        col_max = col + 1

    occupied_seats = 0
    for row_i in seats[row_min:row_max+1]:
        row_part = row_i[col_min:col_max+1]
        occupied_seats += row_part.count('#')

    if seats[row][col] == '#':
        occupied_seats -= 1

    return occupied_seats


def count_seats(seats: List[List[str]]):
    return sum([i.count('#') for i in seats])


def iterate_seats(seats: List[List[str]]) -> int:
    seats = init_seats(seats)

    seats_old = count_seats(seats)
    seats_new = seats_old

    seats_changing = True
    while(seats_changing):
        seats_old = seats_new
        seats = update_seats(seats)
        seats_new = count_seats(seats)

        if seats_old == seats_new:
            seats_changing = False

    return seats_new


if __name__ == '__main__':
    example_input = read_input_to_lines("Day_11/example_input.txt")
    inputs = read_input_to_lines("Day_11/input.txt")

    print(iterate_seats(example_input))
    print(iterate_seats(inputs))


'''
#.##.##.##
#######.##

#.LL.L#.##
#LLLLLL.L#

#.##.L#.##
#L###LL.L#

#.#L.L#.##
#LLL#LL.L#

#.#L.L#.##
#LLL#LL.L#
'''