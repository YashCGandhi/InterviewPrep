class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(result, 0, nums);
        return result;
    }

    private void backtrack(List<List<Integer>> result, int index, int[] nums){
        if (index >= nums.length){
            List<Integer> currentList = new ArrayList<>();
            for (int n : nums){
                currentList.add(n);
            }
            result.add(new ArrayList(currentList));
            return;
        }

        for (int i = index; i < nums.length; i++){
            swap(nums, index, i);
            backtrack(result, index + 1, nums);
            swap(nums, index, i);
        }
    }

    private void swap(int[] nums, int index, int i){
        int tmp = nums[index];
        nums[index] = nums[i];
        nums[i] = tmp;
        
    }
}
