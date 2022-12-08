"""--- Day 8: Treetop Tree House ---"""
import numpy as np

DEBUG, TEST = False, False
DAY = "8"


def makeGrid(data: list) -> np.ndarray:
    """Strip, convert to ints, and return a numpy array of the input data"""
    grid = [list(int(i) for i in line.strip()) for line in data]
    return np.array(grid)


def isEdge(grid: np.ndarray, r, c) -> bool:
    """Return whether a coord is on an edge of the grid"""
    if r in (0, grid[0].size - 1) or c in (0, grid[:, 0].size - 1):
        return True
    return False


def countVisibleTrees(grid: list) -> int:
    """Counts visible trees from the perimeter of the forest, where a tree is visible
    if it is not obstructed in all directions by trees of equal or greater height"""

    def visibleHorizontal(r, c) -> bool:
        height = grid[r][c]

        # check left, then right, short circuiting if visible from the left
        visLeft = True
        for j in reversed(range(0, c)):
            if grid[r][j] >= height and j != c:
                visLeft = False
                break
        if visLeft:
            return True

        for j in range(c, len(grid[r])):
            if grid[r][j] >= height and j != c:
                return False

        return True

    def visibleVertical(r, c) -> bool:
        height = grid[r][c]

        # check up, then down, short circuiting if visible from up
        visUp = True
        for i in reversed(range(0, r)):
            if i != r and grid[i][c] >= height:
                visUp = False
                break

        if visUp:
            return True

        for i in range(r, len(grid)):
            if i != r and grid[i][c] >= height:
                return False

        return True

    count = 0
    for r, row in enumerate(grid):
        for c, _ in enumerate(row):

            visible: bool
            if isEdge(grid, r, c):
                visible = True
            else:
                horizontal = visibleHorizontal(r, c)
                if not horizontal:
                    vertical = visibleVertical(r, c)
                visible = horizontal or vertical

            if visible:
                count += 1

    return count


def findHighestScenicScore(grid: np.ndarray) -> int:
    """Find the highest scenic score for a tree, where the score is calculated
    as the product of how many trees can be seen in each direction"""

    # this scores array exists entirely for debugging, to display the whole forest with each
    # location occupied by its scenic score
    scores = np.array(
        [[0 for c in range(grid[0].size)] for i in range(grid[:, 0].size)]
    )

    highestScenicScore = 0

    def findScoreDir(vector, r, c):
        if isEdge(grid, r, c):
            return 0
        height = grid[r, c]
        score = 0
        for tree in vector:
            score += 1
            if height <= tree:
                break

        return score

    for r, row in enumerate(grid):
        for c, _ in enumerate(row):
            row = grid[r]
            col = grid[:, c]

            # left and up need to be reversed to properly stop when the first tree obstructing the
            # view is encountered
            left = row[:c][::-1]
            right = row[c + 1 :]
            up = col[:r][::-1]
            down = col[r + 1 :]

            dirScores = (
                findScoreDir(up, r, c),
                findScoreDir(down, r, c),
                findScoreDir(left, r, c),
                findScoreDir(right, r, c),
            )

            scenicScore = np.prod(dirScores)
            scores[r, c] = scenicScore

            highestScenicScore = max(scenicScore, highestScenicScore)

    print("-" * 15)
    print(scores)

    return highestScenicScore


def solve(data: list):
    """Make a numpy array out of data and pass to part one and two functions"""
    grid = makeGrid(data)
    print(grid)
    print(f"grid is {grid[0].size}x{grid[:,0].size}")
    return countVisibleTrees(grid), findHighestScenicScore(grid)


if __name__ == "__main__":
    # TEST = True
    # DEBUG = True
    datasets = [f"./day{DAY}/day{DAY}input.txt", f"./day{DAY}/testday{DAY}input.txt"]
    filename = datasets[1] if TEST else datasets[0]
    with open(file=filename, mode="r", encoding="utf8") as file:
        lines = file.readlines()
        print(solve(lines))
