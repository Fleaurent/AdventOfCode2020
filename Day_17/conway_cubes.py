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
import numpy as np

def read_input_to_str(filepath: str) -> str:
    output = ""
    with open(filepath) as f:
        output = f.read()
    return output


def parse_cube_input(data: str) -> np.array:
    cube_array = []

    for row_i in data.split('\n'):
        cube_array.append(list(row_i))

    return np.array([cube_array])


def active_cells(cube: np.array) -> int:
    return np.count_nonzero(cube == '#')


def cube_cycle(cube: np.array):
    # 1. increase each dimension +-1
    dim_z, dim_y, dim_x = np.shape(cube)  # (z, y, x)
    cube_enhanced = np.full((dim_z+2, dim_y+2, dim_x+2), fill_value='.')
    cube_enhanced[1:-1, 1:-1, 1:-1] = cube

    # 2. update each pixel
    cube_update = cube_enhanced.copy()
    dim_z, dim_y, dim_x = np.shape(cube_enhanced)
    # print(dim_z, dim_y, dim_x)

    for z_i in range(dim_z):
        for y_i in range(dim_y):
            for x_i in range(dim_x):
                # 1. access each cell
                cell_zyx = cube_enhanced[z_i, y_i, x_i]
                # print(z_i, y_i, x_i)

                # 2. extract subcube for each cell
                z_min = 0 if z_i == 0 else z_i - 1
                y_min = 0 if y_i == 0 else y_i - 1
                x_min = 0 if x_i == 0 else x_i - 1
                z_max = dim_z-1 if z_i == dim_z-1 else z_i + 1
                y_max = dim_y-1 if y_i == dim_y-1 else y_i + 1
                x_max = dim_x-1 if x_i == dim_x-1 else x_i + 1
                # print(z_min, z_max, y_min, y_max, x_min, x_max)
                sub_cube_zyx = cube_enhanced[z_min:z_max+1, y_min:y_max+1, x_min:x_max+1]

                # 3. update each cell based on active neighbors
                if(cell_zyx == '.'):  # inactive
                    active_neighbors_zyx = active_cells(sub_cube_zyx)
                    if active_neighbors_zyx == 3:
                        cube_update[z_i, y_i, x_i] = '#'
                elif(cell_zyx == '#'):  # active
                    active_neighbors_zyx = active_cells(sub_cube_zyx) - 1  # do not count cell itself!
                    if not (active_neighbors_zyx == 2 or active_neighbors_zyx == 3):
                        cube_update[z_i, y_i, x_i] = '.'

    return cube_update


def cycle_cube(data: str, n_cycles: int) -> int:
    cube = parse_cube_input(data)

    for cycle in range(n_cycles):
        cube = cube_cycle(cube)

    return active_cells(cube)


if __name__ == '__main__':
    example_inputs = read_input_to_str("Day_17/example_input.txt")
    inputs = read_input_to_str("Day_17/input.txt")

    print(cycle_cube(example_inputs, 6))
    print(cycle_cube(inputs, 6))


'''
# ToDo: refactor in class
class Cube:
    def __init__(self, data: str):
        self.cube = np.array([])
        self.parse_cube_input(data)

    def parse_cube_input(self, data: str):
        cube_array = []

        for row_i in data.split('\n'):
            cube_array.append(list(row_i))

        self.cube = np.array([cube_array])
'''