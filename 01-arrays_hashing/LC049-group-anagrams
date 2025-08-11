"""
LeetCode: Group Anagrams
ID: 049 | Topic: Arrays & Hashing | Difficulty: Medium

Approach:
-

Complexity:
- Time: O(...)
- Space: O(...)
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())



        