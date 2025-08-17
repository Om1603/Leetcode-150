"""
LeetCode: Longest substring without repeating characters
ID: 003 | Topic: Sliding Window | Difficulty: Medium

Approach:

-

Complexity:
- Time: O(n)
- Space: O(n)
"""




class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        longest = 0
        sett = set()
        n = len(s)

        for r in range(n):

            while s[r] in sett:
                sett.remove(s[l])
                l += 1
        
            w = (r - l) + 1
            sett.add(s[r])
            longest = max(longest, w)

        return longest