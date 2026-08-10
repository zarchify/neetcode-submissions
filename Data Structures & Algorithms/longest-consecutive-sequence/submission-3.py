class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        other = {}
        highest = 1

        if not nums:
            return 0

        for num in nums:
            other[num] = True
        for num in nums:
            if (num-1) not in other:
                alive = True
                l = 1
                target = num + 1
                while alive:
                    if target in other:
                        target = target + 1
                        l += 1
                    else:
                        alive = False
                        if l > highest:
                            highest = l
        
        return highest
        