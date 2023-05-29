#!/usr/bin/env python

def number_to_english(n):
  if n == 0:
    return 'zero'
  if n == 1000:
    return 'one thousand'
  ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
  teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
           'sixteen', 'seventeen', 'eighteen', 'nineteen']
  tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
          'eighty', 'ninety']
  if n < 10:
    return ones[n - 1]
  if n < 20:
    return teens[n - 10]
  if n < 100:
    return tens[n // 10 - 2] + ('' if n % 10 == 0 else '-' + number_to_english(n % 10))
  if n < 1000:
    return ones[n // 100 - 1] + ' hundred' + (' and ' + number_to_english(n % 100) if n % 100 != 0 else '')

n = 0
for i in range(1, 1001):
  s = number_to_english(i)
  n += len([c for c in s if c not in [' ', '-']])
print(n)
