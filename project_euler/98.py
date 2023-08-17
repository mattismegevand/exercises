#!/usr/bin/env python

from collections import defaultdict

words = [word.strip('"') for word in open('data/0098_words.txt').read().split(',')]

anagrams = defaultdict(list)
for w in words:
  anagrams[''.join(sorted(w))].append(w)
anagrams = {k: v for k, v in anagrams.items() if len(v) > 1}

squares_by_len = defaultdict(set)
max_len = max(len(w) for w in words)
for i in range(1, int(1e6)):
  square = i * i
  if len(str(square)) > max_len:
    break
  squares_by_len[len(str(square))].add(square)

def get_mapped_num(word, mapping):
  mapped = ''.join(mapping.get(c, '') for c in word)
  return int(mapped) if len(mapped) == len(word) else None

max_square = 0
for group in anagrams.values():
  word_length = len(group[0])
  for square in squares_by_len[word_length]:
    for i in range(len(group)):
      for j in range(i+1, len(group)):
        mapping = dict(zip(group[i], str(square)))
        if len(set(mapping.values())) < len(mapping):
          continue
        second_num = get_mapped_num(group[j], mapping)
        if second_num and (second_num in squares_by_len[word_length]):
          max_square = max(max_square, square, second_num)
print(max_square)
