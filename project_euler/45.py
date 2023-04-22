#!/usr/bin/env python

from math import sqrt

def is_pentagonal(n):
  x = sqrt(24 * n + 1)
  return x % 6 == 5

for m in range(144, int(1e6)):
  n = 2*m*m - m
  if is_pentagonal(n):
    print(n)
    break
