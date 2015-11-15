#!python3

# https://www.hackerrank.com/challenges/palindrome-index/

cases = int(input())
for _ in range(cases):
    s = input()
    l_ptr = 0
    r_ptr = len(s) - 1
    rm_ptr = -1
    while l_ptr < r_ptr:
        if s[l_ptr] != s[r_ptr]:
            if s[l_ptr] != s[r_ptr - 1] or s[l_ptr + 1] != s[r_ptr - 2]:
                rm_ptr = l_ptr
            else:
                rm_ptr = r_ptr
            break
        l_ptr += 1
        r_ptr -= 1
    print(rm_ptr)