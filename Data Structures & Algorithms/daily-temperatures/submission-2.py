class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mon_stack = []
        result = [0] * len(temperatures)
        

        for i in range(len(temperatures)):
            while mon_stack and temperatures[mon_stack[-1]] < temperatures[i]:
                index = mon_stack.pop()
                result[index] =  i - index
            mon_stack.append(i)
        

        return result
