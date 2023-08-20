#!/usr/bin/env python

from math import sqrt

sqrt_two = sqrt(2)
minus_term, plus_term = 3 - 2 * sqrt_two, 3 + 2 * sqrt_two
for i in range(1, int(1e6)):
  blue_disks = round(((((-2 - sqrt_two) * minus_term**i) - (2 - sqrt_two) * plus_term**i + 4) / -8)) + 1
  total_disks = 0.5 * (sqrt(8 * blue_disks**2 - 8 * blue_disks + 1) + 1)

  if total_disks > int(1e12):
    print(blue_disks)
    break
