class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for word in strs:
            cute = ''.join(sorted(word))
            if cute in result:
                result[cute].append(word)
            else:
                result[cute] = [word]

        return list(result.values())