#!/usr/bin/env python

from functools import cache

@cache
def collatz_length(n):
  if n == 1:
    return 1
  if n % 2 == 0:
    return collatz_length(n // 2) + 1
  return collatz_length(3 * n + 1) + 1

print(max(range(1, 1000000), key=collatz_length))
