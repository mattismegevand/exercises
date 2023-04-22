#!/usr/bin/env python

import numpy as np

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
seen = set()

grid = [[int(n) for n in line] for line in open("8.in").read().splitlines()]
grid = np.array(grid)

part_one = 0
part_two = float('-inf')

for i in range(grid.shape[0]):
  for j in range(grid.shape[1]):
    v = grid[i, j]
    score = 1
    for (di, dj) in directions:
      ii, jj = i, j
      visible = True
      s = 0

      while True:
        ii += di
        jj += dj
        if not (0 <= ii < grid.shape[0] and 0 <= jj < grid.shape[1]):
          break
        s += 1
        if grid[ii, jj] >= v:
          visible = False
          break

      score *= s
      if visible and (i, j) not in seen:
        part_one += 1
        seen.add((i, j))
    part_two = max(part_two, score)

print(part_one)
print(part_two)
