class Solution {
    public int removeDuplicates(int[] nums) {
        int lastUnique = 0;
        
        for (int current = 1; current < nums.length; current++){
            if (nums[lastUnique] == nums[current]){
                continue;
            }

            nums[lastUnique + 1] = nums[current];
            lastUnique++;
        }

        return lastUnique + 1;
    }
}
