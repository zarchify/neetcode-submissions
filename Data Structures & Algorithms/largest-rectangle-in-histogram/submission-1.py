class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        result = 0

        inc_stack = []
        dec_stack = []
        inc_res = [n] * n
        dec_res = [-1] * n
        for i in range(n):
            while inc_stack and heights[inc_stack[-1]] > heights[i]:
                inc_res[inc_stack.pop()] = i
            inc_stack.append(i)

            inversed_i = n - i - 1

            while dec_stack and heights[dec_stack[-1]] > heights[inversed_i]:
                dec_res[dec_stack.pop()] = inversed_i
            dec_stack.append(inversed_i)


        for i in range(n):
            result = max(result, heights[i])
            left_height_idx = dec_res[i]
            right_height_idx = inc_res[i]
            width = right_height_idx - left_height_idx - 1
            result = max(heights[i] * width, result)

        return result

        