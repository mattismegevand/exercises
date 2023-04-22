#!/usr/bin/env python

from collections import deque

grid = [list(l) for l in open("12.in").read().splitlines()]
H = len(grid)
W = len(grid[0])
for i in range(H):
  for j in range(W):
    l = grid[i][j]
    if l in ['S', 'E']:
      grid[i][j] = 0 if l == 'S' else 26
    else:
      grid[i][j] = ord(l) - ord('a') + 1

def bfs(part):
  q = deque()
  for i in range(H):
    for j in range(W):
      if (part == 1 and grid[i][j] == 0) or (part == 2 and grid[i][j] == 1):
        q.append(((i, j), 0))

  s = set()
  while q:
    (i, j), d = q.popleft()
    if (i, j) in s:
      continue
    s.add((i, j))
    if grid[i][j] == 26:
      return d
    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
      ii = i + di
      jj = j + dj
      if ii < 0 or ii >= H or jj < 0 or jj >= W:
        continue
      if grid[ii][jj] <= grid[i][j] + 1:
        q.append(((ii, jj), d + 1))

print(bfs(1))
print(bfs(2))
