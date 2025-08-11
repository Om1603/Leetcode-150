"""
LeetCode: Contains Duplicates
ID: 217 | Topic: Arrays & Hashing | Difficulty: Easy

Approach:
-

Complexity:
- Time: O(...)
- Space: O(...)
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True
        
