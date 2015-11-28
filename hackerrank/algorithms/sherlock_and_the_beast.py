#!/bin/python3

# https://www.hackerrank.com/challenges/sherlock-and-the-beast/

cases = int(input().strip())
for _ in range(cases):
    n = int(input().strip())
    res = -1
    for fives in reversed(range(n+1)):
        if fives % 3 == 0 and (n - fives) % 5 == 0:
            res = ("5"*fives + "3"*(n - fives))
            break        
    print(res)
