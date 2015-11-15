# https://leetcode.com/problems/count-primes/

import math

class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n <= 2: 
            return 0
        possible_primes = [True] * (n - 1)
        possible_primes[0] = False
        for possible_prime in range(2, int(math.ceil(math.sqrt(n)))):
            if possible_primes[possible_prime-1] == True:
                comp = possible_prime * 2
                while comp < n: 
                    possible_primes[comp-1] = False
                    comp += possible_prime
        return possible_primes.count(True)