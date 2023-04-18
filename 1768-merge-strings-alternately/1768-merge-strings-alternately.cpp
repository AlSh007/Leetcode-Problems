class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int i=0,j=0;
        string newStr="";
        while(i<word1.size() and j<word2.size()){
            newStr.push_back(word1[i++]);
            newStr.push_back(word2[j++]);
        }
        if(i<word1.size()){
            newStr+=word1.substr(i);
        }
        if(j<word2.size()){
            newStr+=word2.substr(j);
        }
        return newStr;
    }
};