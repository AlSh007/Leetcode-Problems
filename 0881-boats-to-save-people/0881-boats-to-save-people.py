class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        num_of_boats = 0
        while left <= right:
            num_of_boats += 1
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
        
        return num_of_boats