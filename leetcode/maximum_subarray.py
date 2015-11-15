# https://leetcode.com/problems/maximum-subarray/

class Solution:
    
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        
        # using a class -> 94ms 
        # class SubArray:
        #    def __init__(self): 
        #        self.value = None
        #        self.x = self.y = 0
        # sol = SubArray()
        # alt = SubArray()
        #
        # using a list -> 78ms
        # SubArray => [value, x, y]
        #
        # using vars ->
        sol_value = alt_value = None
        sol_x = sol_y = alt_x = alt_y = 0
        
        for i in range(len(A)):
            if sol_value is None:
                sol_value = A[i]
                alt_value = A[i]
                continue
            if A[i] > 0 or A[i] > sol_value: 
                # upgrading solution if next value positive
                if i == sol_y + 1 and sol_value > 0:
                    sol_y = i
                    sol_value = sol_value + A[i]
                # cannot upgrade, but better create a new solution with the current number
                elif A[i] > sol_value:
                    sol_x = sol_y = i
                    sol_value = A[i]
                # if valid, is "alt" better?
                if i == alt_y + 1 and alt_value > 0:
                    alt_value = alt_value + A[i]
                    alt_y = i
                    if alt_value > sol_value:
                        sol_value = alt_value
                        sol_x = alt_x
                        sol_y = alt_y
                # initialize "alt" if it gets old
                else:
                    alt_x = alt_y = i
                    alt_value = A[i]
                    
            # neg, number. carry on "alt" if sum. still positive
            elif A[i] < 0:
                alt_value = alt_value + A[i]
                if alt_value > 0:
                    alt_y = i
            
            # 0 case
            else:
                if i == sol_y + 1: sol_y = i
                if i == alt_y + 1: alt_y = i
                
        return sol_value