"""File directory exploration"""

DEBUG, TEST = False, False
DAY = "7"


class Directory:
    """Represents a directory and its size, parent directory (if applicable) and name"""

    size: int
    parent: "Directory"
    name: str

    def __init__(self, name: str, parent: "Directory" = None, size=0):
        self.name = name
        self.parent = parent
        self.size = size
        if size and parent:
            parent.updateSize(size)

    def setSize(self, size: int):
        """recursively set size of self and parent(s)"""
        self.size = size
        if self.parent:
            self.parent.updateSize(size)

    def updateSize(self, size: int):
        """recursively update size of self and parent(s)"""
        self.size += size
        if self.parent:
            self.parent.updateSize(size)

    def setParent(self, parent: "Directory"):
        """set parent Directory"""
        self.parent = parent

    def __repr__(self):
        return str(
            {
                "name": self.name,
                "size": self.size,
                "parent": self.parent.name if self.parent else None,
            }
        )


def solve(data: list) -> int:
    """Build directory objects, recursively updating their sizes along the way, then use these to
    solve parts one and two."""

    UPDATE_SIZE = 30000000
    HARD_DRIVE_SIZE = 70000000

    dirs = []
    lastCommandWasLs = False
    previousDir = None
    currentDir = None

    for line in data:
        if lastCommandWasLs and not line.startswith("$") and not line.startswith("dir"):
            filesize = line.split(" ")[0]

            currentDir.updateSize(int(filesize))

        elif line.startswith("$ cd"):
            previousDir = currentDir
            dest = line.split(" ")[2].strip()
            if dest not in ["..", "\n"]:
                currentDir = Directory(name=dest, parent=previousDir)
                if DEBUG:
                    print(f"navigated to directory {currentDir.name}")
            elif dest == "..":
                if DEBUG:
                    print(f"moving up one directory to {currentDir.parent.name}")
                currentDir = currentDir.parent

            if currentDir not in dirs:
                dirs.append(currentDir)

            lastCommandWasLs = False
        elif line.startswith("$ ls"):
            lastCommandWasLs = True

    if DEBUG:
        print(dirs)

    sizesUnder10k = sum(item.size for item in dirs if item.size < 100000)

    spaceNeeded = UPDATE_SIZE - (HARD_DRIVE_SIZE - dirs[0].size)
    if DEBUG:
        print("total space needed is", spaceNeeded)

    smallest = min(d.size for d in dirs if d.size > spaceNeeded)

    return sizesUnder10k, smallest


if __name__ == "__main__":
    # TEST = True
    # DEBUG = True
    datasets = [f"./day{DAY}/day{DAY}input.txt", f"./day{DAY}/testday{DAY}input.txt"]
    filename = datasets[1] if TEST else datasets[0]
    with open(file=filename, mode="r", encoding="utf8") as file:
        lines = file.readlines()
        sizes, smallestFileToDelete = solve(lines)
        print(sizes)
        print(smallestFileToDelete)

# 1007861 is too low
# 1423358 is just right
