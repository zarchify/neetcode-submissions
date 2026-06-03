class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1 = ''.join(sorted(s1))
        left_index = 0
        right_index = len(s1)

        for i in range(len(s2)):
            if right_index > len(s2):
                return False
            substr = s2[left_index:right_index]
            substr = ''.join(sorted(substr))

            if s1 == substr:
                return True
            else:
                left_index += 1
                right_index += 1
            
        return False