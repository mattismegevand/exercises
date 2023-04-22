#!/usr/bin/env python

from functools import cache

@cache
def is_prime(n):
  if n < 2:
    return False
  if n == 2:
    return True
  if n % 2 == 0:
    return False
  for i in range(3, int(n ** 0.5) + 1, 2):
    if n % i == 0:
      return False
  return True

def quadratic_primes(a, b):
  n = 0
  while is_prime(n * n + a * n + b):
    n += 1
  return n

best = max((quadratic_primes(a, b), a * b) for a in range(-999, 1000) for b in range(-999, 1000))
print(best[1])
