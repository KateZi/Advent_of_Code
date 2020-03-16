class Planet:

    def __init__(self, name):
        self.name = name
        self.moons = list()
        self.star = None

    def add_moon(self, moon):
        self.moons.append(moon)

    def add_star(self, star):
        self.star = star

class Universe:

    def __init__(self):
        self.planets = list()

    def iter(self):
        for planet in self.planets:
            yield planet

    def add_planet(self, planet):
        self.planets.append(planet)

    def planet_names(self):
        names = list()
        for planet in self.planets:
            names.append(planet.name)
        return names

    def get_planet(self, name):
        for planet in self.planets:
            if planet.name == name:
                return planet

        return -1

my_planets = Universe()

def count_orbits(instance):
    planets = instance.split(')')
    planets[1] = planets[1].rstrip("\n")

    if planets[0] not in my_planets.planet_names():
        planet = Planet(planets[0])
        my_planets.add_planet(planet)
    else:
        planet = my_planets.get_planet(planets[0])

    moon = Planet(planets[1])
    moon.add_star(planet)
    planet.add_moon(moon)

with open("inputs/Test Map Data", "r") as f:
    for line in f:
        count_orbits(line)

for planet in my_planets.iter():
    print(planet.name)
    print(planet.moons)
    print(planet.star)