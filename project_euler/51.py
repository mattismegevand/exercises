#!/usr/bin/env python

from math import floor, sqrt
from functools import cache

@cache
def is_prime(n):
  if n == 1:
    return False
  elif n < 4:
    return True
  elif n % 2 == 0:
    return False
  elif n < 9:
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

def generate_primes(n):
  return (i for i in range(2, n + 1) if is_prime(i))

def replace(string, newchar, indexlist):
  s = list(string)
  for index in indexlist:
    s[index] = newchar
  return ''.join(s)

def solve(n):
  for num_digits in range(2, 7):
    primes = [i for i in generate_primes(10**num_digits) if i > 10**(num_digits-1)]
    for prime in primes:
      prime_str = str(prime)
      for digit in '0123456789':
        if prime_str.count(digit) >= 1:
          indices = [i for i, x in enumerate(prime_str) if x == digit]
          family = [replace(prime_str, str(i), indices) for i in range(10)]
          family = [int(member) for member in family if len(str(int(member))) == num_digits and is_prime(int(member))]
          if len(family) == n:
            return min(family)
  return None

print(solve(8))
