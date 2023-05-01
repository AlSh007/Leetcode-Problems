class Solution:
    def average(self, salary: List[int]) -> float:
        minEl=min(salary)
        maxEl=max(salary)
        sumAll=sum(salary)-minEl-maxEl
        return sumAll/(len(salary)-2)