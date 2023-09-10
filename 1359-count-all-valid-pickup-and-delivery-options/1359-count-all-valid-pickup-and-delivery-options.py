class Solution:
    def countOrders(self, n: int) -> int:
        mod = 10**9 + 7
        pickup_permutation = math.factorial(n)%mod
        delievery_permutation = reduce(mul,range(1,2*n,2),1)%mod
        return pickup_permutation*delievery_permutation%mod