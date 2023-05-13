#!/usr/bin/env python

a, b = 1, 2
answer = 0
while b < 4000000:
  if b % 2 == 0:
    answer += b
  a, b = b, a+b
print(answer)
