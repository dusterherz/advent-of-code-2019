from step1 import calculate_fuel, get_data


def calculate_fuel_total(mass):
    value = calculate_fuel(mass)
    if value > 0:
        value += calculate_fuel_total(value)
        return value
    return 0


def main():
    modules = get_data()
    fuel_total = 0
    for module_mass in modules:
        fuel_total += calculate_fuel_total(module_mass)
    print(fuel_total)


if __name__ == "__main__":
    main()
