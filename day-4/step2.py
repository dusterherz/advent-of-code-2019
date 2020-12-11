import re
import step1

def test_biggest_group(str_value):
    groups = [{"digit": str_value[0], "number": 1}]
    past_digit = str_value[0]

    # order digits by group and find the biggest one
    for digit in str_value[1:]:
        if digit == past_digit:
            groups[-1]["number"] += 1
        else:
            groups.append({"digit": digit, "number": 1})
            past_digit = digit
    filtered_group = [group for group in groups if group['number'] == 2]
    if len(filtered_group) > 0:
        return True
    return False

if __name__ == "__main__":
    value_range = step1.get_data()
    matching = []
    for value in range(*value_range):
        if value < 100000:
            continue
        str_value = str(value)
        if not step1.test_increment_digits(str_value):
            continue
        if not step1.test_duplicate_digits(str_value):
            continue
        if not test_biggest_group(str_value):
            continue
        matching.append(value)
    print(matching)
    print(len(matching))
