#!/bin/python3

# https://www.hackerrank.com/contests/w18/challenges/ghosts

# A: town
# B: street
# C: house
# D: apt
# sum all:
#    1. diff between A and B divisible by 3
#    2. sum of B and C divisible by 5
#    3. prod of A and C divisible by 4
#    4. GCD of A and D is 1

A, B, C, D = input().split()
A, B, C, D = int(A), int(B), int(C), int(D)

def gcd(a, b):
    while b: a, b = b, a % b
    return a

sum = 0
for a in range(1, A + 1):
    for b in range(1, B + 1):
        # cond 1
        if abs(a - b) % 3 == 0:
            for c in range(1, C + 1):
                # cond 2 & 3
                if (b + c) % 5 + (a * c) % 4 == 0: 
                    for d in range(1, D + 1):
                        if gcd(a, d) == 1:
                            sum += 1
print(sum)
