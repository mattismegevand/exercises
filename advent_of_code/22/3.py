#!/usr/bin/env python

def score(l):
  if l.islower():
    return ord(l) - ord('a') + 1
  return ord(l) - ord('A') + 27

lines = open("3.in").read().splitlines()

part_one = 0
for line in lines:
  m = len(line) // 2
  letter = (set(line[:m]) & set(line[m:])).pop()
  part_one += score(letter)

part_two = 0
for i in range(0, len(lines), 3):
  a, b, c = lines[i:i+3]
  letter = (set(a) & set(b) & set(c)).pop()
  part_two += score(letter)

print(part_one)
print(part_two)
