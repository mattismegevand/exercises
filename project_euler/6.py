#!/usr/bin/env python

n = 100
sum_of_squares = (n*(n+1)*(2*n+1)) // 6
square_of_sum = ((n*(n+1)) // 2) ** 2
print(square_of_sum - sum_of_squares)
