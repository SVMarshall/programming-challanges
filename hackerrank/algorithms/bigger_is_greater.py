#!python3

# https://www.hackerrank.com/challenges/bigger-is-greater/

n = int(input())
for _ in range(n):
    try:
        s = list(input())
        rs = list(s)
        rs.reverse()
        # find first item decreasing
        #i = len(s) - 2
        i = 1
        while True:
            if rs[i] < rs[i - 1]: break
            i += 1
        # find where to put this item
        #j = len(s) - 1
        j = 0
        while True:
            if rs[j] > rs[i]: break
            j += 1
        # swap
        rs[i], rs[j] = rs[j], rs[i]
        # reverse remaining items
        #print("".join(s[: i + 1] + s[len(s) - 1 : i : -1]))
        print("".join(rs[len(rs) - 1 : i - 1 : -1] + rs[:i]))
    except IndexError:
        print("no answer")
