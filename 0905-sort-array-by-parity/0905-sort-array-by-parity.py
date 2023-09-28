class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd_list = []
        even_list = []
        for num in nums:
            if num%2 == 0:
                even_list.append(num)
            else:
                odd_list.append(num)
        return even_list+odd_list