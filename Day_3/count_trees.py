from pathlib import Path

print(Path.cwd())
print("test")


def traverse_forest(filepath: str) -> int:
    n_trees = 0

    with open(filepath) as f:
        lines = f.readlines()
        n_rows = len(lines)
        n_cols = len(lines[0]) - 1
        # print(n_rows, n_cols)

        for row_i, row in enumerate(lines):
            col_i = (row_i * 3) % n_cols

            if(row[col_i] == '#'):
                n_trees += 1

            # print(row_i, col_i)
            # print(row[col_i])

    return n_trees


def traverse_forest2(filepath: str, right: int, down: int) -> int:
    n_trees = 0

    with open(filepath) as f:
        lines = f.readlines()
        n_rows = len(lines)
        n_cols = len(lines[0]) - 1
        # print(n_rows, n_cols)

        step = 0
        for row_i, row in enumerate(lines):
            if row_i % down:
                continue

            col_i = (step * right) % n_cols
            if(row[col_i] == '#'):
                n_trees += 1

            step += 1

            # print(row_i, col_i)
            # print(row[col_i])

    return n_trees


if __name__ == '__main__':
    # print(traverse_forest("Day_3/example_input.txt"))
    print(traverse_forest("Day_3/input.txt"))

    # print(traverse_forest2("Day_3/example_input.txt", right=1, down=1))
    # print(traverse_forest2("Day_3/example_input.txt", right=3, down=1))
    # print(traverse_forest2("Day_3/example_input.txt", right=5, down=1))
    # print(traverse_forest2("Day_3/example_input.txt", right=7, down=1))
    # print(traverse_forest2("Day_3/example_input.txt", right=1, down=2))

    val = 1
    val *= traverse_forest2("Day_3/input.txt", right=1, down=1)
    val *= traverse_forest2("Day_3/input.txt", right=3, down=1)
    val *= traverse_forest2("Day_3/input.txt", right=5, down=1)
    val *= traverse_forest2("Day_3/input.txt", right=7, down=1)
    val *= traverse_forest2("Day_3/input.txt", right=1, down=2)
    print(val)
