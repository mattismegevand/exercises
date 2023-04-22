#!/usr/bin/env python

from functools import cache

@cache
def coin_sums(coins, n):
  if n == 0:
    return 1
  if n < 0:
    return 0
  if not coins:
    return 0
  return coin_sums(coins, n - coins[0]) + coin_sums(coins[1:], n)

print(coin_sums((1, 2, 5, 10, 20, 50, 100, 200), 200))
