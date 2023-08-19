class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = strs.sort()
        string = ''
        for i,j in zip(strs[0],strs[-1]):
            if i == j:
                string += i
            else:
                break
        
        return string