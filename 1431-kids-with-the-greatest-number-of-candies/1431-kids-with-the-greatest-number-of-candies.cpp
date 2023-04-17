class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> ans;
        int maxVal=0;
        for(int i=0;i<candies.size();i++){
            if(candies[i]>maxVal)
                maxVal=candies[i];
        }
        for(int i=0;i<candies.size();i++){
            if(candies[i]+extraCandies>=maxVal)
                ans.push_back(true);
            else
                ans.push_back(false);
        }
        return ans;
    }
};