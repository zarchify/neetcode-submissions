class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = [0] * n
        leftSeen = 0
        rightMax = [0] * n
        rightSeen = 0
        if n <= 2:
            return 0
        
        for i in range(n):
            leftSeen = max(leftSeen, height[i])
            rightSeen = max(rightSeen, height[n -i- 1])
            leftMax[i] = leftSeen
            rightMax[n-i-1] = rightSeen
        
        total = 0
        for i in range(n):
            water = min(leftMax[i], rightMax[i]) - height[i]
            total += water
        return total