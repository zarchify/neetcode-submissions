import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.casefold()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)

        for i, char in enumerate(s):
            left = char
            right = s[len(s) - i - 1]

            if left != right:
                return False
        
        return True