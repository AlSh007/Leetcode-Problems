class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def dp(i):
            if i>=len(questions):
                return 0
            points,jump=questions[i][0],questions[i][1]
            return max(dp(i+1),points + dp(i+jump+1))
        return dp(0)