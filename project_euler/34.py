#!/usr/bin/env python

from functools import cache

@cache
def factorial(n):
  if n == 0:
    return 1
  return n * factorial(n - 1)

total = 0
for n in range(3, 100000):
  if n == sum(map(factorial, map(int, str(n)))):
    total += n
print(total)
