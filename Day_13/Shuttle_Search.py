'''
timestamp measures number of minutes since some fixed reference point in the past
At timestamp 0, every bus simultaneously departed from the sea port
-> repeat its journey forever
a) ID 5 departs from the sea port at timestamps 0, 5, 10, 15,
b) ID 11 departs at 0, 11, 22, 33, and so on
-> figure out the earliest bus you can take to the airport.
The first line is the estimate of the earliest timestamp you could depart on a bus.
The second line lists the bus IDs that are in service according to the shuttle company; 
entries that show x must be out of service
'''
from typing import List, Tuple, Set, Union
import numpy as np


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


def read_schedule(filepath: str) -> Tuple[int, List[int]]:
    with open(filepath) as f:
        departure_str = f.readline()
        buslines_str = f.readline()

    departure = int(departure_str)
    buslines = [i for i in buslines_str.split(',')]

    return departure, buslines


def find_bus(departure: int, buslines: List[str]) -> int:
    buslines = [int(i) for i in buslines if i != 'x']
    next_departures = [(departure // busline_i)*busline_i + busline_i for busline_i in buslines]

    waiting = min(next_departures) - departure
    busline = buslines[next_departures.index(min(next_departures))]

    return busline*waiting


def run_contest(buslines_str: List[str], start_time: int = 0) -> int:
    buslines = []
    buslines_depart = []
    for i, busline in enumerate(buslines_str):
        if busline != 'x':
            buslines.append(int(busline))
            buslines_depart.append(i)

    time = start_time
    timestep = max(buslines)
    diff_depart = buslines_depart[buslines.index(timestep)]
    time = find_starttime(start_time, timestep, diff_depart)
    valid = False
    while(not valid):
        time += timestep
        valid = time_valid(time, buslines, buslines_depart)
    return time


def find_starttime(start_time: int, timestep: int, diff: int):
    while((start_time + diff) % timestep != 0):
        start_time += 1
    print(start_time)
    return start_time


def time_valid(time: int, buslines: List[int], buslines_depart: List[int]):
    for busline, busline_depart in zip(buslines, buslines_depart):
        # print(busline, busline_depart)
        if (time+busline_depart) % busline:
            return False
    
    return True

'''
assert run_contest(['17','x','13','19']) == 3417
assert run_contest(['67','7','59','61']) == 754018
assert run_contest(['67','x','7','59','61']) == 779210
assert run_contest(['67','7','x','59','61']) == 1261476
assert run_contest(['1789','37','47','1889'], 1202100000) == 1202161486
'''

if __name__ == '__main__':
    departure_example, buslines_example = read_schedule("Day_13/example_input.txt")
    print(find_bus(departure_example, buslines_example))

    departure, buslines = read_schedule("Day_13/input.txt")
    print(find_bus(departure, buslines))

    print(run_contest(buslines_example))
    print(run_contest(buslines, 100000000000000))
