DAY = "5"
from day5.day5 import CrateStack
from day5 import day5

data = []
with open(f"./day{DAY}/day{DAY}input.txt") as f:
    data = f.readlines()

a = "[A]"
b = "[B]"
c = "[C]"
d = "[D]"
e = "[E]"
f = "[F]"
g = "[G]"
h = "[H]"
i = "[I]"
j = "[J]"
k = "[K]"
l = "[L]"
m = "[M]"
n = "[N]"
o = "[O]"
p = "[P]"
q = "[Q]"
r = "[R]"
s = "[S]"
t = "[T]"
u = "[U]"
v = "[V]"
w = "[W]"
x = "[X]"
y = "[Y]"
z = "[Z]"


def test_canAddCrateToStack():
    expected = CrateStack([a])

    stackA = CrateStack()
    stackA.addCrate(a)

    assert expected == stackA


def test_canRemoveCrateFromStack():
    expected = CrateStack()
    stackA = CrateStack()
    stackA.addCrate(a)
    crate = stackA.takeCrate()

    assert expected == stackA
    assert crate == a


def test_addAndRemoveSeveral():

    expected = CrateStack()

    stackA = CrateStack()
    stackA.addCrate(a)
    stackA.addCrate(b)
    stackA.addCrate(c)

    removed = []

    for _ in range(3):
        removed.append(stackA.takeCrate())

    assert expected == stackA
    assert [c, b, a]


def test_moveCrates():
    stackA = CrateStack()
    stackB = CrateStack()

    stackA.addCrate(a)
    stackB.addCrate(b)
    stacks = [stackA, stackB]
    day5.parseCommand(stacks, "move 1 from 1 to 2")

    assert CrateStack() == stackA
    assert CrateStack([b, a]) == stackB


def test_readTops_shouldReturnEmptyWhenEmpty():

    actual = day5.readTops([CrateStack([]), CrateStack([]), CrateStack([])])
    # print('DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG', stacks)
    assert "" == actual


def test_readTops_shouldReturnCorrectResultWithStacksOfOne():

    stacks = [CrateStack([a]), CrateStack([b]), CrateStack([c])]

    assert "ABC" == day5.readTops(stacks)


def test_readTops_shouldReturnCorrectResultWithUnevenStacks():

    stacks = [CrateStack([a]), CrateStack([b, c, d, e, f, g]), CrateStack([h])]

    assert "AGH" == day5.readTops(stacks)


def test_parseStacksShouldParseCorrecrtly():
    expected = [
        CrateStack([z]),
        CrateStack([m, c, d]),
        CrateStack([p]),
        CrateStack([s]),
        CrateStack([y]),
        CrateStack([r, l]),
        CrateStack([v]),
    ]
    testData = []
    with open("./day5/testinput3.txt") as f:
        testData = f.readlines()

    stacks, _ = day5.splitData(testData)

    parsed = day5.parseStacks(stacks)
    print("expected: ", expected)
    print("parsed: ", parsed)

    assert expected == parsed


def test_part1HasRightSolution():

    expected = "LJSVLTWQM"
    actual = day5.solve(data)

    assert expected == actual


def test_part2HasRightSolution():
    expected = "BRQWDBBJM"
    actual = day5.solve(data, "9001")

    assert expected == actual
