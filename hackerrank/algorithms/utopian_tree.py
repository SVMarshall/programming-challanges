#!python3

# https://www.hackerrank.com/challenges/utopian-tree/

cases = int(input())
for _ in range(cases):
    n = int(input())
    m = 0
    for _ in range((n+1)//2):
        m = m*2 + 2
    if n % 2 == 0:
        m += 1
    print(m)