testfile = "day14/testinput.txt"
file = "day14/input.txt"
filetouse = file


def ints(line: str) -> list[int]:
    "find and return all ints in string separated by spaces or commas"
    values = []
    for chunk in line.strip().replace(",", " ").split(" "):
        value: int = None
        try:
            value = int(chunk)
        except ValueError:
            pass
        else:
            values.append(value)

    return values


def printGrid(g):
    labels = [str(l) for l in [wmin, 500, 503]]
    for i in range(3):
        print(
            f"     {labels[0][i]}{' '*((500-wmin)-1)}{labels[1][i]}{' '*((w-500)-1)}{labels[2][i]}"
        )

    for i, row in enumerate(g):
        # print(row)
        rowLabel = ""
        if i < 10:
            rowLabel = f"  {i}"
        elif i < 100:
            rowLabel = f" {i}"
        else:
            rowLabel = f"{i}"

        print(f"{rowLabel}  {''.join(row[wmin-20:])}")


lines = None
# with open("day14/testinput.txt") as f:
#     lines = f.read().split("\n")

# w, h = 504, 10
# wmin = 490
w, h, wmin, w2, h2, wmin2 = None, None, None, None, None, None
offset = 2000
with open(filetouse) as f:
    data = f.read()
    bounds = ints(data)
    h = max(i for i in bounds if i < 200)
    h2 = h + 2
    w = max(i for i in bounds) + 1
    w2 = w + offset * 2
    # wmin = w - 9
    wmin = min(i for i in bounds if i > 200)
    wmin2 = wmin - 40
    print(f"calculated bounds as x: {wmin}-{w}, h: 0-{h}")
    lines = [l.split(" -> ") for l in data.split("\n")]

grid = [["."] * (w + 1) for _ in range(h + 1)]
grid2 = [["."] * (w2 + 2) for _ in range(h2 + 1)]
sandOrigin = (0, 500)
sandOrigin2 = (0, 500 + offset)
grid[sandOrigin[0]][sandOrigin[1]] = "+"
grid2[sandOrigin2[0]][sandOrigin2[1]] = "+"
for i in range(w2):
    grid2[h2][i] = "#"

# printGrid(grid2)
# grid[1][500] = "!" # ok, so we know rows increasing -> lower in graph

for line in lines:

    for p1, p2 in zip(line, line[1:]):

        x1, y1 = map(int, p1.split(","))
        x2, y2 = map(int, p2.split(","))

        if x1 < x2:
            for x in range(x1, x2 + 1):
                grid[y1][x] = "#"
                grid2[y1][x + offset] = "#"
        elif x1 > x2:
            for x in range(x1, x2 - 1, -1):
                grid[y1][x] = "#"
                grid2[y1][x + offset] = "#"
        elif y1 < y2:
            for y in range(y1, y2 + 1):
                grid[y][x1] = "#"
                grid2[y][x1 + offset] = "#"
        elif y1 > y2:
            for y in range(y1, y2 - 1, -1):
                grid[y][x1] = "#"
                grid2[y][x1 + offset] = "#"
# . . . . . . . . . . . . . . . . . . . . .
# left = (0, -1)
# down = (1, 0)
# right = (0, 1)

# printGrid(grid)
# printGrid(grid2)


def simulateGrain(grid, w, wmin, h, sandOrigin, sandCount):

    rested = False
    sandr, sandc = sandOrigin
    while not rested:
        if grid[sandr][sandc] == "o":
            # part 2 guard
            break
        inBoundsD = sandr + 1 <= h
        inBoundsDL = inBoundsD and sandc - 1 >= wmin
        inBoundsDR = inBoundsD and sandc + 1 <= w

        isFree = inBoundsD and grid[sandr + 1][sandc] == "."
        if isFree:
            # print(f"moving sand down one to ({sandc}, {sandr+1})")
            sandr += 1
            continue

        blockedDLeft = inBoundsDL and grid[sandr + 1][sandc - 1] in ["#", "o"]
        blockedDRight = inBoundsDR and grid[sandr + 1][sandc + 1] in ["#", "o"]

        if inBoundsDL and grid[sandr + 1][sandc - 1] not in ["#", "o"]:
            sandr += 1
            sandc -= 1
            continue

        if inBoundsDR and grid[sandr + 1][sandc + 1] not in ["#", "o"]:
            sandr += 1
            sandc += 1
            continue

        blockedDown = inBoundsD and grid[sandr + 1][sandc] in ["#", "o"]

        if blockedDown and blockedDLeft and blockedDRight:
            # print(f"came to a rest at ({sandc}, {sandr})")
            grid[sandr][sandc] = "o"
            sandCount += 1
            rested = True
        else:
            break
    return rested, sandCount


def simulate(g):
    sandCount = 0

    grainsKeepResting = True
    while grainsKeepResting:
        grainsKeepResting, sandCount = simulateGrain(
            g, w, wmin, h, sandOrigin, sandCount
        )
        # sandCount += 1
    # printGrid(g)
    print("======")
    print(sandCount)


def simulatePart2(g2):
    sandCount = 0

    grainsKeepResting = True
    while grainsKeepResting:
        grainsKeepResting, sandCount = simulateGrain(
            g2, w2, wmin2, h2, sandOrigin2, sandCount
        )
        # sandCount += 1
    # printGrid(g)
    print("======")
    print(sandCount)


simulate(grid)
simulatePart2(grid2)

# 769 is too high
# 753 is too low

# part2 1213 is too low
# 2905 is too low
# 5282 is too low
# 26686 is right
