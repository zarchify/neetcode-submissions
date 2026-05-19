class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if not seen.get(num):
                seen[num] = True
            else:
                return True
        return False
            
        