class Solution {
    public int rob(int[] nums) {
        if (nums.length == 1){
            return nums[0];
        } 
        if (nums.length == 2){
            return Math.max(nums[0], nums[1]);
        } 

        return Math.max(houseRobber(nums,0, nums.length - 1), houseRobber(nums,1, nums.length));
    }

    private int houseRobber(int[] nums, int startIndex, int endIndex){
        if (nums.length == 1){
            return nums[0];
        }

        int rob0 = nums[startIndex], rob1 = Math.max(nums[startIndex + 1], nums[startIndex]), rob2 = 0;
        for (int i = startIndex  + 2; i < endIndex; i++ ){
            rob2 = Math.max(rob1, rob0 + nums[i]);
            rob0 = rob1;
            rob1 = rob2;
        }

        return rob1;
    }
}
