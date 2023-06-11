class Solution {
public:
    int longestPalindrome(string s) {
        int oddCount = 0;
        unordered_map<char,int> mp;
        for(char ch:s){
            mp[ch]++;
            if(mp[ch]%2 == 1)
                oddCount++;
            else{
                oddCount--;
            }
        }
        if(oddCount > 1)
            return s.length() - oddCount + 1;
        return s.length();
    }
};