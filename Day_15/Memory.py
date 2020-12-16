from typing import List, Tuple, Set, Union


class Memory():
    def __init__(self, starting_numbers: List[int]):
        self.numbers = starting_numbers

    def next_turn(self):
        last_numbers = self.numbers[:-1]
        recent_number = self.numbers[-1]
        turn = len(self.numbers) - 1

        if recent_number in last_numbers:
            last_turn = len(last_numbers) - 1 - last_numbers[::-1].index(recent_number)
            self.numbers.append(turn - last_turn)
        else:
            self.numbers.append(0)

    def run_turns(self, n: int) -> int:
        while(len(memory.numbers) < n):
            self.next_turn()

        return self.numbers[-1]


'''
class Memory2():
    def __init__(self, starting_numbers: List[int]):
        self.numbers = []
        self.turns = dict()
        self.init_numbers(starting_numbers)

    def init_numbers(self, starting_numbers: List[int]):
        self.turns = dict()
        self.numbers = []
        for i, starting_number in enumerate(starting_numbers):
            self.numbers.append(starting_number)
            self.turns[starting_number] = i

    def run_turn(self, number: int, turn: int):
        # number = self.numbers[-1]
        turn = len(self.numbers)
        last_turn = self.turns[number]

        if last_turn == turn:
            new_number = 0
            self.numbers.append(new_number)
            self.turns[new_number] = turn
        else:
            new_number = turn - last_turn
            self.numbers.append(new_number)

            
        print(number, new_number, turn)

    def next_turn(self):
        number = self.numbers[-1]
        turn = len(self.numbers)
        self.run_turn(number, turn)
'''

if __name__ == '__main__':
    example_inputs1 = [0,3,6]  # 436
    example_inputs2 = [1,3,2]  # 1
    example_inputs3 = [2,1,3]  # 10
    example_inputs4 = [1,2,3]  # 27
    example_inputs5 = [2,3,1]  # 78
    example_inputs6 = [3,2,1]  # 438
    example_inputs7 = [3,1,2]  # 1836

    memory = Memory(example_inputs1)
    print(memory.run_turns(2020))
    assert memory.run_turns(2020) == 436

    memory = Memory(example_inputs2)
    assert memory.run_turns(2020) == 1


    inputs = [6,19,0,5,7,13,1]
    memory = Memory(inputs)
    print(memory.run_turns(2020))

    inputs = [6,19,0,5,7,13,1]
    memory = Memory(inputs)
    print(memory.run_turns(30_000_000))
    
