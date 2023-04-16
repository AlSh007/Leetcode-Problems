class Solution {
public:
    int maxDivScore(vector<int>& nums, vector<int>& divisors) {
        int maxScore=0;
        sort(divisors.begin(),divisors.end());
        int ans=divisors[0];
        for(int i=0;i<divisors.size();i++){
            int curScore=0;
            for(int j=0;j<nums.size();j++){
                if(nums[j]%divisors[i]==0)
                    curScore+=1;
            }
            if(curScore>maxScore)
            {
                maxScore=curScore;
                ans=divisors[i];
            }
        }
        return ans;
    }
};