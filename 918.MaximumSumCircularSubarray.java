class Solution {
    public int maxSubarraySumCircular(int[] nums) {
        int currMax = nums[0];
        int currMin = nums[0];
        int globalMax = nums[0];
        int globalMin = nums[0];
        int total = nums[0];
        for (int i = 1; i < nums.length; i++){
            currMax = Math.max(currMax + nums[i], nums[i]);
            currMin = Math.min(currMin + nums[i], nums[i]);

            globalMax = Math.max(globalMax, currMax);
            globalMin = Math.min(globalMin, currMin);

            total = total + nums[i];
        }

        if (globalMax < 0 || globalMax > total - globalMin){
            return globalMax;
        } else {
            return total - globalMin;
        }
    }
}
