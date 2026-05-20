class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []

        for word in strs:
            for char in word:
                rep = ord(char)
                rep += 1
                if rep == 128:
                    rep = 0
                new = chr(rep)
                result.append(new)
            result.append('.')
        return ''.join(result)

    def decode(self, s: str) -> List[str]:
        result = []

        curr = ""
        
        for char in s:
            if char == '.':
                result.append(curr)
                curr = ""
                continue
            rep = ord(char)
            rep -=1
            if rep < 0:
                rep = 127
            new = chr(rep)
            curr += new
        return result