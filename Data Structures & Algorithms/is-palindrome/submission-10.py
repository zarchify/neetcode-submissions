class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.casefold()
        s = ''.join([x for x in s if x.isalnum()])

        for i in range(len(s) // 2):
            if s[i] != s[len(s) - i - 1]:
                return False

        return True