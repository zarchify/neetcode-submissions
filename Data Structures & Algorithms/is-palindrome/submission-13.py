class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left = 0
        right = n - 1

        while left < right:
            while left < right and not s[left].casefold().isalnum():
                left += 1
            while left < right and not s[right].casefold().isalnum():
                right -= 1
            if s[left].casefold() != s[right].casefold():
                return False
            left += 1
            right -= 1

        return True