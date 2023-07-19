#!/usr/bin/env python

from math import sqrt

def is_prime(n):
  if n < 2:
    return False
  if n == 2:
    return True
  if n % 2 == 0:
    return False
  for i in range(3, int(sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True

n = 1
for p in [p for p in range(2, 1000) if is_prime(p)]:
  if n * p > int(1e6):
    break
  n *= p
print(n)
