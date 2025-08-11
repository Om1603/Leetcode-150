"""
LeetCode: Two Sum 2
ID: 167 | Topic: Two Pointers | Difficulty: Easy

Approach:
1. Initiate 2 pointers L & R
2. If L+R is not equal to target yet - 
3. If L+R > Target then R-=1, and if L+R < Target then L+=1
4. append L and R to res and break
5. return res
-

Complexity:
- Time: O(...)
- Space: O(...)
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n = len(numbers)
        L = 0
        R = n-1
        res = []

        while L < R:
            if numbers[L] + numbers[R] != target:
                if numbers[L] + numbers[R] < target:
                    L+=1
                else:
                    R-=1

            else:
                res.append(L+1)
                res.append(R+1)
                break
        
        return res
            
            


        