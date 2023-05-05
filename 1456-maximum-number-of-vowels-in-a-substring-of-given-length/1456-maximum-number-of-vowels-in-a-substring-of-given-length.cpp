class Solution {
public:
    int maxVowels(string s, int k) {
        int i=0,j=0;
        int countVowel=0;
        int maxCount=0;
        while(j<s.length()){
            if(s[j]=='a' or s[j]=='i' or s[j]=='e' or s[j]=='o' or s[j]=='u')
                    countVowel++;
            
            if(j-i+1==k){
                maxCount=max(maxCount,countVowel);
                if(s[i]=='a' or s[i]=='i' or s[i]=='e' or s[i]=='o' or s[i]=='u')
                    countVowel--;
                j++;
                i++;
            }
            if(j-i+1<k)
            {
                j++;
            }
        }
        return maxCount;
    }
};