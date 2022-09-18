#!/usr/bin/env python3

from collections import defaultdict, Counter

def step(fishes):
  next_day = defaultdict(int)
  for age, count in fishes.items():
    if age == 0:
      next_day[6] += count
      next_day[8] = count
    else:
      next_day[age - 1] += count
  return next_day


if __name__ == "__main__":
  l = [int(n) for n in open("input_06").read().strip().split(",")]
  fishes = defaultdict(int, Counter(l))

  for _ in range(80):
    fishes = step(fishes)
  print(sum(fishes.values()))

  for _ in range(256 - 80):
    fishes = step(fishes)
  print(sum(fishes.values()))
