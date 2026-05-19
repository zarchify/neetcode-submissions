class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for i in range(len(nums)):
            if nums[i] in complements:
                return [complements.get(nums[i]), i]
            complements[target - nums[i]] = i

        