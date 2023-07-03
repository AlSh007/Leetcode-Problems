class Solution {
public:
    bool buddyStrings(string s, string goal) {
        if(s.length()!=goal.length())
            return false;
        if(s==goal and set<char>(s.begin(),s.end()).size()<s.size()) //both string are equal and they have duplicates
            return true;
        vector<int> diff;
        for(int i=0;i<s.size();i++){
            if(s[i]!=goal[i])
                diff.push_back(i);
        }
        return diff.size()==2 and s[diff[0]]==goal[diff[1]] and goal[diff[0]]==s[diff[1]];
    }
};