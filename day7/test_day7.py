from day7 import solve

DAY = "7"

data = []
with open(f"./day{DAY}/day{DAY}input.txt") as f:
    data = f.readlines()


def test_one():
    expected = 1423358
    actual = solve(data)[0]
    assert expected == actual


def test_two():
    expected = 545729
    actual = solve(data)[1]
    assert expected == actual
