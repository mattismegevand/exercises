#!/usr/bin/env python

from functools import cache

@cache
def divisors(n):
  return [i for i in range(1, n) if n % i == 0]

n = 0
for i in range(1, 10000):
  a = sum(divisors(i))
  b = sum(divisors(a))
  if i == b and a != b:
    n += i
print(n)
