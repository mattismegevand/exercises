#!/usr/bin/env python

def palindrome(n):
  return str(n) == str(n)[::-1]

def int_to_binary(n):
  return bin(n)[2:]

total = 0
for i in range(1000000):
  if palindrome(i) and palindrome(int_to_binary(i)):
    total += i
print(total)
