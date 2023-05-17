class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        sort(strs.begin(),strs.end());
        int i=0,j=0;
        string ans="";
        int n=strs.size();
        while(strs[0][i]==strs[n-1][j] and i<strs[0].size() and j<strs[n-1].size()){
            ans.push_back(strs[0][i]);
            i++;
            j++;
        }
        return ans;
    }
};