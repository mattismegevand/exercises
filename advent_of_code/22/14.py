#!/usr/bin/env python

rocks = set()
for l in open("14.in").read().splitlines():
  prev = None
  for p in l.split(' -> '):
    x, y = (int(n) for n in p.split(','))
    if prev is not None:
      dx = x - prev[0]
      dy = y - prev[1]
      length = max(abs(dx), abs(dy))
      dir = (dx // length, dy // length)
      for n in range(length+1):
        xx = prev[0] + n * dir[0]
        yy = prev[1] + n * dir[1]
        rocks.add((xx, yy))
    prev = (x, y)

floor = 2 + max(y for _, y in rocks)
part_one = None
for part in [1, 2]:
  if part == 2:
    min_x = min(x for x, _ in rocks) - 1000
    max_x = max(x for x, _ in rocks) + 1000
    for x in range(min_x, max_x):
      rocks.add((x, floor))

  for i in range(int(1e9)):
    x, y = (500, 0)
    if (x, y) in rocks:
      part_two = part_one + i
      break
    while True:
      if y > floor and part == 1:
        part_one = i
        break
      if (x, y+1) not in rocks:
        y += 1
      elif (x-1, y+1) not in rocks:
        x -= 1
        y += 1
      elif (x+1, y+1) not in rocks:
        x += 1
        y += 1
      else:
        break
    if part == 1 and part_one is not None:
      break
    rocks.add((x, y))

print(part_one)
print(part_two)
