class Solution {
    List<List<Integer>> res = new ArrayList<>();

    public void backtrack(List<Integer> pat, boolean[] used, int[] nums){
        if (pat.size() == nums.length){
            res.add(new ArrayList<>(pat));
            return;
        }
        for (int i = 0; i < nums.length; i++){
            if (used[i]){
                continue;
            }
            if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]){
                continue;
            }
            pat.add(nums[i]);
            used[i] = true;
            backtrack(pat, used, nums);
            used[i] = false;
            pat.remove(pat.size() - 1);
        }
    }

    public List<List<Integer>> permuteUnique(int[] nums) {
        boolean[] used = new boolean[nums.length];
        Arrays.sort(nums); 
        backtrack(new ArrayList<>(), used, nums);
        return res;
    }
}