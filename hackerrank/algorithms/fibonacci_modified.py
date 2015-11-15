#!python3

# https://www.hackerrank.com/challenges/fibonacci-modified/

# Computing serie:
#	T_(n+2) = T_(n+1)^2 + T_n

a, b, n = input().split()
a, b, n = int(a), int(b), int(n)
i = 2
while i < n:
    c = b*b + a
    a, b = b, c
    i += 1
print(c)