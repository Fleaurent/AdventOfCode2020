'''
the fields have valid ranges for values
input: 
1. rules for ticket fields: 
specify a list of fields that exist and the valid ranges of values for each field
e.g. class: 1-3 or 5-7
-> field class on ticket can have any value between 1-3 or 5-7 (inclusive)

2. numbers on your ticket
3. numbers on other nearby tickets
Each ticket is a single line of comma-separated values
-> numbers are always in the same order they appear on the ticket

Task1: 
determine invalid tickets 
i.e. tickets that contain invalied values for any field.
Question: ticket scanning error rate on nearby tickets!
'''
from typing import List, Tuple, Set, Union, Dict
import re


def read_input_to_list(filepath: str) -> List[int]:
    output = []
    with open(filepath) as f:
        output = [int(i) for i in f.readlines()]
    return output

'''
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12 
'''

# 1. input
def read_input_to_str(filepath: str) -> str:
    output = ""
    with open(filepath) as f:
        output = f.read()
    return output


def parse_rules(rule_str: str) -> List[List[int]]:
    rules = dict()
    for rule in rule_str.split('\n'):
        class_str, regions = rule.split(':')
        region1, _ , region2 = regions.split()
        min1, max1 = [int(i) for i in region1.split('-')]
        min2, max2 = [int(i) for i in region2.split('-')]
        rules[class_str] = [min1, max1, min2, max2]
    return rules


def parse_tickets(ticket_str: str) -> List[int]:
    tickets = []
    # ignore first line
    for ticket_i_str in ticket_str.split('\n')[1:]:
        ticket_i = [int(i) for i in ticket_i_str.split(',')]
        tickets.append(ticket_i)

    return tickets


def read_tickets(text: str):
    rules_str, my_ticket_str, nearby_tickets_str = text.split('\n\n')
    # 1. parse rules
    rules = parse_rules(rules_str)

    # 2. parse tickets
    my_ticket = parse_tickets(my_ticket_str)

    nearby_tickets = parse_tickets(nearby_tickets_str)
    return rules, my_ticket, nearby_tickets


# 2. check data
def check_valid_range(value: int, ranges: List[int]):
    min1, max1, min2, max2 = ranges
    return (min1 <= value <= max1) or (min2 <= value <= max2)


def check_valid_value(value: int, rules: Dict[str, List[int]]) -> bool:
    valid_value = False
    for key, valid_range in rules.items():
        valid_value |= check_valid_range(value, valid_range)

    return 0 if valid_value else value


def error_rate(tickets: List[int], rules: Dict[str, List[int]]) -> int:
    # check if all values are in a valid range
    sum_error_rate = 0
    for ticket in tickets:
        for value in ticket:
            sum_error_rate += check_valid_value(value, rules)

    return sum_error_rate


# 3. Unit Tests
assert check_valid_range(6, [1,5,7,14]) is False
assert check_valid_range(6, [1,6,7,14]) is True
assert check_valid_value(6, {'1':[1,5,7,14]}) == 6
assert check_valid_value(6, {'1':[1,6,7,14]}) == 0

# 4. Main Application
if __name__ == '__main__':
    example_inputs = read_input_to_str("Day_16/example_input.txt")
    inputs = read_input_to_str("Day_16/input.txt")

    # 1. parse input
    rules, my_ticket, nearby_tickets = read_tickets(example_inputs)

    # 2. count invalid tickets
    print(error_rate(nearby_tickets, rules))

    rules, my_ticket, nearby_tickets = read_tickets(inputs)
    print(error_rate(nearby_tickets, rules))
