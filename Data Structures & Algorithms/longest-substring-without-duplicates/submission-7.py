class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        curr = []
        offset = 0
        max_len = 0

        for c in s:
            if not c in chars:
                curr.append(c)
                chars[c] = 1
            else:
                while c in chars:
                    front = curr[offset]
                    chars.pop(front, None)
                    offset += 1
                curr.append(c)
                chars[c] = 1
            max_len = max(max_len, len(curr) - offset)
        return max_len