#!/usr/bin/env python

from math import sqrt, floor

def is_prime(n):
  if n == 1:
    return False
  elif n < 4: # 2, 3
    return True
  elif n % 2 == 0:
    return False
  elif n < 9: # 5, 7
    return True
  elif n % 3 == 0:
    return False
  f = 5
  while f <= floor(sqrt(n)):
    if n % f == 0:
      return False
    if n % (f + 2) == 0:
      return False
    f += 6
  return True

limit = 10001
count = 1
n = 1
while count < limit:
  n += 2
  if is_prime(n):
    count += 1
print(n)
