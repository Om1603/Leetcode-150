"""
LeetCode: Trapping Rain Water
ID: 42 | Topic: Two Pointers | Difficulty: Hard

Approach:

-

Complexity:
- Time: O(...)
- Space: O(...)
"""



class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l = 0
        n = len(height)
        r = n - 1

        leftmax = height[l]
        rightmax = height[r]
        res = 0

        while l < r:

            if leftmax < rightmax:
                l+=1
                leftmax = max(height[l], leftmax)
                res += leftmax - height[l]
            else:
                r-=1
                rightmax = max(height[r], rightmax)
                res += rightmax - height[r]
        
        return res