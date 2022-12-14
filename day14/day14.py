lines = None
with open("day14/testinput.txt") as f:
    lines = f.read().split("\n")

lines = [line.split(" -> ") for line in lines]

grid = [["."] * 520 for _ in range(10)]

for line in lines:
    for vector in line:
        print(vector)
        c, r = vector.split(",")
        grid[int(r)][int(c)] = "#"
    # # y = [z.split(",") for z in x]
# print(coords)
# for line in coords:
#     for coord in line:
#         foo = (a, b) = coord.split(",")
#         print(foo)
#     # print(y)


def printGrid(grid):
    for row in grid:
        # print(row)
        print("".join(row[480:]))


printGrid(grid)
