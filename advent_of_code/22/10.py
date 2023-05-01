#!/usr/bin/env python

insts = open("10.in").read().splitlines()
cycles = list(range(20, 221, 40))

x = 1
pc = 0
part_one = 0
part_two = ""

for inst in insts:
  part_two += "#" if x-1 <= (pc % 40) <= x+1 else "."
  if inst == "noop":
    pc += 1
    if pc in cycles: part_one += (x * pc)
  else:
    pc += 1
    if pc in cycles: part_one += (x * pc)
    part_two += "#" if x-1 <= (pc % 40) <= x+1 else "."
    pc += 1
    if pc in cycles: part_one += (x * pc)
    x += int(inst.split()[1])

print(part_one)
for i in range(0, 201, 40):
  print("".join(part_two[i:i+40]))
