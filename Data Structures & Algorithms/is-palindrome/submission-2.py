import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.casefold()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)

        for i in range(len(s) // 2):
            left = s[i]
            right = s[len(s) - i - 1]

            if left != right:
                return False
        
        return True