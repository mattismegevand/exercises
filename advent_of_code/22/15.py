#!/usr/bin/env python

sensors = set()
beacons = set()
for l in open("15.in").read().splitlines():
  l = l.split()
  sx, sy = (int(s[2:-1]) for s in l[2:4])
  bx, by = l[8:10]
  bx, by = int(bx[2:-1]), int(by[2:])
  distance = abs(sx - bx) + abs(sy - by)
  sensors.add((sx, sy, distance))
  beacons.add((bx, by))

def visible(x, y, sensors):
  for sx, sy, ds in sensors:
    distance = abs(sx - x) + abs(sy - y)
    if distance <= ds:
      return True
  return False

y = 2000000
part_one = 0
for x in range(-int(1e7), int(1e7)):
  if (x, y) in beacons: continue
  if visible(x, y, sensors):
    part_one += 1

part_two = None
for sx, sy, ds in sensors:
  for dx in range(ds+2):
    dy = (ds+1) - dx
    for dirx, diry in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
      x, y = sx + dirx * dx, sy + diry * dy
      if not (0 <= x <= 4000000 and 0 <= y <= 4000000): continue
      if not visible(x, y, sensors):
        part_two = x * 4000000 + y
        break
    if part_two is not None: break
  if part_two is not None: break

print(part_one)
print(part_two)
