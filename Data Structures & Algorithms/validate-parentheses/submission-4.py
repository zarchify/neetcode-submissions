class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = '{[('
        closes = '}])'

        for char in s:
            if opens.find(char) != -1:
                stack.append(char)
            elif closes.find(char) != -1:
                complement = opens[closes.find(char)]
                if len(stack) > 0:
                    popped = stack.pop()
                    if complement != popped:
                        return False
                else:
                    return False


        
        return len(stack) == 0