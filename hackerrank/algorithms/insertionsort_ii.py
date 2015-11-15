#!python3

# https://www.hackerrank.com/challenges/insertionsort2/

n = int(input())
ar = list(map(int, input().split()))

def insert_last(ar, n):
    num = ar[n-1]
    for i in reversed(range(-1, n)):
        if i > 0 and ar[i-1] > num:
            ar[i] = ar[i-1]
        else:
            ar[i] = num
            break

for i in range(1, n):
    insert_last(ar, i+1)
    print(" ".join(map(str, ar)))