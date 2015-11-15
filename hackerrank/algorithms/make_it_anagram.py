#!python3

# https://www.hackerrank.com/challenges/make-it-anagram/

s1 = input()
s2 = input()

letters_s1 = {}
for c in s1:
    if c not in letters_s1:
        letters_s1[c] = 0
    letters_s1[c] += 1
dels = 0
for c in s2: 
    if c not in letters_s1:
        dels += 1
    else:
        letters_s1[c] -= 1
        if letters_s1[c] == 0:
            del(letters_s1[c])
dels += sum(letters_s1.values())
print(dels)