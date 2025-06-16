class Solution {
public:
    bool canPartition(vector<int>& nums) {
      int  s = 0;
      for(int i: nums)
        s += i;

        if(s%2 != 0)
            return false;

        int t = s /2;
        int n = nums.size();

        vector<bool> dp(t+1,0);
        dp[0] = true;

        for(int n : nums){
            for(int j=t;j>=n;j--){
                dp[j] = dp[j] || dp[j-n];
            }
        }
        return dp[t];
    }
};