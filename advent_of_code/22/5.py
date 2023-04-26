#!/usr/bin/env python

inst1, inst2 = open("5.in").read().split("\n\n")

for i, line in enumerate(inst1.splitlines()):
  if i == 0:
    n = (len(line)+1) // 4
    crates = [[] for _ in range(n)]
  for j, l in enumerate(line[1::4]):
    if l.isnumeric():
      break
    if l != " ":
      crates[j].append(l)

start = crates.copy()
for is_part_one in [True, False]:
  crates = start.copy()
  for line in inst2.splitlines():
    n, s, d = [int(x) for x in line.split()[1::2]]
    s, d = s-1, d-1

    moving = crates[s][:n]
    if is_part_one:
      moving = moving[::-1]

    crates[d] = moving + crates[d]
    crates[s] = crates[s][n:]
  print("".join(c[0] for c in crates))
