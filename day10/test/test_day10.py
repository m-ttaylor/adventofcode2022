from day10 import day10

DAY = "10"

data = []
# with open(file=f"./day{DAY}/day{DAY}input.txt", mode="r", encoding="utf8") as f:
#     data = f.readlines()

testdata = []
with open(file=f"./day{DAY}/testday{DAY}input.txt", mode="r", encoding="utf8") as f:
    testData = f.readlines()


def test_partOneTestData():
    expected = 13140

    actual = day10.simulate(testData)
    assert expected == actual
