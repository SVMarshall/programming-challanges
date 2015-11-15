# https://leetcode.com/problems/valid-anagram/

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): 
            return False
        
        letters = {}
        for c in s: 
            if c in letters:
                letters[c] += 1
            else: 
                letters[c] = 1

        is_anagram = True
        for c in t:
            if c not in letters: 
                is_anagram = False
                break
            else:
                letters[c] -= 1
                if letters[c] == 0: 
                    del (letters[c])

        if len(letters) > 0: 
            is_anagram = False
        return is_anagram