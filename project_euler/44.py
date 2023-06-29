#!/usr/bin/env python

from math import sqrt

def is_pentagonal(n):
  x = sqrt(24 * n + 1)
  return x % 6 == 5

pentagonals = set()
for i in range(1, 25000000):
  if is_pentagonal(i):
    pentagonals.add(i)

d = float('inf')
for a in pentagonals:
  for b in pentagonals:
    if a - b in pentagonals and a + b in pentagonals:
      d = min(d, abs(a - b))
print(d)
