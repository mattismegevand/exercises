#!/usr/bin/env python

from math import sqrt

def prime_factors(n):
  factors = []
  while n % 2 == 0:
    factors.append(2)
    n //= 2
  for i in range(3, int(sqrt(n)) + 1, 2):
    while n % i == 0:
      factors.append(i)
      n //= i
  if n > 2:
    factors.append(n)
  return factors

for i in range(2, int(1e6)):
  l = (len(set(prime_factors(i+j))) for j in range(4))
  if all([x == 4 for x in l]):
    print(i)
    break
