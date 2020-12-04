import pandas as pd


def validate_password(row) -> bool:
    # 0. get parts
    min_max = row[0].split("-")
    char = row[1].strip(":")
    password = row[2]

    # 1. count number of char in password
    n_char = password.count(char)

    # 2. check if n_char is in range
    min = int(min_max[0])
    max = int(min_max[1])

    return (n_char >= min) & (n_char <= max)


def validate_passwords(filepath: str) -> int:
    # 1. read data into pandas dataframe
    data = pd.read_csv(filepath_or_buffer=filepath, header=None, sep=" ")

    # 2. apply function to each row (axis=1)
    data['valid'] = data.apply(validate_password, axis=1)
    print(data['valid'])
    # 3. count valid passwords
    return len(data[data['valid'] == True])


def validate_password2(row) -> bool:
    # 0. get parts
    pos12 = row[0].split("-")
    char = row[1].strip(":")
    password = row[2]

    # 1. get positions of char
    pos1 = int(pos12[0])
    pos2 = int(pos12[1])

    # 2. check if char exist only once at the positions
    if len(password) < pos2:
        return False
    if len(password) < pos1:
        return False

    return (password[pos1-1] == char) ^ (password[pos2-1] == char)


def validate_passwords2(filepath: str) -> int:
    # 1. read data into pandas dataframe
    data = pd.read_csv(filepath_or_buffer=filepath, header=None, sep=" ")

    # 2. apply function to each row (axis=1)
    data['valid'] = data.apply(validate_password2, axis=1)
    print(data['valid'])

    # 3. count valid passwords
    return len(data[data['valid'] == True])


if __name__ == '__main__':
    print("Hello World")

    print(validate_passwords("example_input.txt"))
    print(validate_passwords("input.txt"))

    print(validate_passwords2("example_input.txt"))
    print(validate_passwords2("input.txt"))
