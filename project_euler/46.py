#!/usr/bin/env python

from math import sqrt
from functools import cache

@cache
def is_prime(n):
  if n < 2:
    return False
  if n == 2:
    return True
  if n % 2 == 0:
    return False
  for i in range(3, int(n**0.5) + 1, 2):
    if n % i == 0:
      return False
  return True

def is_goldbach(n):
  for i in range(1, int(sqrt(n/2)) + 1):
    if is_prime(n - 2*i*i):
      return True

for i in range(33, int(1e6), 2):
  if not is_prime(i) and not is_goldbach(i):
    print(i)
    break
