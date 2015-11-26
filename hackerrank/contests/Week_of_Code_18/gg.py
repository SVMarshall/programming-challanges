
#!/bin/python3

# https://www.hackerrank.com/contests/w18/challenges/gg

# note: this solution still fails some test cases due to timeout (valid buy slow)

N, M = input().split()
N, M = int(N), int(M)
S = input()

# dyn prog.
calc_num_perms = [{} for _ in range(N)]

def num_perms(permut, prev, S, s_i):
    if not permut:
        return 1
    
    # dyn. prog.
    if S in calc_num_perms[s_i]:
        if prev in calc_num_perms[s_i][S]:
            return calc_num_perms[s_i][S][prev]
    else:
        calc_num_perms[s_i][S] = {}
    
    res = 0
    if S[0] == "G":
        for i in range(len(permut)):
            if permut[i] < prev:
                new_permut = list(permut)
                del(new_permut[i])
                res += num_perms(new_permut, permut[i], S[1:], s_i + 1)
            else:
                break
    else:
        for i in reversed(range(len(permut))):
            if permut[i] > prev:
                new_permut = list(permut)
                del(new_permut[i])
                res += num_perms(new_permut, permut[i], S[1:], s_i + 1)
            else:
                break
    res = res % M
    # dyn. prog.
    calc_num_perms[s_i][S][prev] = res
    return res

S = "G" + S
permut = [i for i in range(N)]
print(num_perms(permut, N, S, 0))
