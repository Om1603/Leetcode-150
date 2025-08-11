"""
LeetCode: Two Sum
ID: 001 | Topic: Arrays & Hashing | Difficulty: Easy

Approach:
- Use a hashmap to store number -> index.
- For each num, check if target-num is seen.

Complexity:
- Time: O(n)
- Space: O(n)
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, x in enumerate(nums):
            need = target - x
            if need in seen:
                return [seen[need], i]
            seen[x] = i
        return []
