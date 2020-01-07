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
        step = 0
        for path in wire:
            direction = path[:1]
            distance = int(path[1:])
            dy, dx = getDelta(direction)
            if dx != 0:
                for i in range(x, x + distance * dx, dx):
                    if not (i, y) in map:
                        map[(i, y)] = {
                            'intersection': False,
                            'wire': wire_i,
                            'step': step
                        }
                    elif map[(i, y)]['wire'] != wire_i and map[
                        (i, y)]['intersection'] is not True:
                        map[(i, y)] = {
                            'intersection': True,
                            'wire': wire_i,
                            'step': step + map[(i, y)]['step']
                        }
                    step += 1
                x += distance * dx
            if dy != 0:
                for i in range(y, y + distance * dy, dy):
                    if not (x, i) in map:
                        map[(x, i)] = {
                            'intersection': False,
                            'wire': wire_i,
                            'step': step
                        }
                    elif map[(x, i)]['wire'] != wire_i and map[
                        (x, i)]['intersection'] is not True:
                        map[(x, i)] = {
                            'intersection': True,
                            'wire': wire_i,
                            'step': step + map[(x, i)]['step']
                        }
                    step += 1
                y += distance * dy
    return map


def find_all_junctions_distances(map):
    junctions = []
    for (x, y), value in map.items():
        if value['intersection'] == True:
            junctions.append({
                'x': x,
                'y': y,
                'distance': abs(x) + abs(y),
                'step': value['step']
            })
    return junctions


def main():
    wires = get_data()
    map = convert_wires_to_map(wires)
    junctions = find_all_junctions_distances(map)
    junctions.sort(key=lambda item: item['distance'])
    print(f"Nearest Intersection: {junctions[1]}")  # First match is 0, 0
    junctions.sort(key=lambda item: item['step'])
    print(
        f"Quickest Intersection (step): {junctions[1]}")  # First match is 0, 0


if __name__ == "__main__":
    main()
