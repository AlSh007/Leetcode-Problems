class Solution:
    MOD = 1000000007
    def helper(self,locations,city,finish,remainFuel,memo):
        if remainFuel < 0:
            return 0
        if memo[city][remainFuel] is not None:
            return memo[city][remainFuel]
        
        total = 1 if city==finish else 0
        
        for nextCity in range(len(locations)):
            if city != nextCity and remainFuel >= abs(locations[city] - locations[nextCity]):
                total = (total + self.helper(locations,nextCity,finish,remainFuel - abs(locations[city] - locations[nextCity]),memo))%self.MOD
        memo[city][remainFuel] = total
        return total
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        memo = [[None]*(fuel+1) for i in range(n)]
        return self.helper(locations,start,finish,fuel,memo)
        