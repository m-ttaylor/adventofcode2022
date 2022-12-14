from ast import literal_eval
from functools import cmp_to_key
from math import prod

DEBUG = False
TEST = False


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


lines = None
if TEST:
    with open(file="day13/test13input.txt", mode="r", encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]
else:
    with open(file="day13/13input.txt", mode="r", encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]

packets = [
    [literal_eval(lines[i - 1]), literal_eval(lines[i])]
    for i in range(1, len(lines), 3)
    if lines[i - 1] != "" and lines[i] != ""
]

part2packets = [literal_eval(line) for line in lines if line != ""]
part2packets.append([[2]])
part2packets.append([[6]])


def compare(l, r):
    match l, r:
        case int(), int():
            return (l > r) - (l < r)
        case int(), list():
            return compare([l], r)
        case list(), int():
            return compare(l, [r])
        case list(), list():
            for z in map(compare, l, r):
                if z:
                    return z
            return compare(len(l), len(r))


def compareAtoB(left, right):
    match (left, right):
        case None, _:
            return -1
        case _, None:
            return 1
        case int(), list():
            return compareAtoB([left], right)
        case list(), int():
            return compareAtoB(left, [right])
        case list(), list():
            for result in map(compareAtoB, left, right):
                if result:
                    return result
            return compareAtoB(len(left), len(right))
        case int(), int():
            if left == right:
                return 0
            if left > right:
                return 1
            if left < right:
                return -1


def checkOrder(packets):
    return sum(i + 1 for i, p in enumerate(packets) if compareAtoB(*p) == -1)


def order(packets):
    indices = []
    for i, p in enumerate(sorted(packets, key=cmp_to_key(compareAtoB)), 1):
        if p in [[[2]], [[6]]]:
            print(i)
            indices.append(i)

    return prod(indices)


print("part1:", checkOrder(packets))
print("part2:", order(part2packets))
