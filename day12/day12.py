"""day12"""

from collections import deque
import numpy as np

DEBUG, TEST = False, False
DAY = "12"


class Graph:
    def __init__(self, graph: np.ndarray):
        self.graph = graph
        self.rows = graph[:, 0].size
        self.cols = graph[0].size
        self.edges = np.array([[0 for c in range(self.cols)] for r in range(self.rows)])

    def addEdge(self, r: int, c: int, height: int):
        self.edges[r, c] = height

    def bfs(self, start: str, target: str):
        queue: deque[tuple[tuple[int, int], int]] = deque()
        visited = set()
        # using array of vectors instead of tuples for that sweet sweet vector addition
        dirs = [
            np.array([0, 1]),
            np.array([0, -1]),
            np.array([1, 0]),
            np.array([-1, 0]),
        ]

        for r, row in enumerate(self.graph):
            for c, col in enumerate(row):
                if col == start:
                    queue.appendleft(((r, c), 0))

        while queue:
            node, height = queue.pop()

            if self.graph[node] == target:
                return height

            if node not in visited:
                visited.add(node)

                for d in dirs:
                    neighbor = node + d
                    if 0 <= neighbor[0] < self.rows and 0 <= neighbor[1] < self.cols:
                        if self.edges[tuple(neighbor)] <= 1 + self.edges[node]:
                            queue.appendleft((tuple(neighbor), height + 1))


def solve(graph, start):
    heightMap = {letter: i for i, letter in enumerate("abcdefghijklmnopqrstuvwxyz")}
    heightMap["S"] = 0
    heightMap["E"] = 25

    g = Graph(np.array(graph))

    for r, row in enumerate(graph):
        for c, col in enumerate(row):
            g.addEdge(r, c, heightMap[col])

    print(g.bfs(start, "E"))


if __name__ == "__main__":
    # TEST = True
    # DEBUG = True
    datasets = [f"./day{DAY}/day{DAY}input.txt", f"./day{DAY}/testday{DAY}input.txt"]
    filename = datasets[1] if TEST else datasets[0]
    with open(file=filename, mode="r", encoding="utf8") as file:
        lines = [list(line.strip()) for line in file.readlines()]
        solve(lines, "S")
        solve(lines, "a")
