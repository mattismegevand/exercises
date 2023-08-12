#!/usr/bin/env python

def pentagonal_nums():
  k = 1
  while True:
    yield k * (3*k - 1) // 2
    yield k * (3*k + 1) // 2
    k += 1

partitions = [1]
for n in range(1, 100000): # arbitrary upper bound
    k, pentagonals = 1, pentagonal_nums()
    partition_n = 0
    pentagonal = next(pentagonals)

    while pentagonal <= n:
      if (k-1) % 4 < 2:
        partition_n += partitions[n - pentagonal]
      else:
        partition_n -= partitions[n - pentagonal]
      pentagonal = next(pentagonals)
      k += 1

    mod = partition_n % 1000000
    if mod == 0:
      print(n)
      break
    else:
      partitions.append(mod)
