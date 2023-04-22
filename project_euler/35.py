#!/usr/bin/env python

from functools import cache
from math import sqrt

@cache
def is_prime(n):
  if n < 2:
    return False
  if n == 2:
    return True
  if n % 2 == 0:
    return False
  for i in range(3, int(sqrt(n)) + 1, 2):
    if n % i == 0:
      return False
  return True

seen = {}
for i in range(1, 1000000):
  if is_prime(i):
    s = str(i)
    rotations = (int(s[j:] + s[:j]) for j in range(len(s)))
    if rotations not in seen:
      seen[rotations] = all(is_prime(r) for r in rotations)
print(sum(1 for v in seen.values() if v))
