import re


def populate_path(wire):

    path = {(0, 0): 0}
    x = 0
    y = 0
    step = 0

    for inst in wire:
        temp = re.compile("([a-zA-Z]+)([0-9]+)")
        dir, steps = temp.match(inst).groups()
        steps = int(steps)

        h = 1 if dir == 'R' else -1 if dir == 'L' else 0
        v = 1 if dir == 'U' else -1 if dir == 'D' else 0

        for _ in range(steps):
            x += h
            y += v
            step += 1
            path[(x, y)] = step

    return path


def calc_closest(intersections):
    dist = [abs(x) + abs(y) for (x, y) in intersections]
    dist.sort()
    return dist[1]


def calc_efficient(path1, path2, intersections):
    min_steps = [path1[intersection] + path2[intersection] for intersection in intersections]
    min_steps.sort()
    return min_steps[1]


def main():
    with open("inputs/Wires input", "r") as f:
        wires = f.read()
        wires = wires.split("\n")

    for i in range(0, len(wires), 2):
        wire1 = wires[i].split(",")
        wire2 = wires[i+1].split(',')

        path1 = populate_path(wire1)
        path2 = populate_path(wire2)

        intersections = path1.keys() & path2.keys()

        closest = calc_closest(intersections)
        efficient = calc_efficient(path1, path2, intersections)

        print(efficient)


if __name__ == "__main__":
    main()