class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i=j=0
        for val in pushed:
            pushed[i]=val
            while i>=0 and pushed[i]==popped[j]:
                i,j=i-1,j+1
            i+=1
        return i==0