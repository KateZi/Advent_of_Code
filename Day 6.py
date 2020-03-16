orbits = dict()

# Part 1
def count_orbits(planet, sum):

    p = orbits.get(planet)

    if p is None:
        return 1

    for pl in p:
        sum += count_orbits(pl, 1)

    return sum


def run_part1():
    num_orbits = 0
    for key in orbits.keys():
        num_orbits += count_orbits(key, 0)

    print(num_orbits)


# Part 2
def run_part2():



def main():
    with open("inputs/Map Data", "r") as f:
        for line in f:
            planets = line.split(")")
            planets[1] = planets[1].rstrip("\n")

            if planets[1] in orbits.keys():
                orbits[planets[1]].append(planets[0])
            else:
                orbits[planets[1]] = [planets[0]]

    run_part1()

if __name__=='__main__':
    main()

