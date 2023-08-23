class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {} #dict to store index of last occuring character
        i, output = 0, 0
        for j in range(len(s)):
            if s[j] not in seen:
                output = max(output, j - i + 1)
            else: #the last occuring index can be inside the window or outside the window if it is inside we will make the first index of the window the last occurence of that character +1 else we will increase the window size
                if seen[s[j]] < i:
                    output = max(output, j - i + 1)
                else:
                    i = seen[s[j]] + 1
            seen[s[j]] = j
        return output
                