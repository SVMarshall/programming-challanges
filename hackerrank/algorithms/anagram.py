#!python3

# https://www.hackerrank.com/challenges/anagram/

n = int(input())
for _ in range(n):
    s = input()
    if len(s) % 2 != 0:
        print(-1)
    else:
        letters = {}
        for c in s[ : len(s) // 2]:
            if c not in letters:
                letters[c] = 0
            letters[c] += 1
        dels = 0
        for c in s[len(s) // 2 : ]:
            if c not in letters:
                dels += 1
            else:
                letters[c] -= 1
                if letters[c] == 0:
                    del(letters[c])
        print(dels)
            
        