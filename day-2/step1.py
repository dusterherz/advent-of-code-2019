def get_data(noun, verb):
    file = open('inputs.txt', 'r')
    data = []
    for line in file:
        values = [int(i) for i in line.split(',')]
        data += values
    data[1] = noun
    data[2] = verb
    return data


def execute(intcode):
    for i in range(0, len(intcode), 4):
        if intcode[i] == 1:
            result = intcode[i + 3]
            a = intcode[i + 1]
            b = intcode[i + 2]
            intcode[result] = intcode[a] + intcode[b]
        elif intcode[i] == 2:
            result = intcode[i + 3]
            a = intcode[i + 1]
            b = intcode[i + 2]
            intcode[result] = intcode[a] * intcode[b]
        elif intcode[i] == 99:
            break


def main():
    intcode = get_data(12, 2)
    execute(intcode)
    print(intcode[0])


if __name__ == "__main__":
    main()
