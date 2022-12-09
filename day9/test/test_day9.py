from day9 import day9

DAY = "9"

data = []
with open(file=f"./day{DAY}/day{DAY}input.txt", mode="r", encoding="utf8") as f:
    data = f.readlines()

testdata = []
with open(file=f"./day{DAY}/testday{DAY}input.txt", mode="r", encoding="utf8") as f:
    testData = f.readlines()


def test_partOneTestData():
    expected = 13

    actual = day9.solve(testData, [[0, 0], [0, 0]])
    assert expected == actual
