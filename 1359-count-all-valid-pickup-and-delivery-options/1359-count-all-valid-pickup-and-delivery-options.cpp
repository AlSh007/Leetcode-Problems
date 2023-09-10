class Solution {
public:
    int countOrders(int n) {
        long long res = 1,mod = 1e9+7;
        for(int i=1;i<=n;i++)
            res = (res*i)%mod;
        for(int i=1;i<2*n;i+=2)
            res = (res*i)%mod;
        return res%mod;
    }
};