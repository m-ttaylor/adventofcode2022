from day11 import day11

DAY = "11"

data = []
with open(file=f"./day{DAY}/day{DAY}input.txt", mode="r", encoding="utf8") as f:
    data = f.readlines()

testdata = []
with open(file=f"./day{DAY}/testday{DAY}input.txt", mode="r", encoding="utf8") as f:
    testData = f.readlines()


def test_partOneTestData():
    expected = 10605

    actual = day11.solve(testData, 1, 20)
    assert expected == actual


def test_partOneRealData():
    expected = 61503

    actual = day11.solve(data, 1, 20)
    assert expected == actual


def test_partTwoTestData():
    expected = 2713310158

    actual = day11.solve(testData, 2, 10000)
    assert expected == actual


def test_partTwoRealData():
    expected = 14081365540

    actual = day11.solve(data, 2, 10000)
    assert expected == actual
