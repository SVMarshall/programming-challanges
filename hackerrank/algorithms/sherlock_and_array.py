#!/bin/python3

# https://www.hackerrank.com/challenges/sherlock-and-array/

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    sum_lr = []
    s = 0
    for i in a:
        sum_lr.append(s)
        s += i
    sum_rl = []
    s = 0
    for i in reversed(a):
        sum_rl.append(s)
        s += i
    res = "NO"
    for ix in range(len(a)):
        if sum_lr[ix] == sum_rl[n - ix - 1]:
            res = "YES"
            break
    print(res)
