# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict

import numpy as np

array = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
vector = np.array([0, 1])
print(array[0, 1])
(a, b) = vector
print(array[vector[0], vector[1]])
print(array[a, b])

print(tuple(vector))
