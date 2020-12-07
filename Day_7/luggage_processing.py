from typing import List, Dict

input = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""


def bagsContaintingGoldBag(filepath: str) -> int:
    """
    How many bag colors can eventually contain at least one shiny gold bag?
    """
    data = ""
    with open(filepath) as f:
        data = f.read()

    bag_rules = extract_bag_rules(data)
    colors = bag_rules.keys()
    print(colors)

    """
    for color in colors:
        for rule_values in bag_rules.values():
            contains_color = color in rule_values[0]
    """
    contains_color = [[color in rule_values[0] for color in colors] for rule_values in bag_rules.values()]
    color_rules = dict(zip(colors, contains_color))
    print(color_rules)

    return 0


def extract_bag_rules(data: str) -> List[List[str]]:
    lines = data.replace(' contain', ',').split('\n')
    line_split = [line.split(', ') for line in lines]
    colors = [rule[0].replace(' bags', '') for rule in line_split]
    rules = [rule[1:] for rule in line_split]
    bag_rules = dict(zip(colors, rules))
    return bag_rules


if __name__ == '__main__':
    print(bagsContaintingGoldBag(filepath="Day_7/example_input.txt"))
    # print(bagsContaintingGoldBag(filepath="Day_7/input.txt"))
