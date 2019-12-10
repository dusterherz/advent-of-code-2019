from step1 import execute, get_data


def main():
    for noun in range(0, 99):
        for verb in range(0, 99):
            intcode = get_data(noun, verb)
            execute(intcode)
            if intcode[0] == 19690720:
                print(str(noun).zfill(2) + str(verb).zfill(2))


if __name__ == "__main__":
    main()
