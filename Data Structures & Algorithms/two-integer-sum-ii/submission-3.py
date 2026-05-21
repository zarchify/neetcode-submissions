class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = None
        left = 0
        right = -1

        while result is None:
            l = numbers[left]
            r = numbers[right]

            if l + r > target:
                right -= 1
            elif l + r < target:
                left += 1
            else:
                result = [left + 1, len(numbers) + right + 1]

        return result
