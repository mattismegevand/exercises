#!/usr/bin/env python

import sys
from math import sqrt

def is_prime(n):
  if n < 2:
    return False
  elif n == 2:
    return True
  elif not n & 1:
    return False
  else:
    for i in range(3, int(sqrt(n)) + 1, 2):
      if not n % i:
        return False
    return True

def is_permutation(a, b):
  return sorted(str(a)) == sorted(str(b))

primes = [i for i in range(1000, 10000) if is_prime(i)]
count = 0
for i, p1 in enumerate(primes):
  for j, p2 in enumerate(primes[i+1:]):
    p3 = p2 + (p2 - p1)
    if p3 in primes and is_permutation(p1, p2) and is_permutation(p2, p3):
      print(p1, p2, p3, sep='')
      count += 1
      if count == 2: sys.exit(0)
