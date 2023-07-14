class Solution {
public:
    int longestSubsequence(vector<int>& arr, int difference) {
        int ans = 0;
        unordered_map<int,int> lengthsAt;
        for(auto i: arr){
            if(lengthsAt.count(i-difference)){
                lengthsAt[i] = lengthsAt[i-difference] + 1;
            }
            else{
                lengthsAt[i] = 1;
            }
            ans = max(ans,lengthsAt[i]);
        }
        return ans;
    }
};