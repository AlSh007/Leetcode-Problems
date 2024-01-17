class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0] * n
        st = []
        for i in range(n-1, -1, -1):
            while st and heights[i] > st[-1]:
                ans[i] += 1
                st.pop()
            if st:
                ans[i] += 1
            st.append(heights[i])
        
        return ans