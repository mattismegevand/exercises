#!/usr/bin/env python

def is_palindrome(n):
  return str(n) == str(n)[::-1]

def is_lychrel(n):
  for _ in range(50):
    n += int(str(n)[::-1])
    if is_palindrome(n):
      return False
  return True

print(sum(1 for n in range(1, 10000) if is_lychrel(n)))
