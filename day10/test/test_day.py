from template import day

DAY = "x"

data = []
# with open(file=f"./day{DAY}/day{DAY}input.txt", mode="r", encoding="utf8") as f:
#     data = f.readlines()

testdata = []
# with open(file=f"./day{DAY}/testday{DAY}input.txt", mode="r", encoding="utf8") as f:
#     testData = f.readlines()


def test_partOne():
    expected = "foo"

    actual = day.solve(data)
    assert expected == actual
