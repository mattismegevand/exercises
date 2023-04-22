#!/usr/bin/env python

from math import prod

s = "".join(str(i) for i in range(1, 1000000))
print(prod(int(s[10 ** i - 1]) for i in range(7)))
