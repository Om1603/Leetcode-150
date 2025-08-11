"""
LeetCode: Valid Palindrome
ID: 125 | Topic: Two Pointers | Difficulty: Easy

Approach:
1. Initiate 2 pointers L & R
2. Check if they are alphanumeric - If not then L++/R++ and continue
3. compare S[L].lower and S[R].lower - If not equal return false
4. L++ and R--
5. Outside the loop return True
-

Complexity:
- Time: O(...)
- Space: O(...)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:

        n = len(s)
        R = n - 1
        L = 0

        while L < R:
            if not s[L].isalnum():
                L+=1
                continue

            if not s[R].isalnum():
                R-=1
                continue   

            if s[L].lower() != s[R].lower():
                return False
            
            L+=1
            R-=1
        
        return True
        