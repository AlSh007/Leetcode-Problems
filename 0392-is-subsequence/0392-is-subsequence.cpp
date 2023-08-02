class Solution {
public:
    bool isSubsequence(string s, string t) {
        int n = s.size();
        int idx = 0;
        for(int i=0;i<t.size();i++){
            if(s[idx]==t[i]) 
                idx++;
        }
        return (idx==n);
    }
};