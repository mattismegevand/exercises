#!/usr/bin/env python

def is_prime(n):
  if n < 2:
    return False
  if n == 2 or n == 3:
    return True
  if not n % 2 or not n % 3:
    return False
  for i in range(5, int(n ** 0.5) + 1, 6):
    if not n % i or not n % (i + 2):
      return False
  return True

for i in range(9999999, 1, -2):
  if is_prime(i):
    l = [int(c) for c in str(i)]
    m = max(l)
    if len(l) == len(set(l)) and set(l) == set(range(1, m + 1)):
      print(i)
      break
