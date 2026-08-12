class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        dec = [(position[x], speed[x]) for x in range(n)]
        dec.sort(key=lambda x: x[0], reverse=True)
        stack = []

        for (pos, sp) in dec:
            time = (target - pos) / sp
            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)
        
        return len(stack)

