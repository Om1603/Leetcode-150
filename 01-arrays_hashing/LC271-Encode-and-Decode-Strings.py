"""
LeetCode: Encode and decode strings
ID: 271 | Topic: Arrays & Hashing | Difficulty: medium

Approach:
-

Complexity:
- Time: O(...)
- Space: O(...)
"""

class Codec:
    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings to a single string.
      
        Each string is prefixed with its length in a 4-character wide field, 
        allowing for easy extraction during decoding.
        """
        encoded_string = []
        for string in strs:
            # '{:4}' formats the length into a 4-character wide field, 
            # padding with spaces if the number is less than 4 characters long.
            length_prefix = '{:4}'.format(len(string))
            encoded_string.append(length_prefix + string)
        return ''.join(encoded_string)

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string to a list of strings.
      
        Each string was encoded with a 4-character length prefix, which we use to 
        determine where one string ends and the next begins.
        """
        decoded_strings = []
        i = 0
        n = len(s)
        while i < n:
            # Extract the length of the next string, which is stored in the first 4 characters.
            size = int(s[i: i + 4])
            i += 4
            # Extract the string of the given length.
            decoded_strings.append(s[i: i + size])
            i += size
        return decoded_strings