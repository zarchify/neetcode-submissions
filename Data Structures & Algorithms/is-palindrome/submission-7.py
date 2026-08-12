class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.casefold()
        filtered = ''.join([x for x in s if x.isalnum()])
        return filtered == ''.join(reversed(filtered))