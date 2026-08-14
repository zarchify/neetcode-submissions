class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n - 1
        highest = 0

        while left < right:
            rainwater = (right - left) * min(heights[left], heights[right])
            highest = max(highest, rainwater)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return highest
