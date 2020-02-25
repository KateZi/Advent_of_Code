def calc_fuel(mass):
    if mass <= 0: return 0
    else:
        fuel = mass//3 - 2
        temp = calc_fuel(fuel)
        return fuel + temp if temp > 0 else fuel


def calc_total():
    M = 0
    with open("Fuel_input", "r") as f:
        masses = f.readlines()
    for mass in masses:
        M += calc_fuel(int(mass))

    print(M)

# print(calc_fuel(100756))
calc_total()