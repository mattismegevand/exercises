#!/usr/bin/env python

from collections import defaultdict

lines = open("7.in").read().splitlines()
fs = defaultdict(int)
current_path = []

for line in lines:
  words = line.split()
  if words[1] == "cd":
    if words[2] == "..":
      current_path.pop()
    else:
      current_path.append(words[2])
  elif words[1] == "ls":
    continue
  elif words[0] == "dir":
    continue
  else:
    size = int(words[0])
    for i in range(1, len(current_path) + 1):
      fs["/".join(current_path[:i])] += size

need = fs["/"] - (70000000 - 30000000)

part_one = 0
part_two = float('inf')

for k, v in fs.items():
  if v <= 100000:
    part_one += v
  if v >= need:
    part_two = min(part_two, v)

print(part_one)
print(part_two)
