
def validate_passport(passport: str) -> bool:
    # OPTIONAL_KEYS = {"cid"}
    REQUIRED_KEYS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    passport_items = passport.strip().split()
    passport_keys = {item.split(sep=":")[0] for item in passport_items}
    missing_keys = REQUIRED_KEYS - passport_keys
    return len(missing_keys) == 0


def validate_passports(filepath: str) -> int:
    # run through the files: pass
    temp_passport = ""
    valid_passports = 0

    with open(file=filepath) as passports:
        lines = passports.readlines()
        for line in lines:
            temp_passport += " " + line.strip()

            if line == "\n":
                valid_passports += validate_passport(temp_passport)
                temp_passport = ""

        valid_passports += validate_passport(temp_passport)
    return valid_passports


def check_number(number: str, min: int, max: int):
    return min <= int(number) <= max


def check_height(height: str):
    valid_height = False
    if(height.endswith("cm")):
        valid_height |= check_number(number=height.strip("cm"), min=150, max=193)
    elif(height.endswith("in")):
        valid_height |= check_number(number=height.strip("in"), min=59, max=76)
    return valid_height


def check_hcl(hcl: str):
    # '#123def'
    valid_hcl = True
    valid_hcl &= len(hcl) == 7
    valid_hcl &= hcl.startswith('#')
    try:
        hcl_num = int(hcl[1:7], 16)
        valid_hcl &= True
    except ValueError:
        valid_hcl = False
    return valid_hcl

def check_ecl(ecl: str):
    VALID_COLORS = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    return ecl in VALID_COLORS

def check_pid(pid: str):
    # nine-digit number, including leading zeroes
    valid_pid = True
    if len(pid) == 9:
        try:
            pid_num = int(pid)
            valid_pid &= True
        except ValueError:
            valid_pid = False
    else:
        valid_pid = False
    return valid_pid

def validate_passport2(passport: str) -> bool:
    """
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    """
    passport_valid = True
    # OPTIONAL_KEYS = {"cid"}
    # REQUIRED_KEYS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    REQUIRED_KEYS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    passport_items = passport.strip().split()
    passport_dict = dict(item.split(sep=":") for item in passport_items)

    missing_keys = REQUIRED_KEYS - passport_dict.keys()

    if len(missing_keys) == 0:
        passport_valid &= check_number(number=passport_dict['byr'], min=1920, max=2002)
        passport_valid &= check_number(number=passport_dict['iyr'], min=2010, max=2020)
        passport_valid &= check_number(number=passport_dict['eyr'], min=2020, max=2030)
        passport_valid &= check_height(height=passport_dict['hgt'])
        passport_valid &= check_hcl(hcl=passport_dict['hcl'])
        passport_valid &= check_ecl(ecl=passport_dict['ecl'])
        passport_valid &= check_pid(pid=passport_dict['pid'])
    else:
        passport_valid = False

    return passport_valid


def validate_passports2(filepath: str) -> int:
    # run through the files: pass
    temp_passport = ""
    valid_passports = 0

    with open(file=filepath) as passports:
        lines = passports.readlines()
        for line in lines:
            temp_passport += " " + line.strip()

            if line == "\n":
                valid_passports += validate_passport2(temp_passport)
                temp_passport = ""

        valid_passports += validate_passport2(temp_passport)
    return valid_passports


if __name__ == '__main__':
    print(validate_passports(filepath="Day_4/example_input.txt"))
    print(validate_passports(filepath="Day_4/input.txt"))

    print(validate_passports2(filepath="Day_4/example_input.txt"))
    print(validate_passports2(filepath="Day_4/input.txt"))
