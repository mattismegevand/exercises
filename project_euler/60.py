#!/usr/bin/env python

import math
import random

def is_prime(n, k=3):
  if n < 2:
    return False
  if n != 2 and n % 2 == 0:
    return False
  s, d = 0, n - 1
  while d % 2 == 0:
    s, d = s + 1, d // 2
  for _ in range(k):
    x = random.randint(2, n - 1)
    if pow(x, d, n) != 1:
      for r in range(s):
        if pow(x, 2**r * d, n) == n - 1:
          break
      else:
        return False
  return True

def sieve(n):
  primes = [True] * n
  primes[0], primes[1] = False, False
  for i in range(2, int(math.sqrt(n)) + 1):
    if primes[i]:
      for j in range(i**2, n, i):
        primes[j] = False
  return [i for i, x in enumerate(primes) if x]

def comb(a, b):
  ab = int(f"{a}{b}")
  ba = int(f"{b}{a}")
  return is_prime(ab) and is_prime(ba)

def prime_combinations(primes, depth, current_primes=[]):
  if depth == 0:
    return sum(current_primes)
  for i, p in enumerate(primes):
    if not current_primes or p >= current_primes[-1]:
      if all(comb(p, x) for x in current_primes):
        result = prime_combinations(primes[i:], depth-1, current_primes + [p])
        if result:
          return result

def prime_pairs(primes):
  return prime_combinations(primes, 5)

primes = sieve(10000)
print(prime_combinations(primes, 5))
