class Solution:
    def maxArea(self, heights: List[int]) -> int:

        val1idx = 0
        val2idx = -1
        most = 0

        for i, val in enumerate(heights):
            val1 = heights[val1idx]
            val2 = heights[val2idx]
            idx_diff = ((len(heights) + val2idx)) - val1idx
            calculated_area = idx_diff * min(val1, val2)

            if calculated_area > most:
                most = calculated_area

            if val1 <= val2:
                val1idx += 1
            elif val2 < val1:
                val2idx -= 1

        return most