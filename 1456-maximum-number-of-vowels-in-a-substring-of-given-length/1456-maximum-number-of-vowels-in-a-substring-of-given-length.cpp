class Solution {
public:
    int maxVowels(string s, int k) {
        int i=0,j=0;
        int countVowel=0;
        int maxCount=0;
        bool vowels[26]={false};
        vowels[0]=vowels[4]=vowels[8]=vowels[14]=vowels[20]=true;
        for(int i=0;i<s.length();i++){
            if(i>=k and vowels[s[i-k]-'a']){
                countVowel--;
            }
            if(vowels[s[i]-'a'])
                countVowel++;
            maxCount=max(maxCount,countVowel);
        }
        return maxCount;
    }
};