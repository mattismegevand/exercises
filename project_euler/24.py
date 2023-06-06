#!/usr/bin/env python

def fibbonaci_sequence():
  a, b = 1, 1
  while True:
    yield a
    a, b = b, a + b

for i, n in enumerate(fibbonaci_sequence()):
  if len(str(n)) >= 1000:
    print(i + 1)
    break
