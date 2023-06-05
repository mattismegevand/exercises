#!/usr/bin/env python

from functools import cache

@cache
def is_abundant(n):
  return sum(i for i in range(1, n//2+1) if n % i == 0) > n

abundants = [i for i in range(1, 28124) if is_abundant(i)]
sum_abundants = set()
for a in abundants:
  for b in abundants:
    if a + b > 28123:
      break
    sum_abundants.add(a + b)

print(sum(i for i in range(1, 28124) if i not in sum_abundants))
