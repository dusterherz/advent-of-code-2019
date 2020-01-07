def get_data():
    file = open('inputs.txt', 'r')
    wires = []
    for line in file:
        wires.append([value for value in line.split(',')])
    return wires


def getDelta(direction):
    dxy = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0),
    }
    return dxy[direction]


def convert_wires_to_map(wires):
    map = {}
    for wire_i, wire in enumerate(wires):
        x = 0
        y = 0
        for path in wire:
            direction = path[:1]
            distance = int(path[1:])
            dy, dx = getDelta(direction)
            if dx != 0:
                for i in range(x, x + distance * dx, dx):
                    if not (i, y) in map:
                        map[(i, y)] = wire_i
                    elif map[(i, y)] != wire_i:
                        map[(i, y)] = 'x'
                x += distance * dx
            if dy != 0:
                for i in range(y, y + distance * dy, dy):
                    if not (x, i) in map:
                        map[(x, i)] = wire_i
                    elif map[(x, i)] != wire_i:
                        map[(x, i)] = 'x'
                y += distance * dy
    return map


def find_all_junctions_distances(map):
    junctions = []
    for (x, y), value in map.items():
        if value == "x":
            junctions.append({'x': x, 'y': y, 'distance': abs(x) + abs(y)})
    return junctions


def main():
    wires = get_data()
    map = convert_wires_to_map(wires)
    junctions = find_all_junctions_distances(map)
    junctions.sort(key=lambda item: item['distance'])
    print(junctions[1])  # First match is 0, 0


if __name__ == "__main__":
    main()
