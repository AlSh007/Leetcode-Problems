class Solution {
public:
    int maxValue(int n, int index, int maxSum) {
        maxSum -= n;
        int left = 0,right = maxSum, mid;
        while(left<right){
            mid = (left + right + 1)/2;
            if(test(n,index,mid) <= maxSum){
                left = mid;
            }
            else
                right = mid - 1;
        }
        return left + 1;
    }
    long test(int n,int index,int a){
        int b = max(a - index, 0); //basically the value of leftmost element in array
        long res = long(a + b)*(a - b + 1 )/2; //sum of values that are to the left of our chosen index
        b = max(a - ((n - 1) - index),0 );
        res += long(a + b)*(a - b + 1 )/2; // sum of values that are to the right of our chosen index
        return res - a; // sum of all values, subtracting a since it was added twice
    }
};