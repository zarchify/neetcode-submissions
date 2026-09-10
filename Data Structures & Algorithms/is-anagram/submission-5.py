from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        qtys = defaultdict(int)

        for char in s:
            qtys[char] += 1
        

        for char in t:
            qtys[char] -= 1
            if qtys[char] < 0:
                return False
            elif qtys[char] == 0:
                qtys.pop(char)
        
        return len(qtys) == 0
            
        