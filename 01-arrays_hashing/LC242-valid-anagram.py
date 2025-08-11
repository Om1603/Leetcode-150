"""
LeetCode: Valid Anagram
ID: 242 | Topic: Arrays & Hashing | Difficulty: Easy

Approach:
-

Complexity:
- Time: O(...)
- Space: O(...)
"""

from typing import List, Optional

class Solution:
    def todo(self):
        pass

if __name__ == "__main__":
    # quick sanity tests here
    pass


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)
        
        # Count the frequency of characters in string s
        for x in s:
            count[x] += 1
        
        # Decrement the frequency of characters in string t
        for x in t:
            count[x] -= 1
        
        # Check if any character has non-zero frequency
        for val in count.values():
            if val != 0:
                return False
        
        return True