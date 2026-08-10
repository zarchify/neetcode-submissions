class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = []
        postfixes = []

        for i in range(len(nums)):
            if i == 0:
                prefixes.append(nums[i])
            else:
                prefixes.append(prefixes[i-1] * nums[i])
            
            j = len(nums) - 1 - i
            if i == 0:
                postfixes.append(nums[j])
            else:
                postfixes.append(postfixes[i-1] * nums[j])

        
        postfixes = list(reversed(postfixes))

        results = []

        for i in range(len(nums)):
            left = prefixes[i -1] if i > 0 else 1
            right = postfixes[i+1] if i < len(nums)-1 else 1
            results.append(left * right)
        return results

        