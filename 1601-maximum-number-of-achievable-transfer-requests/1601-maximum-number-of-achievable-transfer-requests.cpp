class Solution {
public:
    int ans = 0;
    void helper(int start,vector<int>& indegree,vector<vector<int>>& requests,int n,int count){
        if(start == requests.size()){
            for(int i=0;i<n;i++){
                if(indegree[i]!=0) //if any building has non zero indegree that state is invalid
                    return;
            }
            ans = max(count,ans);
            return;
        }
        indegree[requests[start][0]]--; //taking from first building
        indegree[requests[start][1]]++; //shifting to second building
        helper(start+1,indegree,requests,n,count+1);
        
        indegree[requests[start][0]]++; //backtracking
        indegree[requests[start][1]]--;
        helper(start+1,indegree,requests,n,count);//ignoring request
    }
    int maximumRequests(int n, vector<vector<int>>& requests) {
        vector<int> indegree(n,0);
        helper(0,indegree,requests,n,0);
        return ans;
    }
};