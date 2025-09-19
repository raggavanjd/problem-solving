class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int ac = (n * ( n + 1) / 2);
        int ori = 0;
        for(int ele : nums){
            ori = ori + ele;
        }
        int res=ac - ori;
        return res;
    }
}