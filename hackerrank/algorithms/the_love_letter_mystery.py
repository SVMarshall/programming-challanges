#!python3

# https://www.hackerrank.com/challenges/the-love-letter-mystery/

cases = int(input())
for _ in range(cases):
    s = input()
    l_ptr = 0
    r_ptr = len(s) - 1
    ops = 0
    while l_ptr < r_ptr:
        if s[l_ptr] != s[r_ptr]:
            ops += abs(ord(s[l_ptr]) - ord(s[r_ptr]))
        l_ptr += 1
        r_ptr -= 1
    print(ops)