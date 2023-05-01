class Solution {
public:
    double average(vector<int>& salary) {
        int size=salary.size();
        sort(salary.begin(),salary.end());
        double res=0;
        for(int i=1;i<size-1;i++){
            res+=salary[i];
        }
        return res/(size-2);
    }
};