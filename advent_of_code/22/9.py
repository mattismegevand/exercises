#!/usr/bin/env python

dirs = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}

def update(h, t):
  dx = h[0] - t[0]
  dy = h[1] - t[1]
  if abs(dx) <= 1 and abs(dy) <= 1:
    pass
  elif abs(dx) >= 2 and abs(dy) >= 2:
    t = (h[0]-1 if t[0]<h[0] else h[0]+1, h[1]-1 if t[1]<h[1] else h[1]+1)
  elif abs(dx) >= 2:
    t = (h[0]-1 if t[0]<h[0] else h[0]+1, h[1])
  elif abs(dy) >= 2:
    t = (h[0], h[1]-1 if t[1]<h[1] else h[1]+1)
  return t

h = (0, 0)
t = [(0,0) for _ in range(9)]
part_one = set([t[0]])
part_two = set([t[8]])

for line in open("9.in").read().splitlines():
  inst, n = line.split()
  d = dirs[inst]
  n = int(n)
  for _ in range(n):
    h = (h[0] + d[0], h[1] + d[1])
    t[0] = update(h, t[0])
    for i in range(1, 9):
      t[i] = update(t[i-1], t[i])
    part_one.add(t[0])
    part_two.add(t[8])

print(len(part_one))
print(len(part_two))
