class Solution:
    def average(self, salary: List[int]) -> float:
        minEl,maxEl,s=float('inf'),float('-inf'),0
        for num in salary:
            s+=num
            minEl,maxEl=min(num,minEl),max(maxEl,num)
        return (s-minEl-maxEl)/(len(salary)-2)