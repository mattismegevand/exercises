#!/usr/bin/env python

from functools import cache

@cache
def is_prime(n):
  if n == 2:
    return True
  if n < 2 or n % 2 == 0:
    return False
  for i in range(3, int(n ** 0.5) + 1, 2):
    if n % i == 0:
      return False
  return True

def is_truncable_prime(n):
  if not is_prime(n):
    return False
  n = str(n)
  for i in range(1, len(n)):
    if not is_prime(int(n[i:])):
      return False
    if not is_prime(int(n[:-i])):
      return False
  return True

truncable_primes = []
for i in range(11, int(1e9), 2):
  if len(truncable_primes) == 11: break
  if is_truncable_prime(i):
    truncable_primes.append(i)
print(sum(truncable_primes))
