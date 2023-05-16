#!/usr/bin/env python

from math import sqrt, log, floor

P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
check = True
k = 20
N = 1
for p in P:
    if p > k: break
    a = 1
    if check:
        if p <= sqrt(k):
            a = floor(log(k) // log(p))
        else:
            check = False
    N *= p ** a
print(N)
