class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left_index = 0
        right_index = len(s1)
        s1_tab = Counter(s1)
        substr = Counter(s2[left_index:right_index])



        for i in range(len(s2)):

            if s1_tab == substr:
                return True
            if right_index > len(s2) - 1:
                return False
            char_to_remove = s2[left_index]
            char_to_add = s2[right_index]
            left_index += 1
            right_index += 1


            substr[char_to_remove] -= 1
            if substr[char_to_remove] == 0:
                substr.pop(char_to_remove, None)
            substr[char_to_add] += 1
            print(substr)


            
        return False