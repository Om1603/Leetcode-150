"""
LeetCode: Longest Consecutive Sequence
ID: 128 | Topic: Arrays & Hashing | Difficulty: Medium

Approach:
-

Complexity:
- Time: O(...)
- Space: O(...)
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sorted_arr = sorted(nums)
        longest = 1
        curr = 1

        for i in range(1, len(sorted_arr)):
            if sorted_arr[i] == sorted_arr[i - 1]:
                continue              # skip duplicates
            if sorted_arr[i] == sorted_arr[i - 1] + 1:
                curr += 1             # extend streak
                longest = max(longest, curr)
            else:
                curr = 1              # reset streak

        return longest
