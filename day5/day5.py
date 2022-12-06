"""
--- Day 5 ---
TODO: Go back and adding the problem text now
"""
from collections import defaultdict

DEBUG, TEST = False, False
DAY = "5"


class CrateStack:
    """A stack of crates. Crates should contain strings of format '[A]'"""

    crates: list[str] = []

    def __init__(self, data: list[str] = None):
        if data:
            self.crates = data
        else:
            self.crates = []

    def takeCrate(self) -> str:
        """Take and return top crate from stack"""
        return self.crates.pop()

    def takeCrates(self, amount: int) -> "CrateStack":
        """Take and return a CrateStack of top n crates from stack"""
        length = len(self.crates)
        takenCrates = self.crates[length - amount : length]
        self.crates = self.crates[: length - amount]
        return CrateStack(takenCrates)

    def addCrate(self, crate):
        """Add crate to top of stack"""
        self.crates.append(crate)

    def addCrates(self, crates: "CrateStack"):
        """Add a CrateStack to stack, preserving order"""
        self.crates += crates.crates

    def __repr__(self) -> str:
        return f"[{', '.join(self.crates)}]\n"

    def __eq__(self, other) -> bool:
        return self.crates == other.crates


def readTops(stacks: list[CrateStack]) -> str:
    """Return the top crates from a list of crates in strin format, e.g. 'abcd'"""
    tops = ""
    for stack in stacks:
        if stack.crates != []:
            tops += stack.takeCrate().strip("[").strip("]")

    return tops


def parseCommand(stacks: list[CrateStack], command: str, version=""):
    """Parses a list of commands of format: 'move x from i to j'"""
    words = command.split()
    moves = int(words[1])
    source = int(words[3]) - 1
    dest = int(words[5]) - 1

    if version == "9001":
        crates = CrateStack()
        crates = stacks[source].takeCrates(moves)
        stacks[dest].addCrates(crates)

    else:
        for _ in range(moves):
            crate = stacks[source].takeCrate()
            if crate != None:
                stacks[dest].addCrate(crate)


def parseStacks(data: list[str]) -> list[CrateStack]:
    """Parses a list of stacks of format:
        [f]
        [a]    [b]
    [c] [d]    [e] [g]
     1   2   3  4   5

    and returns them as a list of CrateStack objects.
    """

    crateStacks = defaultdict(list)
    crateStacksIndexed: list[CrateStack] = []

    for line in data:
        spaceCount, index = 0, 0

        for c in line.split(" "):

            if spaceCount == 4:
                index += 1
                spaceCount = 0

            if c == "":
                spaceCount += 1

            elif c.startswith("["):
                stack = crateStacks[str(index)]
                stack.insert(len(stack), c.strip())
                index += 1

    for i in range(len(crateStacks)):
        stack = CrateStack(list(reversed(crateStacks[str(i)])))
        crateStacksIndexed.append(stack)

    return crateStacksIndexed


def splitData(data: list[str]) -> tuple[list[str]]:
    """Splits input data into crate stacks and commands and returns a tuple of split data"""

    splitIndex = data.index("\n")
    stacks, commands = data[: splitIndex - 1], data[splitIndex + 1 :]

    return (stacks, commands)


def solve(data: list[str], version="") -> int:
    """Runs the exercise"""
    stacks, commands = splitData(data)
    crateStacksIndexed = parseStacks(stacks)

    for command in commands:
        parseCommand(crateStacksIndexed, command, version)

    return readTops(crateStacksIndexed)


if __name__ == "__main__":
    # TEST = True
    datasets = [
        f"./day{DAY}/day{DAY}input.txt",
        f"./day{DAY}/testday{DAY}input.txt",
        f"./day{DAY}/testday{DAY}input2.txt",
    ]

    filename = datasets[1] if TEST else datasets[0]

    with open(file=filename, mode="r", encoding="utf8") as file:
        lines = file.readlines()
        print(solve(lines, "9001"))
