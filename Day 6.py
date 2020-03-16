orbits = dict()


def count_orbits(planet, sum):

    p = orbits.get(planet)

    if p is None:
        return 1

    for pl in p:
        sum += count_orbits(pl, 1)

    return sum


def main():
    with open("inputs/Map Data", "r") as f:
        for line in f:
            planets = line.split(")")
            planets[1] = planets[1].rstrip("\n")

            if planets[0] in orbits.keys():
                orbits[planets[0]].append(planets[1])
            else:
                orbits[planets[0]] = [planets[1]]

    num_orbits = 0
    for key in orbits.keys():
        num_orbits += count_orbits(key, 0)

    print(num_orbits)


if __name__=='__main__':
    main()

