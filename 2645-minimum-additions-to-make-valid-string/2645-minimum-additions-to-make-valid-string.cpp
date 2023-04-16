class Solution {
public:
    int addMinimum(string word) {
        int k=0;
        char prev='z';
        int n=word.size();
        for(int i=0;i<n;i++){
            k+=word[i]<=prev;
            prev=word[i];
        }
        return k*3-n;
    }
};