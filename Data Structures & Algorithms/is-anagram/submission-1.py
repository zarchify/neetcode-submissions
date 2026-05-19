class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        qtys = {}

        for char in s:
            if char not in qtys:
                qtys[char] = 1
                continue
            qtys[char] += 1
        

        for char in t:
            if char not in qtys:
                return False
            qtys[char] -= 1
            if qtys[char] < 0:
                return False
            elif qtys[char] == 0:
                qtys.pop(char)
        
        return len(qtys) == 0
            
        