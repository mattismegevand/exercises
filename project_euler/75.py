#!/usr/bin/env python

from math import sqrt

N = 1500000

def gcd(a, b):
  while b:
    a, b = b, a % b
  return a

perimeters = [0] * (N + 1)
for m in range(2, int(sqrt(N // 2)) + 1):
  for n in range(1, m):
    if (m - n) % 2 == 1 and gcd(m, n) == 1:
      a = m * m - n * n
      b = 2 * m * n
      c = m * m + n * n

      p = a + b + c
      while p <= N:
        perimeters[p] += 1
        p += a + b + c
print(perimeters.count(1))
