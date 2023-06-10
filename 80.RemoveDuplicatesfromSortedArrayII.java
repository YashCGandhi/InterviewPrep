class Solution {
    
    public int removeDuplicates(int[] nums) {
        if (nums.length < 3) {
            return nums.length;
        }
        int index = 2;
        for( int i = 2; i < nums.length; i++){
            if(nums[index - 2] != nums[i]){
                nums[index] = nums[i];
                index++;
            }
            
        }
        return index;
    }
}
