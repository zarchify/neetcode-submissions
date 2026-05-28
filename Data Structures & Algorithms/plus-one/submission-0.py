class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for digit in digits:
            num = num * 10 + digit
        
        num += 1



        count = 0

        dupe = num

        while dupe > 0:
            dupe = dupe // 10
            count += 1
        new = [0] * count
        for n in range(count):
            remainder = num % 10
            num = num // 10
            new[count - n - 1] = remainder
        
        return new

