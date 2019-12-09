import math


def get_data():
    file = open('inputs.txt', 'r')
    data = []
    for line in file:
        data.append(int(line))
    return data


def calculate_fuel(mass):
    return int(math.floor(mass / 3)) - 2


def main():
    modules = get_data()
    sum = 0
    for module_mass in modules:
        sum += calculate_fuel(module_mass)
    print(sum)


if __name__ == "__main__":
    main()
