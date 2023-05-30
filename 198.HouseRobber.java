class Solution {
    public int rob(int[] nums) {
        if (nums.length == 1){
            return nums[0];
        }
        int rob0 = nums[0], rob1 = Math.max(nums[0], nums[1]), rob2 = 0;
        
        for (int i = 2; i < nums.length;i++){
            rob2 = Math.max(rob1, nums[i] + rob0);
            rob0 = rob1;
            rob1 = rob2;
        }

        return rob1;
    }
}
