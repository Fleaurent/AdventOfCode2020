from typing import List, Tuple, Set, Union
import math


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


NORTH = 0
EAST = 90
SOUTH = 180
WEST = 270


class Coordinates:
    def __init__(self):
        self.direction = EAST
        self.coordinates = [0, 0]  # [x, y]

    def update(self, turn: str):
        command = turn[0]
        amount = int(turn[1:])

        if command == 'F':
            # move forward
            self.move(self.direction, amount)
        elif command == 'R':
            # turn right the given number of degrees
            self.rotate(amount)
        elif command == 'L':
            # turn left the given number of degrees
            self.rotate(-amount)
        elif command == 'N':
            self.move(NORTH, amount)
        elif command == 'E':
            self.move(EAST, amount)
        elif command == 'S':
            self.move(SOUTH, amount)
        elif command == 'W':
            self.move(WEST, amount)

    def rotate(self, degrees: int):
        # EAST <-> SOUTH <-> WEST <-> NORTH
        self.direction = (self.direction + degrees) % 360

    def move(self, direction: str, amount: int):
        if direction == NORTH:
            self.coordinates[1] += amount
        elif direction == EAST:
            self.coordinates[0] += amount
        elif direction == SOUTH:
            self.coordinates[1] -= amount
        elif direction == WEST:
            self.coordinates[0] -= amount

    def manhattan_distance(self):
        return abs(self.coordinates[0]) + abs(self.coordinates[1])


def move_ship(inputs: List[str]) -> int:
    position = Coordinates()
    for temp_input in inputs:
        position.update(temp_input)

    return position.manhattan_distance()


class Coordinates_Waypoint:
    def __init__(self):
        self.coordinates_ship = [0, 0]
        self.coordinates_waypoint = [10, 1]  # relative to the ship!

    def update(self, turn: str):
        command = turn[0]
        amount = int(turn[1:])

        if command == 'F':            
            self.move_ship(amount)
        elif command == 'R':
            # clockwise is negative!
            self.rotate_waypoint(-amount)
        elif command == 'L':
            # counter clockwise is positive
            self.rotate_waypoint(amount)
        elif command == 'N':
            self.move_waypoint(NORTH, amount)
        elif command == 'E':
            self.move_waypoint(EAST, amount)
        elif command == 'S':
            self.move_waypoint(SOUTH, amount)
        elif command == 'W':
            self.move_waypoint(WEST, amount)

    def move_ship(self, amount: int):
        # move forward to the waypoint a number of times equal to the given value.
        self.coordinates_ship[0] += self.coordinates_waypoint[0] * amount
        self.coordinates_ship[1] += self.coordinates_waypoint[1] * amount

    def rotate_waypoint(self, degrees: int):
        # EAST <-> SOUTH <-> WEST <-> NORTH
        # a) rotate the waypoint around the ship left (counter-clockwise) the given number of degrees
        # b) rotate the waypoint around the ship right (clockwise) the given number of degrees.
        direction = degrees % 360
        x_0 = self.coordinates_waypoint[0]
        x_1 = self.coordinates_waypoint[1]

        ''' 
        rotate_sin = math.sin(math.radians(direction))
        rotate_cos = math.cos(math.radians(direction))
        
        self.coordinates_waypoint[0] = rotate_cos*x_0 - rotate_sin*x_1
        self.coordinates_waypoint[1] = rotate_sin*x_0 + rotate_cos*x_1
        '''
        if direction == 90:
            # rotate_sin=1, rotate_cos=0
            self.coordinates_waypoint[0] = -1 * x_1
            self.coordinates_waypoint[1] =  1 * x_0 
        elif direction == 180:
            # rotate_sin=0, rotate_cos=-1
            self.coordinates_waypoint[0] = -1 * x_0
            self.coordinates_waypoint[1] = -1 * x_1
        elif direction == 270:
            # rotate_sin=-1, rotate_cos=0
            self.coordinates_waypoint[0] =  1 * x_1
            self.coordinates_waypoint[1] = -1 * x_0

    def move_waypoint(self, direction: str, amount: int):
        if direction == NORTH:
            self.coordinates_waypoint[1] += amount
        elif direction == EAST:
            self.coordinates_waypoint[0] += amount
        elif direction == SOUTH:
            self.coordinates_waypoint[1] -= amount
        elif direction == WEST:
            self.coordinates_waypoint[0] -= amount

    def manhattan_distance(self):
        return abs(self.coordinates_ship[0]) + abs(self.coordinates_ship[1])


def move_waypoint(inputs: List[str]) -> int:
    position = Coordinates_Waypoint()
    for temp_input in inputs:
        position.update(temp_input)

    return position.manhattan_distance()


if __name__ == '__main__':
    example_inputs = read_input_to_list("Day_12/example_input.txt")
    inputs = read_input_to_list("Day_12/input.txt")

    print(move_ship(example_inputs))
    print(move_ship(inputs))

    print(move_waypoint(example_inputs))
    print(move_waypoint(inputs))
