def is_valid(password):
    prev = 0
    count = dict()

    password = str(password)

    if len(password) != 6: return False

    for d in password:
        d = int(d)
        if d not in count.keys():
            count[d] = 1
        if d < prev:
            return False
        if d == prev:
            count[d] = count.get(d) + 1
        prev = d

    return 2 in count.values()


def count_in_range(rng):
    count = 0

    for password in range(rng[0], rng[1]):
        count += 1 if is_valid(password) else 0

    return count


def test():
    valid_passwords = [112233, 111122, 122334, 112345, 123455, 112222, 112344, 133344, 111233]
    invalid_passwords = [123444, 123456, 111234, 111111, 111222, 111234]

    valid_result = list(map(is_valid, valid_passwords))
    invalid_result = list(map(is_valid, invalid_passwords))

    assert valid_result == len(valid_result)*[True], print(valid_result)
    assert invalid_result == len(invalid_result) * [False], print(invalid_result)


def main():
    with open("inputs/Day 4 input", "r") as f:
        rng = list(map(int, f.read().split('-')))

    print(count_in_range(rng))


if __name__=='__main__':
    main()

