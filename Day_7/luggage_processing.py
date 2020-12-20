from typing import List, Dict

"""
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""


def read_input(filepath: str) -> str:
    with open(filepath) as f:
        output = f.read()
    return output


def extract_bag_rules(data: str) -> List[List[str]]:
    # 1. split each line on contain and ,
    # -> first replace contain with , then split on ,
    lines = data.replace(' contain', ',').split('\n')
    line_split = [line.split(', ') for line in lines]

    # 2. built dict: key=each bag color and values=containing bags
    colors = [rule[0].replace(' bags', '') for rule in line_split]
    # rules = [rule[1:] for rule in line_split]

    rules = []
    for rule in line_split:
        # rule[1:] = ['1 bright white bag', '2 muted yellow bags.']
        dict_i = dict()
        for rule_i in rule[1:]:
            rule_i_parts = rule_i.split()
            rule_i_color = ' '.join(rule_i_parts[1:3])

            # check if no other bags
            if 'no' not in rule_i_parts[0]:
                rule_i_number = int(rule_i_parts[0])
                dict_i[rule_i_color] = rule_i_number

        rules.append(dict_i)

    bag_rules = dict(zip(colors, rules))

    return bag_rules


def can_contain_gold_bag(bag: str, bag_rules: Dict[str, Dict]) -> bool:
    # 1. search direct childs
    # -> break condition
    bag_contains = bag_rules.get(bag, dict())
    if "shiny gold" in bag_contains.keys():
        return True

    # 2. recursively search subchilds
    contain_gold_bag = False
    for subbag_i in bag_contains.keys():
        contain_gold_bag |= can_contain_gold_bag(subbag_i, bag_rules)

    return contain_gold_bag


def bags_containting_gold_bag(data: str) -> int:
    """
    How many bag colors can eventually contain at least one shiny gold bag?
    """
    # 1. parse bag rules
    bag_rules = extract_bag_rules(data)

    # 2. check for every key recursively if it can contain the gold bag
    n_bags_containing_gold_bag = 0
    for bag in bag_rules.keys():
        n_bags_containing_gold_bag += can_contain_gold_bag(bag, bag_rules)

    return n_bags_containing_gold_bag


if __name__ == '__main__':
    # 1. How many bag colors can eventually contain at least one shiny gold bag?
    example_inputs = read_input("Day_7/example_input.txt")
    inputs = read_input("Day_7/input.txt")

    print(bags_containting_gold_bag(example_inputs))
    print(bags_containting_gold_bag(inputs))
