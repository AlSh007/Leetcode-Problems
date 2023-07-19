class Solution {
public:
   static bool comp(vector<int>&a,vector<int>&b){
        return a[1]<b[1];
    }
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if(intervals.size()<=1) return 0;
        int prevIndex=0;
        int eraseCount=0;
        
        sort(intervals.begin(),intervals.end(),comp);
        for(int i=1;i<intervals.size();i++){
            if(intervals[prevIndex][1]>intervals[i][0]){
                eraseCount++;
            }
            else prevIndex=i;
        }
        return eraseCount;
    }
};