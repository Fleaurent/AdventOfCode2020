'''
acc increases or decreases a single global value called the accumulator
jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the argument as an offset from the jmp instruction
nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next
''' 
from typing import List
import copy


def read_input(filepath: str) -> str:
    output = ""
    with open(filepath) as f:
        output = f.read()
    return output


class Command:
    def __init__(self, command: str, value: int):
        self.command = command
        self.value = value

    def __str__(self):
        return f"{self.command}: {self.value}"


def parse_input(input: str) -> List[Command]:
    commands = []
    for line in input.splitlines():
        command, value = line.split(sep=' ')
        temp_command = Command(command, int(value))
        commands.append(temp_command)
    return commands


class Statemachine:
    def __init__(self):
        self.accumulator = 0
        self.instruction_ptr = 0
        self.visited_instructions = []
    
    def mark_visited(self):
        self.visited_instructions.append(self.instruction_ptr)

    def update_state(self, command: str, value: int):
        if(command == 'acc'):
            self.instruction_ptr += 1
            self.accumulator += value
        elif(command == 'jmp'):
            self.instruction_ptr += value
        elif(command == 'nop'):
            self.instruction_ptr += 1

    def check_visited(self) -> bool:
        return self.instruction_ptr not in self.visited_instructions


def detect_loop(commands: List[Command]) -> int:
    n_commands = len(commands)
    statemachine = Statemachine()
    statemachine.instruction_ptr = 0

    while(statemachine.check_visited()):
        command = commands[statemachine.instruction_ptr].command
        value = commands[statemachine.instruction_ptr].value

        statemachine.mark_visited()
        statemachine.update_state(command, value)

        if(statemachine.instruction_ptr > n_commands):
            break

    return statemachine.accumulator


def detect_loop2(commands: List[Command]) -> int:
    n_commands = len(commands)
    result = 0

    for i in range(n_commands):
        # temp_commands = commands # bug: only reference
        # temp_commands = commands.copy() # bug: shallow copy
        # temp_commands = list(commands) # bug: shallow copy
        temp_commands = copy.deepcopy(commands)

        if commands[i].command == 'nop': 
            temp_commands[i].command = 'jmp'
        elif commands[i].command == 'jmp':
            temp_commands[i].command = 'nop'

        statemachine = Statemachine()
        statemachine.instruction_ptr = 0

        while(statemachine.check_visited()):
            command = temp_commands[statemachine.instruction_ptr].command
            value = temp_commands[statemachine.instruction_ptr].value

            statemachine.mark_visited()
            statemachine.update_state(command, value)

            if(statemachine.instruction_ptr > n_commands - 2):
                print(f"success {i}: {statemachine.accumulator}")
                result = statemachine.accumulator
                break

    return result


if __name__ == '__main__':
    output = read_input("Day_8/example_input.txt")
    commands = parse_input(output)
    print(detect_loop(commands))

    output = read_input("Day_8/input.txt")
    commands = parse_input(output)
    print(detect_loop(commands))

    print(detect_loop2(commands))
    print("Done")
