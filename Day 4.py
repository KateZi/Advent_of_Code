def is_valid(password):
    prev = 0
    super_prev = 0

    has_double = False

    password = str(password)

    if len(password) != 6: return False

    for d in password:
        d = int(d)
        if d < prev: return False
        #case of 3 in a row
        if d == super_prev and d == prev:
            has_double = False
        #case 2 in a row now found
        elif d == prev:
            has_double = True
        #case 2 in a row has finished
        elif has_double:
            break
        super_prev = prev
        prev = d

    return has_double


def count_in_range(rng):
    count = 0

    for password in range(rng[0], rng[1]):
        count += 1 if is_valid(password) else 0

    return count


def test():
    passowrds = [112233, 123444, 111122, 123456, 122334, 112345, 123455, 112222, 111234, 112344]
    correct = [True, False, True, False, True, True, True, True, False, True]

    result = list(map(is_valid, passowrds))

    assert result == correct, print(result)


def main():
    with open("inputs/Day 4 input", "r") as f:
        rng = list(map(int, f.read().split('-')))

    print(count_in_range(rng))


if __name__=='__main__':
    main()

