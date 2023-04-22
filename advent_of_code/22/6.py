#!/usr/bin/env python

line = open("6.in").read().strip()

def marker(line, length):
  for i in range(len(line)-length):
    seq = line[i:i+length]
    if len(set(seq)) == length:
      return i+length

print(marker(line, 4))
print(marker(line, 14))
