class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = ""
        max_seen = 0
        for char in s:
            if not char in curr:
                curr = curr + char
            else:
                curr = curr[curr.find(char)+1:] + char
            max_seen = max(max_seen, len(curr))
        return max_seen