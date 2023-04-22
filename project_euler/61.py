#!/usr/bin/env python

import sys

F = {
  3: lambda n: n * (n + 1) // 2,
  4: lambda n: n * n,
  5: lambda n: n * (3*n - 1) // 2,
  6: lambda n: n * (2*n - 1),
  7: lambda n: n * (5*n - 3) // 2,
  8: lambda n: n * (3*n - 2)
}

def generate_numbers(s):
  n = 1
  while True:
    f = F[s](n)
    if f > 9999:
      break
    if f > 999 and f % 100 > 9:
      yield f
    n += 1

def search(chain, remaining):
  if not remaining:
    return chain if chain[-1] % 100 == chain[0] // 100 else None
  prefix = chain[-1] % 100
  for s in list(remaining):
    for num in numbers[s]:
      if num // 100 == prefix:
        res = search(chain + [num], remaining - {s})
        if res:
          return res

numbers = {s: list(generate_numbers(s)) for s in range(3, 9)}

for start_type in range(3, 9):
  for start_num in numbers[start_type]:
    chain = search([start_num], set(range(3, 9)) - {start_type})
    if chain:
      print(sum(chain))
      sys.exit(0)