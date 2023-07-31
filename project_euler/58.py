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

def find_spiral_side_length():
  primes = 0
  corners = 1
  side_length = 0
  for i in range(3, 100000, 2):
    side_length = i
    corners += 4

    for j in range(4):
      if is_prime(i**2 - j*(i - 1)):
        primes += 1

    if primes / corners < 0.1:
      return side_length

print(find_spiral_side_length())
