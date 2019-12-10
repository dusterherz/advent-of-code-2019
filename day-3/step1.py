def get_data():
    file = open('inputs.txt', 'r')
    wires = []
    for line in file:
        wires.append([value for value in line.split(',')])
    return wires


def getDelta(direction):
    dxy = {
        'U': (1, 0),
        'D': (-1, 0),
        'L': (0, -1),
        'R': (0, 1),
    }
    return dxy[direction]


def convert_wires_to_map(wires):
    map = [[0 for i in range(9000)] for j in range(9000)]
    for wire in wires:
        x = 0
        y = 0
        for path in wire:
            direction = path[:1]
            distance = int(path[1:])
            dx, dy = getDelta(direction)
            if dx:
                for i in range(x + dx, x + (dx * (distance)), dx):
                    map[i][y] += 1
                x = x + (dx * distance) 
            if dy:
                for j in range(y + dy, y + (dy * (distance)), dy):
                    map[x][j] += 1
                y = y + (dy * distance)
                if x < 0 or y < 0: print('FUUUUUUCK')
            map[x][y] += 1
    return map

def find_all_junctions_distances(map):
    junctions = []
    for x, line in enumerate(map):
        for y, value in enumerate(line):
            if value >= 2:
                junctions.append((x, y))
    return junctions

def main():
    wires = get_data()
    map = convert_wires_to_map(wires)
    junctions = find_all_junctions_distances(map)
    print(junctions)
    print(min(junctions))


if __name__ == "__main__":
    main()
