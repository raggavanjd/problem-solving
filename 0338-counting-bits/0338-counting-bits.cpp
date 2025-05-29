class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> arr(n+1);
        int k=0;
        for(int i=0;i<=n;i++){
            arr[k++]=i%2 +arr[i/2];
        }
        return arr;
    }
};