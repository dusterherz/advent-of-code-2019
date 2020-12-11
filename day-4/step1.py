import re


def get_data():
    file = open('inputs.txt', 'r')
    line = file.readline()
    value_range = (int(value) for value in line.split('-'))
    return value_range


def test_increment_digits(str_value):
    past_digit = str_value[0]
    for digit in str_value[1:]:
        if digit < past_digit:
            return False
        past_digit = digit
    return True

def test_duplicate_digits(str_value):
    for i, digit in enumerate(str_value, start=1):
        if digit in str_value[i:]:
            return True
    return False

if __name__ == "__main__":
    value_range = get_data()
    matching = []
    for value in range(*value_range):
        if value < 100000:
            continue
        str_value = str(value)
        if not test_increment_digits(str_value):
            continue
        if not test_duplicate_digits(str_value):
            continue
        matching.append(value)
    print(matching)
    print(len(matching))
