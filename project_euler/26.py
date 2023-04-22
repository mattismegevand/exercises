#!/usr/bin/env python

def recurring_cycle(n):
  r = 1
  for i in range(1, n):
    r = (r * 10) % n
    if r == 1:
      return i
  return 0

print(max(range(1, 1000), key=recurring_cycle))
