#!/usr/bin/env python

from math import sqrt
from itertools import accumulate, count

def count_factors(n):
  s = 2 * sum(n % i == 0 for i in range(1, int(sqrt(n)) + 1))
  if int(sqrt(n)) ** 2 == n:
    s -= 1
  return s

def triangle_numbers():
  yield from accumulate(count())

for t in triangle_numbers():
  if count_factors(t) > 500:
    print(t)
    break
