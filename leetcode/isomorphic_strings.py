# https://leetcode.com/problems/isomorphic-strings/

import collections

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        ss = collections.OrderedDict()
        tt = collections.OrderedDict()
        pos = 0
        for x, y in zip(s, t):
            lss = ss.get(x, [])
            lss.append(pos)
            ltt = tt.get(y, [])
            ltt.append(pos)
            ss[x] = lss
            tt[y] = ltt
            pos += 1
        return ss.values() == tt.values()