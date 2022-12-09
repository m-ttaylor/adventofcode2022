"""foo"""
from collections import Counter
import numpy as np

DEBUG, TEST = False, False
DAY = "9"


def moveRope(rope, direction):

    moveHead(rope[0], direction)

    for i in range(1, len(rope)):
        moveTail(rope[i - 1], rope[i])

    # moveTail(rope[0], rope[-1])

    return tuple(rope[-1])


def moveHead(head, direction):
    """foo"""
    if direction == "R":
        head[0] += 1
    elif direction == "L":
        head[0] -= 1
    if direction == "U":
        head[1] += 1
    elif direction == "D":
        head[1] -= 1


def moveTail(head, tail):
    xgap, ygap = head[0] - tail[0], head[1] - tail[1]

    if head[0] != tail[0] and head[1] != tail[1] and (abs(xgap) > 1 or abs(ygap) > 1):
        tail[0] += np.sign(xgap)
        tail[1] += np.sign(ygap)
    elif abs(xgap) > 1:
        tail[0] += np.sign(xgap)
    elif abs(ygap) > 1:
        tail[1] += np.sign(ygap)
    # return(str(tail[0])+str(tail[1]))


def solve(data: list, rope):
    """foo"""

    # # uncomment for test set visualization
    # board = np.array([["."] * 5] * 6)
    # board[0, 0] = "H"

    # head = [0, 0]
    # tail = [0, 0]

    # rope = [head, tail]

    visited = set()

    visited.add((0, 0))

    # # uncomment for test set visualization
    # def clearBoard():
    #     board[rope[0][0], rope[0][1]] = "."
    #     board[rope[1][0], rope[1][1]] = "."

    for command in data:
        direction, spaces = command.strip().split()
        # # uncomment for test set visualization
        # print(f"== {command.strip()} ==")
        for m in range(int(spaces)):
            # # uncomment for test set visualization
            # clearBoard()
            visited.add(moveRope(rope, direction))

            # # uncomment for test set visualization
            # board[rope[0][0], rope[0][1]] = "H"
            # board[rope[1][0], rope[1][1]] = "T"
            # print(" ------------------------")
            # print(np.flip(board.T, 0))

    return len(visited)


if __name__ == "__main__":
    # TEST = True
    # DEBUG = True
    datasets = [f"./day{DAY}/day{DAY}input.txt", f"./day{DAY}/testday{DAY}input.txt"]
    filename = datasets[1] if TEST else datasets[0]
    with open(file=filename, mode="r", encoding="utf8") as file:
        lines = file.readlines()
        print(solve(lines, [[0, 0], [0, 0]]))
        print(solve(lines, [[0, 0] for _ in range(10)]))

# 5907 is too low
