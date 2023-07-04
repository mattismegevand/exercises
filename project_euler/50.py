#!/usr/bin/env python

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

primes = [i for i in range(1, 1000000) if is_prime(i)]
max_len, max_sum = 0, 0
for i in range(len(primes)):
  for j in range(i + max_len, len(primes)):
    s = sum(primes[i:j])
    if s > 1000000: break
    if s in primes:
      max_len, max_sum = j - i, s
print(max_sum)
