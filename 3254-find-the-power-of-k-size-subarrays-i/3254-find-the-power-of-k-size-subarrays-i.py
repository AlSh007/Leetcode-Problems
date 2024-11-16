class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        result = [-1] * (length - k + 1)
        index_deque = deque()
        
        for current_index in range(length):
            if index_deque and index_deque[0] < current_index - k + 1:
                index_deque.popleft()
            
            if (index_deque and nums[current_index] != nums[current_index - 1] + 1):
                index_deque.clear()
            
            index_deque.append(current_index)
            
            if current_index >= k - 1:
                if len(index_deque) == k:
                    result[current_index - k + 1] = nums[index_deque[-1]]
                else:
                    result[current_index - k + 1] = -1
        
        return result
