import re


def populate_path(wire):

    path = {(0, 0)}
    x = 0
    y = 0

    for inst in wire:
        temp = re.compile("([a-zA-Z]+)([0-9]+)")
        dir, steps = temp.match(inst).groups()
        steps = int(steps)

        h = 1 if dir == 'R' else -1 if dir == 'L' else 0
        v = 1 if dir == 'U' else -1 if dir == 'D' else 0

        for _ in range(steps):
            x += h
            y += v
            path.add((x, y))

    return path


def main():
    with open("inputs/input.txt", "r") as f:
        wires = f.read()
        wires = wires.split("\n")

    wire1 = wires[0].split(",")
    wire2 = wires[1].split(',')

    path1 = populate_path(wire1)
    path2 = populate_path(wire2)

    intersections = [point for point in path1 if point in path2]

    dist = [abs(x) + abs(y) for (x,y) in intersections]
    dist.sort()

    print(dist[1])


if __name__ == "__main__":
    main()