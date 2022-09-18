#!/usr/bin/env python3

import numpy as np

if __name__ == "__main__":
  nums = list(map(int, open("input_01").readlines()))
  windows = np.convolve(nums, np.ones(3), 'valid')

  print(np.sum(np.diff(nums) > 0))
  print(np.sum(np.diff(windows) > 0))
