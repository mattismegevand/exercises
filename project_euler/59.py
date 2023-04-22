#!/usr/bin/env python

import string
import itertools

def decrypt_message(key, cipher_text):
  return ''.join(chr(int(cipher_text[i]) ^ ord(key[i % len(key)])) for i in range(len(cipher_text)))

def score(decrypted_message):
  common_english_words = ["the", "be", "to", "of", "and", "in", "that", "have", "it", "is"]
  return sum(word in decrypted_message for word in common_english_words)

with open('data/0059_cipher.txt', 'r') as file:
  cipher_text = file.read().split(',')

keys = (''.join(key) for key in itertools.product(string.ascii_lowercase, repeat=3))
decryptions = ((decrypt_message(key, cipher_text), score(decrypt_message(key, cipher_text))) for key in keys)
best_decryption = max(decryptions, key=lambda x: x[1])
ascii_sum = sum(ord(c) for c in best_decryption[0])
print(ascii_sum)
