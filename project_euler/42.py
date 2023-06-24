#!/usr/bin/env python

def is_triangle(n):
  return ((8 * n + 1) ** 0.5 - 1) / 2 % 1 == 0

words = open("data/0042_words.txt").read().replace('"', '').split(',')
words = [sum(ord(c) - ord('A') + 1 for c in word) for word in words]
words = [word for word in words if is_triangle(word)]
print(len(words))
