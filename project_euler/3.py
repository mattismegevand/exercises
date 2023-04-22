#!/usr/bin/env python

from math import sqrt

n = 600851475143

if n % 2 == 0:
  lf = 2
  while n % 2 == 0:
    n = n // 2
else:
  lf = 1
f = 3

maxf = sqrt(n)
while n > 1 and f <= maxf:
  if n % f == 0:
    lf = f
    while n % f == 0:
      n = n // f
    maxf = sqrt(n)
  f = f + 2

if n == 1:
  print(lf)
else:
  print(n)
