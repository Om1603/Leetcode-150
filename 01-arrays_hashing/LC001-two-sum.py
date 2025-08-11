"""
LeetCode: Two Sum
ID: 001 | Topic: Arrays & Hashing | Difficulty: Easy

Approach:
-

Complexity:
- Time: O(...)
- Space: O(...)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for indx, vals in enumerate(nums):
            diff = target - vals

            if diff in hashmap:
                return [indx, hashmap[diff]]
            hashmap[vals] =  indx