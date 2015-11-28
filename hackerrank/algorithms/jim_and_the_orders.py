#!/bin/python3

# https://www.hackerrank.com/challenges/jim-and-the-orders/

delivers = {}
n = int(input())
for i in range(n):
    t, d = input().split()
    t, d = int(t), int(d)
    if t+d not in delivers:
        delivers[t+d] = [i]
    else:
        delivers[t+d].append(i)
print(" ".join([str(j+1) for i in sorted(delivers.keys()) for j in delivers[i]]))
