#!/bin/python3

# https://www.hackerrank.com/contests/w18/challenges/target

import math

K, N = input().split()
K, N = int(K), int(N)
R = [int(r) for r in input().split()]

res = 0
for _ in range(N):
    x, y = input().split()
    x ,y = int(x), int(y)
    r_shot = int(math.ceil(math.sqrt(x*x + y*y)))
    p_shot = 0
    if r_shot <= R[0]:
        i = 0
        j = len(R)
        # binary search in R
        while True:
            if j == i + 1:
                p_shot = j
                break
            k = i + (j - i) // 2
            if r_shot > R[k]:
                j = k
            else:
                i = k
    res += p_shot
print(res)
