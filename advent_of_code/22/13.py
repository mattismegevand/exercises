#!/usr/bin/env python

from functools import cmp_to_key
from itertools import zip_longest

pairs = [l.splitlines() for l in open("13.in").read().split("\n\n")]

def compare(a, b):
  if a is None: return -1
  if b is None: return 1

  if type(a) == type(b) == int:
    if a < b:
      return -1
    elif a == b:
      return 0
    else:
      return 1
  elif type(a) == type(b) == list:
    for aa, bb in zip_longest(a, b):
      c = compare(aa, bb)
      if c != 0:
        return c
    return 0
  elif type(a) == list:
    return compare(a, [b])
  else:
    return compare([a], b)

packets = [[[2]], [[6]]]
part_one = 0
for i, pair in enumerate(pairs):
  a, b = eval(pair[0]), eval(pair[1])
  packets.append(a)
  packets.append(b)
  if compare(a, b) == -1:
    part_one += i+1

packets = sorted(packets, key=cmp_to_key(compare))
part_two = (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)

print(part_one)
print(part_two)
