#!/usr/bin/env python3

import numpy as np

def fuel1(source, dest):
  return np.sum(np.abs(source - dest))

def fuel2(source, dest):
  d = np.abs(source - dest)
  return np.sum(d * (d + 1) // 2)


if __name__ == "__main__":
  l = np.array([int(n) for n in open("input_07").read().strip().split(",")])
  print(min([fuel1(l, d) for d in range(min(l), max(l) + 1)]))
  print(min([fuel2(l, d) for d in range(min(l), max(l) + 1)]))
