"""bar"""
from collections import deque


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


def shortestPath(start, target):
    queue: deque[list] = deque()
    visited = set()

    queue.append([start])

    if start == target:
        return 0

    while len(queue) > 0:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            visited.add(node)
            for nbor in valves2[node]:
                if nbor == target:
                    return len(path)

                queue.append([*path, nbor])


def executeDFS():
    def dfs(node, visited):

        if node not in visited:
            visited.add(node)

        for n in nodes:
            if n not in visited:
                dfs(n, visited)

    visited = set()

    for node in nodes:
        if node not in visited:
            visited.add(node)
            dfs(node, visited)
