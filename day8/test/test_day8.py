from day8 import day8

DAY = "8"

data = []
with open(file=f"./day{DAY}/day{DAY}input.txt", mode="r", encoding="utf8") as f:
    data = f.readlines()


def test_partOne():
    expected = 1782

    actual = day8.solve(data)[0]
    assert expected == actual


def test_testDataPart2():
    expected = 8
    testData = []
    with open(file=f"./day{DAY}/testday{DAY}input.txt", mode="r", encoding="utf8") as f:
        testData = f.readlines()
    actual = day8.solve(testData)[1]
    assert expected == actual


def test_partTwo():
    expected = 474606
    actual = day8.solve(data)[1]
    assert expected == actual
