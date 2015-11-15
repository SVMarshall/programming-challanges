#!python3

# https://www.hackerrank.com/challenges/pangrams/

s = input()
letters = [chr(c) for c in range(ord("a"), ord("z") + 1)]
pangram = False
for c in s:
    c = c.lower()
    if c in letters:
        letters.remove(c)
        if not letters:
            pangram = True
            break
if pangram: 
    print("pangram")
else: 
    print("not pangram")