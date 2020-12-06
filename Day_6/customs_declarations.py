def count_customs_declarations(filepath: str) -> int:
    with open(filepath) as f:
        input_str = f.read()

    # 1. split groups
    groups = input_str.split('\n\n')

    # 2. search each group
    n_declarations = 0
    for group in groups:
        n_declarations += group_declarations(group)

    return n_declarations


def group_declarations(group_input: str) -> int:
    declarations = set()
    persons = group_input.split('\n')
    for person in persons:
        for answer in person:
            declarations.add(answer)
    return len(declarations)


def count_customs_declarations2(filepath: str) -> int:
    with open(filepath) as f:
        input_str = f.read()

    # 1. split groups
    groups = input_str.split('\n\n')

    # 2. search each group
    n_declarations = 0
    for group in groups:
        n_declarations += group_declarations2(group)

    return n_declarations


def group_declarations2(group_input: str) -> int:
    declarations = set()

    persons = group_input.split('\n')
    for i, person in enumerate(persons):
        declarations_person = set()
        for answer in person:
            declarations_person.add(answer)
        if(i == 0):
            declarations = declarations_person
        else:
            declarations.intersection_update(declarations_person)
    return len(declarations)


if __name__ == '__main__':
    print(count_customs_declarations('Day_6/example_input.txt'))
    print(count_customs_declarations('Day_6/input.txt'))

    print(count_customs_declarations2('Day_6/example_input.txt'))
    print(count_customs_declarations2('Day_6/input.txt'))
