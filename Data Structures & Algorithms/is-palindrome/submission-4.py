import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.casefold()
        filtered = ''.join([x for x in s if x.isalnum()])
        print(filtered)
        return filtered == ''.join(reversed(filtered))